from setuptools import find_packages, setup


def requires():
    deps = []
    with open('requirements.txt', 'r') as fil:
        for line in fil.readlines():
            deps.append(line.rstrip())
    return deps


setup(
    name='pywqp',
    version='0.1.5',
    description='Interface to the Water Quality Portal',
    long_description=open('README.md').read(),
    license='Public Domain',
    maintainer='William Blondeau',
    maintainer_email='wblondeau@usgs.gov',
    py_modules=['pywqp'],
    packages=find_packages(),
    install_requires=requires(),
    url='https://github.com/wblondeau-usgs/pywqp',
    test_suite='tests',
)
