#circuitpython

import time
import busio
from adafruit_bus_device.uart_device import UARTDevice

class DFPlayer:
    def __init__(self, tx, rx):
        uart = busio.UART(tx, rx, baudrate=9600)
        self.device = UARTDevice(uart, None)

    # Build DFPlayer command
    def _send(self, cmd, param=0):
        high = (param >> 8) & 0xFF
        low = param & 0xFF
        packet = bytearray([
            0x7E, 0xFF, 0x06,
            cmd, 0x00, high, low,
            0xEF
        ])
        with self.device as uart:
            uart.write(packet)
        time.sleep(0.1)

    # Public functions
    def play_track(self, num):
        self._send(0x03, num)

    def stop(self):
        self._send(0x16)

    def volume(self, level):
        self._send(0x06, max(0, min(30, level)))
