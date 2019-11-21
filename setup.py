from setuptools import setup, find_packages

setup(
    name="Sagital Average",
    version="0.1.0",
    packages=find_packages(exclude=['*tests']),
    entry_points={
        'console_scripts': [
            'average = sagital_average.command:process'
        ]}
)
