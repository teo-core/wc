import unittest
import wc

class Testwc(unittest.TestCase):
    def test_existe_wc(self):
        w = wc.Wc()
        self.assertIsNotNone(w)
