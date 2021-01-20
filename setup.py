"""
setup.py for financio
"""

import os

from setuptools import setup, find_packages

from financio import __version__


this_dir = os.path.abspath(os.path.dirname(__file__))


NAME = "Financio Test Utilities"
VERSION = __version__
PACKAGES = find_packages(exclude=["ez_setup"])
DESCRIPTION = "Financio Test Utilities"
URL = "https://github.com/jmmjsolutions/financio-test-utils"
LICENSE = "Apache License Version 2.0"
LONG_DESCRIPTION = open(os.path.join(this_dir, "README.rst")).read()
REQUIREMENTS = [
    _f
    for _f in open(os.path.join(this_dir, "requirements.txt")).read().splitlines()
    if _f
]
AUTHOR = "Mark Rees"
AUTHOR_EMAIL = "mark@jmmjsolutions.com"
KEYWORDS = ("performance", "scalability", "load", "test", "testing", "benchmark")
CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.8",
    "Topic :: Software Development :: Testing",
    "Topic :: Software Development :: Testing :: Traffic Generation",
    "Topic :: System :: Benchmark",
]
CONSOLE_SCRIPTS = [
]


params = dict(
    name=NAME,
    version=VERSION,
    packages=PACKAGES,
    install_requires=REQUIREMENTS,
    # metadata for upload to PyPI
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    keywords=KEYWORDS,
    url=URL,
    classifiers=CLASSIFIERS,
    entry_points={"console_scripts": CONSOLE_SCRIPTS},
)

setup(**params)