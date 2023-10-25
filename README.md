Considering the basic prototype provided, here's an updated README:

---

# BeatLearner: Basic Machine Learning Music Improv AI 🎵

---

## Introduction

**BeatLearner** is a simple prototype designed to introduce the concept of generating music programmatically. It's not fully AI-driven yet, but serves as a starting point for those looking to blend technology with music.

---

## Features

1. **Genre Selection** - Currently supports Jazz and EDM genres with predefined scales.
2. **Customizable Tempo** - Adjust the beats per minute to your liking.
3. **MIDI Output** - Save your generated beats as MIDI files for external playback.

---

## Quick Start

1. **Installation**:

   You need to install MIDIUtil for BeatLearner to work:

   ```bash
   pip install MIDIUtil
   ```

2. **Usage**:

   ```python
   from beatlearner import BeatMaker
   
   # Initialize BeatMaker
   beat = BeatMaker()
   
   # Generate a beat based on default settings
   beat.generate()
   
   # Save the beat as a MIDI file
   beat.save("output.mid")
   ```

---

## Customization

You can adjust several parameters:

- **Genre**: Choose between Jazz and EDM.
- **BPM (Beats Per Minute)**: Adjust your desired tempo using the `set_tempo` method.

---

## Contribute

Though BeatLearner is a basic prototype, we welcome all music enthusiasts, developers, and machine learning experts to join in refining and expanding this concept.

- Fork the repository.
- Create your feature branch (`git checkout -b feature/AmazingFeature`).
- Commit your changes (`git commit -m 'Add some AmazingFeature'`).
- Push to the branch (`git push origin feature/AmazingFeature`).
- Open a Pull Request.

---

**Embark on a musical journey with a touch of code! 🎼**
