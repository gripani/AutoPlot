from setuptools import setup
from pathlib import Path 

pwd = Path(__file__).parent 
long_description = (pwd / "README.md").read_text()

setup(
    name="AutoPlot",
    version='0.0.1',
    packages=['AutoPlot'],
    author='Giorgio Ripani',
    author_email='g.ripani93@gmail.com',
    long_description=long_description 
    )