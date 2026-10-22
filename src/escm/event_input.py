"""Load one YARP camera recording without applying model preprocessing."""

from operator import index
from pathlib import Path

import numpy as np
from bimvee.importIitYarp import importIitYarp


def load_events(path, *, channel, width, height, timestamp_clock_ns):
    """Return decoded events, sensor dimensions, and source metadata.

    ``path`` is a YARP recording directory containing data.log or
    binaryevents.log, optionally with info.log. Select the decoded channel
    explicitly, e.g. "left" or "right"; directories yielding multiple
    recordings are rejected.

    ``timestamp_clock_ns`` is the duration of a decoded timestamp tick in
    nanoseconds (bimvee's ``clock`` argument). For logs without per-event
    timestamps, bimvee synthesizes ticks from bottle times in microseconds;
    those logs require 1000. For timestamped events, use the recording's
    actual tick duration. This is independent of Brian's simulation clock.

    ``events`` retains bimvee's arrays and metadata, including tsOffset when
    present. Timestamps are unwrapped by bimvee and expressed in seconds;
    timestamp zeroing is disabled. They are not necessarily wall-clock time.
    ``info`` retains importer metadata, including tsOffsetFromInfo when
    available. No sorting, filtering, deduplication, or model conversion occurs.
    """
    path = Path(path).resolve(strict=True)
    if not path.is_dir():
        raise ValueError("path must be a YARP recording directory")
    width, height = index(width), index(height)
    if width <= 0 or height <= 0:
        raise ValueError("width and height must be positive integers")
    if not np.isfinite(timestamp_clock_ns) or timestamp_clock_ns <= 0:
        raise ValueError("timestamp_clock_ns must be finite and positive")

    recording = importIitYarp(filePathOrName=str(path), splitChannel=True,
                              zeroTimestamps=False, clock=timestamp_clock_ns)
    if not isinstance(recording, dict):
        raise ValueError("path must contain exactly one recording; select its directory explicitly")
    channels = recording["data"]
    if channel not in channels or "dvs" not in channels[channel]:
        available = [name for name, data in channels.items() if "dvs" in data]
        raise ValueError(f"No DVS stream for channel {channel!r}; available channels: {available}")
    events = channels[channel]["dvs"]
    ts, x, y, pol = (events[key] for key in ("ts", "x", "y", "pol"))
    if any(values.ndim != 1 or values.size != ts.size for values in (ts, x, y, pol)):
        raise ValueError("ts, x, y, and pol must be one-dimensional arrays of equal length")
    if not np.all(np.isfinite(ts)) or np.any(ts[1:] < ts[:-1]):
        raise ValueError("timestamps must be finite and nondecreasing")
    if not np.issubdtype(x.dtype, np.integer) or not np.issubdtype(y.dtype, np.integer):
        raise ValueError("pixel coordinates must be integers")
    if np.any((x < 0) | (x >= width)) or np.any((y < 0) | (y >= height)):
        raise ValueError("pixel coordinates are outside the supplied sensor dimensions")
    if not np.all((pol == 0) | (pol == 1)):
        raise ValueError("decoded polarity must contain only 0/1 or False/True")

    return {"events": events, "width": width, "height": height, "channel": channel,
            "source": str(path), "timestamp_unit": "s", "timestamp_clock_ns": timestamp_clock_ns,
            "info": recording["info"]}
