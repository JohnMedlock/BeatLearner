## BeatLearner: Real-time Music Improvisation AI

### Overview

BeatLearner is an AI-driven music generation tool that improvises and plays musical sequences in real-time. Inspired by different genres like Jazz and EDM, BeatLearner not only creates MIDI sequences but also plays them immediately, giving users an immersive music creation experience.

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- `pygame` for real-time MIDI playback
- `midiutil` for MIDI sequence generation

### Installation

1. Clone the repository:

```bash
git clone [URL_TO_YOUR_REPOSITORY]
```

2. Navigate to the project directory:

```bash
cd BeatLearner
```

3. Set up a Python virtual environment:

```bash
/usr/bin/python3 -m venv venv
```

4. Activate the virtual environment:

```bash
source venv/bin/activate
```

5. Install the required Python packages:

```bash
pip install pygame midiutil
```

### Usage

To start the real-time music improvisation:

```bash
python BeatLearner.py
```

The program will continuously generate and play music based on the pre-defined genres. To stop the program, interrupt it manually, typically using `Ctrl + C`.

### Customization

Inside the `BeatLearner.py` script, you can:

- Modify the available genres and associated notes.
- Adjust the tempo for the sequences.
- Randomize tempo and genre to introduce more variety in the generated sequences.

