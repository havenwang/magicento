"""setup.py: setuptools control."""
 
 
import re
from setuptools import setup
 
 
version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('magicento/magicento.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")
    

setup(
    name = "magicento",
    packages = ["magicento"],
    entry_points = {
        "console_scripts": ['magicento = magicento.magicento:main']
        },
    version = version,
    description = "Python command line application for building and managing.",
    long_description = long_descr,
    author = "Matt Barlow",
    author_email = "mattjbarlow@gmail.com",
    url = "https://github.com/mattjbarlow/magicento",
    )
