# Event-Driven Spiking Cortical Model (ESCM)

This repository contains the implementation of the **Event-Driven Spiking Cortical Model (ESCM)** as described in the paper **“Persistent Representation of Event Camera Output Using Spiking Neural Networks”**. The ESCM addresses the static scene blindness of event cameras by generating a persistent, spiking representation of visual data through recurrent connections and tailored synaptic dynamics.  

## Overview

Event cameras capture changes in brightness asynchronously with high temporal resolution, but they often overlook static scenes where little change occurs. Inspired by biological visual persistence (as well as mechanisms such as microsaccades), ESCM uses a spiking neural network (SNN) to retain relevant scene information even in the absence of motion.

Key points of the approach include:
- **Persistent Representation:** ESCM maintains and updates spatial information over time via recurrent connections.
- **Neuronal Dynamics:** The model utilizes Leaky Integrate-and-Fire (LIF) neurons with both excitatory autapses and inhibitory synapses defined over a linking field.
- **Practical Implementation:** The code offers both a Jupyter Notebook (`ESCM_W.ipynb`) and a Python script (`ESCM.py`) that can be executed directly.

Feel free to contact me via email (bernard.maacaron@iit.it) for any questions or suggestions regarding the implementation or the underlying model.

## Repository Contents

- **ESCM_W.ipynb:** Jupyter Notebook implementation for interactive exploration and simulation.
- **ESCM.py:** Standalone Python script equivalent of the notebook.
- **Persistent Representation of Event Camera Output Using Spiking Neural Networks.pdf:** The attached paper detailing the model architecture, experiments, and results.

## Installation

Before running the code, ensure that you have Python 3.7 or later installed. I recommend using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/) for managing virtual environments.
To set up the environment:

```bash
# Clone the repository
git clone https://github.com/BernardMaacaron/Event-SCM
cd Event-SCM

# Create a virtual environment with virtualenvwrapper (replace "event-scm" with your preferred env name)
mkvirtualenv event-scm

# Install required packages; if a requirements.txt exists, run:
pip install -r requirements.txt
```

If no requirements file is provided for any reason, ensure you at least have installed the following packages:
- [Brian2](https://brian2.readthedocs.io)
- NumPy (not recommended - Brian2 provides its own set of NumPy functions adapted to work with the unit system of Brian2)
- Matplotlib
- Jupyter Notebook (if using the notebook)

## Usage

There are two ways to run the simulations:

1. **Using the Jupyter Notebook:**
   - Launch Jupyter Notebook from the repository’s directory:
     ```bash
     jupyter notebook ESCM_W.ipynb
     ```
   - Execute all the cells in the notebook to run the simulations and visualize the persistent spiking output.

2. **Using the Python Script:**
   - Run the Python script directly:
     ```bash
     python ESCM.py
     ```
   - The script will execute the same simulation logic as the notebook, generating the outputs based on the implemented ESCM dynamics.

## Camera-event loader

The first refactored block is `event_input.py`. It loads one YARP recording
directory and selects an explicit DVS channel, independently of Brian. The
existing simulations still use their original loading code.

Install its dependencies with `python -m pip install -r requirements-input.txt`.
The decoder is pinned because timestamp-clock defaults differ between bimvee
versions. Supply the recording's decoded timestamp tick duration explicitly:

```python
from event_input import load_events

recording = load_events(recording_directory, channel="left", width=346, height=260,
                        timestamp_clock_ns=timestamp_tick_ns)
events = recording["events"]
ts, x, y, pol = (events[key] for key in ("ts", "x", "y", "pol"))
```

`recording_directory` must identify one recording, rather than a dataset root
containing several recordings. `timestamp_tick_ns` is the timestamp encoding's
tick duration, **not the simulation timestep**. For logs with event timestamps,
use their actual tick duration. For logs without event timestamps, bimvee derives
microsecond ticks from bottle timestamps, requiring `timestamp_tick_ns = 1000`.
Sensor dimensions must be supplied; they are not inferred from active pixels.

Returned timestamps are in seconds, unwrapped by bimvee, with zeroing disabled.
The loader preserves decoded event order, repeated events, both polarities,
and event metadata such as `tsOffset` when present. Importer metadata, including
`tsOffsetFromInfo` when available, remains in `recording["info"]`. These timestamps
are not necessarily absolute wall-clock times. The return value also records
`width`, `height`, `channel`, `source`, `timestamp_unit`, and `timestamp_clock_ns`.

Invalid array shapes, timestamps, coordinates, or polarity values raise errors.
The loader does not sort, filter, deduplicate, rescale time, or generate Brian
spikes. It preserves what bimvee decodes; bimvee's format detection, timestamp
unwrapping, and handling of malformed packets remain decoder responsibilities.

Loader contract tests use mocked decoded arrays and do not establish decoder
compatibility with a recording. Run them from the repository root with:

```bash
python -m unittest discover -s tests -p 'test_event_input.py'
```

## Experiments and Results

The implementation is designed to replicate key experimental results from the attached paper. In brief:
- **Datasets:** The model has been evaluated on various event camera datasets (e.g., MVSEC Outdoor Day1, Event-Human3.6m).
- **Metrics:** Evaluations are performed using metrics such as Normalized Mutual Information (NMI) and Structural Similarity Index (SSIM) to compare the persistent representation (ESCM) against standard representations like EROS.
- **Observations:** The ESCM achieves a balance between suppressing noise (typical in high event-rate scenarios) and retaining essential scene information in static or low-motion conditions.

For more details on the methodology and experimental evaluation, please refer to the attached paper.

## Contributing

Contributions to this project are welcome! If you find a bug or have suggestions for improvements, please open an issue or submit a pull request.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is distributed under the [MIT License](LICENSE).

## Acknowledgments

- The design and implementation of the ESCM are based on the ideas presented in the paper **“Persistent Representation of Event Camera Output Using Spiking Neural Networks”**.
- Special thanks to the EDPR group at the Italian Institute of Technology for their support and collaboration.
