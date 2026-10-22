"""Original ESCM neuron dynamics, isolated from network wiring."""

from brian2 import NeuronGroup, ms

EQUATIONS = """
dv/dt = (-v + ExtIn + P * (Exc + Inh)) / tau : 1
dExtIn/dt = -ExtIn / tau : 1
dExc/dt = -Exc / tau : 1
dInh/dt = -Inh / tau : 1
P : integer
incoming_spikes : integer
X : integer
Y : integer
"""


def create_neurons(n, *, tau=0.2 * ms, threshold=0.1, reset=0.0):
    """Create the legacy neuron population, without synapses or persistence events."""
    group = NeuronGroup(
        n,
        EQUATIONS,
        threshold="v > vt",
        reset="v = vr",
        method="exact",
        namespace={"tau": tau, "vt": threshold, "vr": reset},
    )
    # Brian2 initializes all state variables to zero.
    return group
