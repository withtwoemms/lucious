from unittest import TestCase
from lucious.utils import class_properties


class UtilsTest(TestCase):

    def test_class_properties(self):
        class Type:
            def __init__(self, a, b):
                self.a = a
                self.b = b
        result = class_properties(Type('a', 'b'))
        self.assertDictEqual(
            dict(result),
            {'a': 'a', 'b': 'b'}
        )
