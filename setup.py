from setuptools import setup

VERSION = "0.1.0"

setup(
    name="fletSDP",
    version=VERSION,
    description="Flet Software Development Pattern -Design Patterns for Flet Software Development",
    url="https://github.com/ipritom/fletSDP",
    author='Pritom Mojumder',
    author_email='pritom.blue2@gmail.com',
    license='MIT',
    packages=['fletSDP'],
    install_requires=[
        "flet>=0.7.2",
    ],
    python_requires='>=3.9',
    zip_safe=False
)