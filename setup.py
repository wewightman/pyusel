from setuptools import setup

with open("README.md", 'r') as f:
    readme = f.read()

# run setup tools
setup(
    name="pyusel",
    description="Ultrasound Elasticity Imaging Toolkit",
    author="Wren Wightman",
    author_email="wew12@duke.edu",
    long_description=readme,
    packages=[
        "pyusel",
        "pyusel.data",
        "pyusel.pycbf",
        "pyusel.cinpy",
        "pyusel.interp",
        "pyusel.pyrho",
        "pyusel.dispest"
    ],
    install_requires=[
        "numpy",
        "scipy",
        "mat73"
        ],
    version="0.0.0"
)