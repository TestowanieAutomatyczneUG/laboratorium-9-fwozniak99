import unittest

from unittest.mock import *
from sample.car import Car


class TestCar(unittest.TestCase):

    def test_needs_fuel(self):
        #prepare mock
        car = Car()
        car.needsFuel = Mock(name = 'needsFuel')
        car.needsFuel.return_value = True
        #testing
        self.assertEqual(True, car.needsFuel())


    def test_get_engine_temperature(self):
        #prepare mock
        car = Car()
        car.getEngineTemperature = Mock(name = 'getEngineTemperature')
        car.getEngineTemperature.return_value = 99
        #testing
        self.assertEqual(99, car.getEngineTemperature())


    @patch.object(Car, 'driveTo')
    def test_drive_to(self, mock_method):
        #prepare mock
        destination = 'Bezrobocie'
        mock_method.return_value = 'Heading to ' + destination
        #testing
        car = Car()
        self.assertEqual('Heading to Bezrobocie', car.driveTo(destination))



if __name__ == '__main__':
    unittest.main()
