=================
Blinkt! Simulator
=================

Simulates `Pimoroni's Blinkt!`_ allowing Blinkt! code to developed and tested on any computer.

Usage
-----

::

    try:
        import blinkt
    except ImportError:
        import blinkt_sim as blinkt

Example Application
-------------------

::

    import time
    import sys

    try:
        import blinkt
        print("Blinkt! detected")
    except ImportError:
        from blinkt_sim import blinkt_sim as blinkt
        print("Using Blinkt! simulator")

    print("Press Ctrl+C to exit")

    try:
        while True:
            for i in range(8):
                blinkt.clear()
                blinkt.set_pixel(i, 255, 0, 0, 0.75)
                blinkt.show()
                time.sleep(0.1)

    except KeyboardInterrupt:  # Handle Ctrl+C gracefully
        sys.exit()

Credits
-------

Thanks to `Jannis Hermanns`_ for creating the unicorn-hat-sim_ which was the inspiration for this project.

.. _`Pimoroni's Blinkt!`: https://shop.pimoroni.com/products/blinkt
.. _`Jannis Hermanns`: https://github.com/jayniz
.. _unicorn-hat-sim: https://github.com/jayniz/unicorn-hat-sim