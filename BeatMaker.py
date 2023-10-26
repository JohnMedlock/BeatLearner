import pygame
from midiutil import MIDIFile
import random
import io

class BeatMaker:
    def __init__(self):
        self.tempo = 120
        self.duration = 48  # default duration of the beat in beats
        self.genres = {
            "Jazz": [60, 62, 64, 67, 69, 71],  # Example jazz notes (C Major Pentatonic)
            "EDM": [60, 64, 65, 67, 71, 72],  # Example EDM notes (C Major Scale)
        }
        self.current_genre = "Jazz"
        self.midi = None

        print(f"Initialized with the {self.current_genre} genre.")  # Print statement here

    def _initialize_midi(self):
        self.midi = MIDIFile(1, adjust_origin=True)
        self.midi.addTempo(0, 0, self.tempo)

    def set_tempo(self, tempo):
        self.tempo = tempo

    def select_genre(self, genre):
        if genre in self.genres:
            self.current_genre = genre
        else:
            print(f"Genre {genre} not found. Using the current genre: {self.current_genre}.")

    def generate(self):
        self._initialize_midi()
        track = 0
        time = 0
        for _ in range(self.duration):
            note = random.choice(self.genres[self.current_genre])
            self.midi.addNote(track, 0, note, time, 1, 100)  # 1 beat duration, 100 velocity
            time += 1

    def save(self, filename="beatlearner_output.mid"):
        with open(filename, "wb") as midi_file:
            self.midi.writeFile(midi_file)
        print(f"File saved as {filename}")

    def play(self):
        # Convert the MIDI data to a bytes-like object
        midi_stream = io.BytesIO()
        self.midi.writeFile(midi_stream)
        midi_stream.seek(0)
        
        # Initialize pygame mixer and play the MIDI
        pygame.mixer.init()
        pygame.mixer.music.load(midi_stream)
        pygame.mixer.music.play()

        # Keep the program running while the music is playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
if __name__ == "__main__":
    while True:  # Infinite loop to generate and play music non-stop
        beat = BeatMaker()
        
        # Optionally, you can add code here to randomize tempo and genre for variety
        # beat.set_tempo(random.choice(range(80, 141)))  # Random tempo between 80 to 140
        # beat.select_genre(random.choice(["Jazz", "EDM"]))  # Random genre
        
        beat.generate()
        beat.play()
