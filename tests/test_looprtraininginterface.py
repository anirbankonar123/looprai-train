# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from looprai_train.LooprTrainingInterface import get_dataset


class TestLooprTrainingInterface(unittest.TestCase):

    def test_get_dataset(self):
        self.assertEqual(get_dataset("x","y","path"), "For rest")


if __name__ == '__main__':
    unittest.main()
