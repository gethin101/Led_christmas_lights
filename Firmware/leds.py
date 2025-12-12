#code in CircuitPython

import time
import neopixel

class LEDs:
    def __init__(self, pin, num_leds):
        self.num_leds = num_leds
        self.pixels = neopixel.NeoPixel(pin, num_leds, brightness=0.4, auto_write=False)

    def set_color(self, color):
        for i in range(self.num_leds):
            self.pixels[i] = color
        self.pixels.show()

    def off(self):
        self.set_color((0, 0, 0))

    def rainbow_cycle(self, wait):
        for j in range(255):
            for i in range(self.num_leds):
                pixel_index = (i * 256 // self.num_leds) + j
                self.pixels[i] = self.wheel(pixel_index & 255)
            self.pixels.show()
            time.sleep(wait)

    def wheel(self, pos):
        if pos < 85:
            return (255 - pos * 3, pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return (0, 255 - pos * 3, pos * 3)
        else:
            pos -= 170
            return (pos * 3, 0, 255 - pos * 3)
