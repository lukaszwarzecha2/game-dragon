import unittest

from main import Dragon

class DragonInitTest(unittest.TestCase):

    def test_init_dragon_failed(self):
        self.assertRaises(TypeError, Dragon)

    def test_init_dragon(self):
        dragon = Dragon("Wawelski")
        self.assertEqual(dragon.name, 'Wawelski')