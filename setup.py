#coding: utf8

"""
Setup script for corrstats.
"""

try:
    from distutils.core import setup
except ImportError:
    from setuptools import setup


setup(name='corrstats',
      version='0.0.1',
      author="TJ Lane, Jonas Sellberg, Derek Mendez",
      author_email="tjlane@stanford.edu",
      description='Correlation statistics calculator and X-ray intensity modifier',
      packages=["correlation_notes"],
      package_dir={"correlation_notes": "source"})
