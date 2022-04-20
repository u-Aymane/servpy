from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

with open('README.md', 'r', encoding="utf-8") as fh:
    long_description = fh.read()

VERSION = '1.0.0'
DESCRIPTION = "ServPy is a Python library that allows you to bruteforce and find (ssh, ftp, windows) server in the internet by checking open ports"
# LONG_DESCRIPTION = 'A package that allows get metadata from websites allowing to perfect your targeting.'

# Setting up
setup(
    name="servpy",
    version=VERSION,
    author="Aymane Elhattab",
    author_email="<aymane.elhattab.master@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['python-nmap', 'faker'],
    keywords=['rdp', 'server', 'port-check', 'bruteforce'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)