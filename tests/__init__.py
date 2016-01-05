import os
import unittest

path = os.path.dirname(__file__)
everything = unittest.TestLoader().discover(path)

