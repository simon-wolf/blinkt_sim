#!./env/bin/python3
import time

try:
    import blinkt
    print("Blinkt! detected")
except ImportError:
    from blinkt_sim import blinktsim as blinkt
    print("Using Blinkt! simulator")

print("\nPress Ctrl+C to exit")
while True:
    for i in range(8):
        blinkt.clear()
        blinkt.set_pixel(i, 255, 0, 0, 0.75)
        blinkt.show()
        time.sleep(0.1)
