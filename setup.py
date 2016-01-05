import importlib.machinery
import os
from setuptools import setup, find_packages

SOK = importlib.machinery.SourceFileLoader('sok', os.path.join('.', 'sok', 'version.py')).load_module()

setup(name='sok-core',
      version=SOK.__version__,
      description='The Service Orchestration Kit',
      url='https://github.com/TalAntR/sok-core',
      author='Anton Talevnin',
      author_email='talantr@gmail.com',
      packages=find_packages(exclude=['tests*']),
      install_requires=['pyaml>=3.11', 'requests>=2.9.1', 'falcon>=0.3.0'],
      test_suite='tests.everything',
      keywords='service orchestration configuration management',
      platforms="Any"
)
