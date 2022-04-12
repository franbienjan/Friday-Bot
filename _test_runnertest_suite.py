import unittest
from main import *


class UnitTests(unittest.TestCase):

  def test_keytest(self):
      # Enter code here
      keys = db.keys()
      print(keys)

