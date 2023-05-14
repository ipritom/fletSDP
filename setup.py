from setuptools import setup

VERSION = "0.0.1"

setup(
    name="fletSDK",
    version=VERSION,
    description="Flet Software Development Pattern -Design Patterns for Flet Software Development",
    url="https://github.com/ipritom/fletSDP",
    author='Pritom Mojumder',
    author_email='pritom.blue2@gmail.com',
    license='MIT',
    packages=['fletSDP'],
    install_requires=[
        "flet>=0.7.1",
    ],
    python_requires='>=3.9',
    zip_safe=False
)