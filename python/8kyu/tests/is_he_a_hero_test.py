import unittest
import is_he_a_hero


class TestHero(unittest.TestCase):
    def test_is_he_gonna_survive(self):
        TrueHero = is_he_a_hero.hero(10, 5)
        FalseHero = is_he_a_hero.hero(7, 4)
        self.assertEqual(TrueHero, True)
        self.assertEqual(FalseHero, False)
       
