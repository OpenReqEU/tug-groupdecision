# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "application"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Group Decision Service",
    author_email="rsamer@ist.tugraz.at",
    url="",
    keywords=["Swagger", "Group Decision Service"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['application=application.__main__:main']},
    long_description="""\
    This group-based recommendation service accepts and analyzes a set of requirement ratings and individual stakeholder preferences within a requirements project.
    For every requirement, the service detects (rating) conflicts (i.e., conflicts of opinions and rating dissents) and computes a utility value reflecting the appropriateness of the stakeholders for the requirement by considering the relevance of the requirements for the individual stakeholders as well as the availability of these stakeholders.
    The stakeholders with the highest utility values are recommended as potential candidates to be assigned to the requirements.
    """
)

