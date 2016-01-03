import imp
import os
import sys
from setuptools import setup, find_packages

SOK = imp.load_source('sok', os.path.join('.', 'sok', 'version.py'))

setup(name='d-ploy',
      version=SOK.__version__,
      description='The Service Orchestration Kit',
      url='https://github.com/TalAntR/sok-core',
      author='Anton Talevnin',
      author_email='talantr@gmail.com',
      packages=find_packages(exclude=['tests*']),
      install_requires=['pyaml>=3.11', 'urllib3>=1.14', 'falcon>=0.3.0'],
      test_suite="tests",
      keywords='service orchestration configuration management',
      platforms="Any"
)
