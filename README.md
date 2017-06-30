# Blinkt! Simulator

Simulates [Pimoroni's Blinkt!](https://shop.pimoroni.com/products/blinkt) using pygame.

## Usage

If you want your code to run on your computer as well as your Pi, do something like this (make sure you `pip install pygame` first):

```python
try:
    import blinkt
    print("Blinkt! detected")
except ImportError:
    from blinkt_sim import blinktsim as blinkt
    print("Using Blinkt! simulator")
```

## Credits

Thanks to [Jannis Hermanns](https://github.com/jayniz) for creating the [unicorn-hat-sim](https://github.com/jayniz/unicorn-hat-sim) which was the inspiration for this (and basis for some of the code).
