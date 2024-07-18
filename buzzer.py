from machine import Pin, PWM
from time import sleep

# Define the frequency of the notes (in Hertz) and their duration (in seconds)
tune = [
    (261.63, 0.5),  # C4
    (293.66, 0.5),  # D4
    (329.63, 0.5),  # E4
    (349.23, 0.5),  # F4
    (392.00, 0.5),  # G4
    (440.00, 0.5),  # A4
    (493.88, 0.5),  # B4
    (523.25, 0.5),  # C5
]

# Initialize the buzzer and button
try:
    buzzer = PWM(Pin(15))
    button = Pin(14, Pin.IN, Pin.PULL_DOWN)

    # Function to play the tune
    def play_tune():
        for frequency, duration in tune:
            buzzer.freq(int(frequency))
            buzzer.duty_u16(32000)  # Set duty cycle to 50%
            sleep(duration)
            buzzer.duty_u16(0)
            sleep(0.1)  # Short pause between notes

    while True:
        if button.value():
            play_tune()
        else:
            buzzer.duty_u16(0)
        sleep(0.1)
finally:
    buzzer.duty_u16(0)
