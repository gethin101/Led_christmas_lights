#code in CircuitPython

import time
import board
import leds
import dfplayer
import voice

# -----------------------
# Initialize Modules
# -----------------------
strip = leds.LEDs(pin=board.GP0, num_leds=60)  # adjust pin + number
player = dfplayer.DFPlayer(tx=board.GP4, rx=board.GP5)
speech = voice.VoiceModule()

print("System initialized!")

# -----------------------
# Main Loop
# -----------------------
while True:
    command = speech.listen()

    if command == "play music":
        print("Playing song...")
        player.play_track(1)           # plays 0001.mp3
        strip.rainbow_cycle(0.003)

    elif command == "lights on":
        strip.set_color((255, 0, 0))

    elif command == "lights off":
        strip.off()

    time.sleep(0.1)


