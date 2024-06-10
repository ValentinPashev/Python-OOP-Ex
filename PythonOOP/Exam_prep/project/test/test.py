
import unittest

from project import SecondHandCar


class TestSecondHandCar(unittest.TestCase):
    def test_set_promotional_price(self):
        car = SecondHandCar('Toyota', 'Sedan', 200, 10000.0)
        car.set_promotional_price(9000.0)
        self.assertEqual(car.price, 9000.0)

    def test_need_repair(self):
        car = SecondHandCar('Toyota', 'Sedan', 200, 10000.0)
        car.need_repair(500.0, 'Replace brake pads')
        self.assertEqual(car.price, 10500.0)
        self.assertEqual(len(car.repairs), 1)

    def test_price_greater_than_1(self):
        with self.assertRaises(ValueError):
            Car = SecondHandCar('Toyota', 'Sedan', 200, 0.5)

    def test_mileage_greater_than_100(self):
        with self.assertRaises(ValueError) as ex:
            car = SecondHandCar('Toyota', 'Sedan', 50, 10000.0)

    def test_comparison(self):
        car1 = SecondHandCar('Toyota', 'Sedan', 200, 10000.0)
        car2 = SecondHandCar('Honda', 'Sedan', 200, 12000.0)
        self.assertEqual(car1 > car2, False)
        car3 = SecondHandCar('Toyota', 'SUV', 200, 15000.0)
        self.assertEqual(car1 > car3, 'Cars cannot be compared. Type mismatch!')

    def test_str_representation(self):
        car = SecondHandCar('Toyota', 'Sedan', 200, 10000.0)
        self.assertEqual(str(car), "Model Toyota | Type Sedan | Milage 200km\nCurrent price: 10000.00 | Number of Repairs: 0")

if __name__ == '__main__':
    unittest.main()
