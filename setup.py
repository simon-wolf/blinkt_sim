from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='blinkt-sim',
    version='1.0.0',
    description='Simulates Pimoroni\'s Blinkt! using pygame.',
    long_description=long_description,
    url='https://github.com/ottersoftware/blinkt_sim',
    author='Simon Wolf',
    author_email='simon@ottersoftware.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: System :: Emulators',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='pimoroni blinkt',
    python_requires='>=3',
    install_requires=[
        'pygame',
    ],
    py_modules=['blinkt_sim'],
    packages=find_packages(where='blinkt_sim'),
    package_dir={'': 'blinkt_sim'},
)
