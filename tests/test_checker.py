import unittest
from unittest.mock import *
from  sample.checker import Checker

class TestChecker(unittest.TestCase):

    def setUp(self):
        self.temp = Checker()

    def test_checker_before(self):
        file = 'file.wav'
        #prepare mock
        self.temp.temp.getTime = Mock(name = 'getTime')
        self.temp.temp.getTime.return_value = 10
        self.temp.temp.resetWav = Mock(name = 'resetWav')
        self.temp.temp.resetWav.return_value = False
        #testing
        result = self.temp.remainder(file)
        self.assertEqual(result, False)

    def test_checker_after(self):
        file = 'file.wav'
        # prepare mock
        self.temp.temp.getTime = Mock(name = 'getTime')
        self.temp.temp.getTime.return_value = 20
        self.temp.temp.wavWasPlayed = Mock(name = 'wavWasPlayed')
        self.temp.temp.wavWasPlayed.return_value = True

        # testing
        result = self.temp.remainder(file)
        self.assertEqual(result, True)

    def tearDown(self):
        self.temp = None