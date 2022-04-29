from setuptools import find_packages, setup

setup(
    name='datastructures',
    packages=find_packages(include=['datastructures']),
    version='0.1.0',
    description='Python library for Data Structures',
    author='Me',
    license='BHARADWAJS',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests'
)