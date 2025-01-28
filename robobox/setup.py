from setuptools import setup, find_packages

setup(
    name='robobox',
    version='1.0.0',
    description='Toolbox for robotics applications',
    author='Mowibox',
    license='Apache-2.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'sympy',
        'matplotlib',
    ]
)