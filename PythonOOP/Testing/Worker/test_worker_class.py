from unittest import TestCase, main
from worker import Worker


class TestWorker(TestCase):

    def setUp(self):
        self.worker = Worker("TestGuy",
                             25_000,
                             100)

    def test_correct_init(self):
        self.assertEqual("TestGuy", self.worker.name)
        self.assertEqual(25_000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_if_he_is_working_properly_money_increase_energy_decrease(self):
        expected_money = self.worker.salary * 2
        expected_energy = self.worker.energy - 2

        self.worker.work()
        self.worker.work()

        self.assertEqual(expected_money, self.worker.money)
        self.assertEqual(expected_energy, self.worker.energy)

    def test_if_exception_is_raised_correctly(self):

        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_check_resting_is_it_properly_added(self):
        expected_energy = self.worker.energy + 1

        self.worker.rest()

        self.assertEqual(expected_energy, self.worker.energy)

    def test_check_the_printed_string(self):

        self.assertEqual(f'TestGuy has saved 0 money.', self.worker.get_info())


if __name__ == "__main__":
    main()
