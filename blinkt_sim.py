"""
A simulator for Pimoroni's Blink!
https://shop.pimoroni.com/products/blinkt
Uses Pygame for the UI.
https://www.pygame.org/news
"""

import sys
import pygame.gfxdraw

NUM_PIXELS = 8
PIXEL_BOUNDARY = 50

try:
    import pygame
except ImportError:
    print("To simulate a Blinkt! on your computer, please 'pip install pygame'")


class BlinktSim(object):
    """ Simulate the Blink! library (https://github.com/pimoroni/blinkt)"""

    def __init__(self):
        # Set up the instance variables
        self.clear_on_exit = True
        self.pixels = [(0, 0, 0, 0.2)] * NUM_PIXELS

        # Init pygame and clear the display
        pygame.init()
        pygame.display.set_caption("Blinkt! Simulator")
        self.screen = pygame.display.set_mode(
            [NUM_PIXELS * PIXEL_BOUNDARY, PIXEL_BOUNDARY])
        self.clear()

    def _exit(self):
        """Placeholder for compatibility."""
        pass

    def set_brightness(self, brightness):
        """Set the brightness of all pixels
        :param brightness: Brightness: 0.0 to 1.0 (default around 0.2)
        """

        if brightness < 0 or brightness > 1:
            raise ValueError("Brightness should be between 0.0 and 1.0")

        for x in range(NUM_PIXELS):
            self.pixels[x][3] = int(255.0 * brightness)

    def clear(self):
        """Clear the pixel buffer"""
        self.set_all(0, 0, 0, 0)
        self.screen.fill((0, 0, 0))

    def show(self):
        """Output the buffer to pygame"""
        self.draw()
        pygame.display.update()

    def set_all(self, r, g, b, brightness=None):
        """Set the RGB value and optionally brightness of all pixels
        If a brightness value is not supplied,
        the last value set for each pixel is kept
        :param r: Amount of red: 0 to 255
        :param g: Amount of green: 0 to 255
        :param b: Amount of blue: 0 to 255
        :param brightness: Brightness: 0.0 to 1.0 (default around 0.2)
        """
        for x in range(NUM_PIXELS):
            self.set_pixel(x, r, g, b, brightness)

    def get_pixel(self, x):
        """Get the RGB and brightness value of a specific pixel
        :param x: The horizontal position of the pixel: 0 to 7
        """
        r, g, b, brightness = self.pixels[x]
        brightness = brightness * (1.0 / 255.0)
        return r, g, b, round(brightness, 3)

    def set_pixel(self, x, r, g, b, brightness=None):
        """Set the RGB value, and optionally brightness, of a single pixel
        If you don't supply a brightness value, the last value will be kept.
        :param x: The horizontal position of the pixel: 0 to 7
        :param r: Amount of red: 0 to 255
        :param g: Amount of green: 0 to 255
        :param b: Amount of blue: 0 to 255
        :param brightness: Brightness: 0.0 to 1.0 (default around 0.2)
        """
        if brightness is None:
            brightness = self.pixels[x][3]
        else:
            brightness = int(255.0 * brightness)

        self.pixels[x] = [int(r), int(g), int(b), brightness]

    def set_clear_on_exit(self, value=True):
        """Placeholder for compatability.
        :param value: True or False (default True)
        """
        self.clear_on_exit = value

    def draw(self):
        """Draw the 'LEDs' in the pygame display"""
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:
                print("Exiting...")
                sys.exit()

        y_position = int(PIXEL_BOUNDARY / 2)
        radius = int(PIXEL_BOUNDARY / 3)  # Leave some space around each 'LED'

        for x in range(NUM_PIXELS):
            x_position = int((x * PIXEL_BOUNDARY) + (PIXEL_BOUNDARY / 2))
            color = self.pixels[x]
            pygame.gfxdraw.aacircle(
                self.screen, x_position, y_position, radius, color)
            pygame.gfxdraw.filled_circle(
                self.screen, x_position, y_position, radius, color)


blinktsim = BlinktSim()
