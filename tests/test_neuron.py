"""Minimal checks for the original ESCM neuron equations."""

import numpy as np
from brian2 import Network, defaultclock, ms, start_scope

from escm.neuron import create_neurons


def test_decay_without_inputs():
    start_scope()
    defaultclock.dt = 0.01 * ms
    neuron = create_neurons(1)
    neuron.v = 0.05
    neuron.ExtIn = 0.0
    net = Network(neuron)
    net.run(0.2 * ms)
    np.testing.assert_allclose(float(neuron.v[0]), 0.05 * np.exp(-1), rtol=1e-8)


def test_input_trace_decays_without_events():
    start_scope()
    defaultclock.dt = 0.01 * ms
    neuron = create_neurons(1)
    neuron.ExtIn = 0.5
    net = Network(neuron)
    net.run(0.2 * ms)
    np.testing.assert_allclose(float(neuron.ExtIn[0]), 0.5 * np.exp(-1), rtol=1e-8)
