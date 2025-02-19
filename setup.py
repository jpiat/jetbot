import glob
import subprocess
from setuptools import setup, find_packages, Extension


def build_libs():
    subprocess.call(['cmake', '.'])
    subprocess.call(['make'])
    

build_libs()


setup(
    name='jetbot',
    version='0.3.0',
    description='An open-source robot based on NVIDIA Jetson Nano',
    packages=find_packages(),
    install_requires=[
        'hoverboard_api',
        'Adafruit-SSD1306',
    ],
    package_data={'jetbot': ['ssd_tensorrt/*.so']},
)
