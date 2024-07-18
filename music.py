import RPi.GPIO as GPIO
import time

# Set up the GPIO pin for the buzzer
buzzer_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

# Define the frequency of the notes (in Hertz)
notes = {
    "C4": 261.63,
    "D4": 293.66,
    "E4": 329.63,
    "F4": 349.23,
    "G4": 392.00,
    "A4": 440.00,
    "B4": 493.88,
    "C5": 523.25,
}

# Define the tune as a sequence of (note, duration) tuples
tune = [
    ("C4", 0.4),
    ("D4", 0.4),
    ("E4", 0.4),
    ("F4", 0.4),
    ("G4", 0.4),
    ("A4", 0.4),
    ("B4", 0.4),
    ("C5", 0.4),
]


# Function to play a note
def play_note(frequency, duration):
    if frequency == 0:  # Rest note
        time.sleep(duration)
        return

    p = GPIO.PWM(buzzer_pin, frequency)
    p.start(50)  # Duty cycle of 50%
    time.sleep(duration)
    p.stop()


# Play the tune
for note, duration in tune:
    play_note(notes[note], duration)
    time.sleep(0.05)  # Short pause between notes

# Clean up GPIO settings
GPIO.cleanup()
