"""Loader contract tests; decoder output is supplied explicitly."""

import unittest
from tempfile import TemporaryDirectory
from unittest.mock import patch

import numpy as np

from escm.event_input import load_events


class EventInputTests(unittest.TestCase):
    def setUp(self):
        directory = TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.path = directory.name
        self.events = {"ts": np.array([12.0, 12.0, 12.5]), "x": np.array([1, 1, 2]),
                       "y": np.array([0, 0, 1]), "pol": np.array([True, False, True]),
                       "tsOffset": 0.0}
        self.recording = {"data": {"right": {"dvs": self.events}},
                          "info": {"tsOffsetFromInfo": 123.0}}
        self.args = {"channel": "right", "width": 3, "height": 2, "timestamp_clock_ns": 1000}
        importer = patch("escm.event_input.importIitYarp", return_value=self.recording)
        self.decode = importer.start()
        self.addCleanup(importer.stop)

    def test_preserves_events_and_metadata(self):
        result = load_events(self.path, **self.args)
        self.assertIs(result["events"], self.events)
        self.assertIs(result["info"], self.recording["info"])
        np.testing.assert_array_equal(result["events"]["ts"], [12.0, 12.0, 12.5])
        np.testing.assert_array_equal(result["events"]["pol"], [True, False, True])
        self.assertEqual((result["width"], result["height"], result["channel"]), (3, 2, "right"))
        self.assertEqual(result["timestamp_unit"], "s")
        self.decode.assert_called_once_with(filePathOrName=result["source"], splitChannel=True,
                                            zeroTimestamps=False, clock=1000)

    def test_requires_explicit_existing_channel(self):
        self.args["channel"] = "left"
        with self.assertRaisesRegex(ValueError, "available channels.*right"):
            load_events(self.path, **self.args)

    def test_rejects_multiple_recordings(self):
        self.decode.return_value = [self.recording, self.recording]
        with self.assertRaisesRegex(ValueError, "exactly one recording"):
            load_events(self.path, **self.args)

    def test_rejects_invalid_decoded_arrays(self):
        cases = [("ts", [12.0, 11.0, 12.5]), ("ts", [12.0, np.nan, 12.5]),
                 ("x", [1, 2]), ("x", [[1, 1, 2]]), ("x", [1.0, 1.0, 2.0]),
                 ("x", [1, 1, 3]), ("y", [0, -1, 1]), ("pol", [0, 2, 1])]
        for key, values in cases:
            with self.subTest(key=key, values=values):
                events = {**self.events, key: np.array(values)}
                self.decode.return_value = {"data": {"right": {"dvs": events}}, "info": {}}
                with self.assertRaises(ValueError):
                    load_events(self.path, **self.args)

    def test_rejects_invalid_geometry_and_clock(self):
        for key, value in [("width", 0), ("height", -1), ("timestamp_clock_ns", 0),
                           ("timestamp_clock_ns", np.inf)]:
            with self.subTest(key=key, value=value), self.assertRaises(ValueError):
                load_events(self.path, **{**self.args, key: value})
        self.decode.assert_not_called()


if __name__ == "__main__":
    unittest.main()
