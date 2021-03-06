#!/usr/bin/env python3
#
# cupp setup
#
# date: Mar 1 2021
# Maintainer: glozanoa <glozanoa@uni.pe>


from setuptools import setup, find_packages
#from ama.core.version import get_version

VERSION = "v0.0.1"

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()


setup(
    name='cupp',
    version=VERSION,
    description='Common User Passwords Profiler',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    maintainer='glozanoa',
    maintainer_email='glozanoa@uni.pe',
    url='https://github.com/fpolit/cupp',
    license='GPL3',
    packages=find_packages(),
    package_data = {
        'cupp': ['cupp.cfg'],
    },
    include_package_data=True,
    entry_points={
        'console_scripts':[
            'cupp = cupp.cupp:main'
        ],
    }
)
