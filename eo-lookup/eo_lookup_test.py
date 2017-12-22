import unittest

from eo_lookup import Lookup

TEST_CONTENT = {
    'sano': ['health'],
    'alto': ['altitude', 'height'],
    'tre': ['very'],
    'bela': ['beautiful']
}

LOOKUP = Lookup(TEST_CONTENT)


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(LOOKUP.lookup('alto'), [('alto', ['altitude', 'height'])])
        self.assertEqual(LOOKUP.lookup_html('alto'), '<strong>alto</strong>: altitude, height')


if __name__ == '__main__':
    unittest.main()
