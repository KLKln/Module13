import unittest
from unit1.number_guessing_game import NumberGuesser as ng


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.ng = ng(3)

    def tearDown(self):
        del self.ng

    def test_constructor(self):
        ng1 = ng(3)
        #assert ng1.random_number == 3
        #assert ng1.number_of_guesses == 1
        assert ng1.guessed_list == 3
        #assert ng1.guess == 1


if __name__ == '__main__':
    unittest.main()
