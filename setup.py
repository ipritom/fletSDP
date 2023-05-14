from setuptools import setup
import subprocess


commits = commits = subprocess.check_output(
    ['/usr/bin/git', 'rev-list', 'HEAD', '--count']).decode('utf8').strip()

MAJOR = "0.0"

setup(
    name="fletSDK",
    version=f"{MAJOR}.{commits}",
    description="Flet Software Development Pattern -Design Patterns for Flet Software Development",
    url="https://github.com/ipritom/fletSDP",
    author='Pritom Mojumder',
    author_email='pritom.blue2@gmail.com',
    license='MIT',
    packages=['gonit'],
    install_requires=[
        "flet=>0.7.1",
    ],
    python_requires='>=3.9',
    zip_safe=False
)