import unittest


def example(x):
    return x + 1


def raise_exception():
    raise Exception("Whoopsie")


class TestExample(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_example(self):
        self.assertEqual(example(1), 2)

    def test_exception(self):
        self.assertRaises(Exception, raise_exception)

    @unittest.skip("Hello")
    def test_skipped(self):
        self.fail("This should not happen")

    def test_subtests(self):
        for i in range(1, 5):
            with self.subTest(i):
                self.assertGreater(i, 2)


# We can also run the tests like this
if __name__ == "__main__":
    unittest.main()
