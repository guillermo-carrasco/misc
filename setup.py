import glob
import os
import sys

from setuptools import setup, find_packages

version = '0.1'

setup(name='misc',
      version=version,
      description="Set of tools and/or scripts for several small tasks",
      long_description="Just a set of unrelated set of tools and utilities",
      keywords='utils python misc tools',
      author='Guillermo Carrasco',
      author_email='guille.ch.88@gmail.com',
      url='http://mussolblog.wordpress.com/',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      scripts = glob.glob('scripts/*'),
      )
