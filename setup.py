#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.md', 'r') as readme:
    LONG_DESCRIPTION = readme.read()

with open('requirements.txt', 'r') as require:
    REQUIRES = require.read()

setup(
    name='pygdk',
    version='1.0.0.dev1',
    license='MIT',
    # url='',
    description='Python General Development Kit',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=REQUIRES,
    project_urls={
        # "Documentation": "",
        "Issue Tracker": "https://github.com/DevByEagle/pygdk/issues",
        "Source": "https://github.com/DevByEagle/pygdk",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        # "Topic :: Multimedia :: Graphics",
        # "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.10"
)