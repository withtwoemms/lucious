from os import environ as envvars
from typing import Iterator
from unittest import TestCase
from unittest.mock import PropertyMock
from unittest.mock import patch

from snowflake.connector.cursor import SnowflakeCursor

from lucious.utils import class_properties
from lucious.utils import pad
from lucious.utils import snowflake_cursor


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

    def test_pad(self):
        contents, pad_amount, padding = 'abc', 2, ''
        extension = [padding for _ in range(pad_amount)]

        iterable = list(contents)
        result = pad(iterable, pad_amount, padding)
        self.assertEqual(result, iterable + extension)

        iterator = iter(contents)
        result = pad(iterator, pad_amount, padding)
        self.assertIsInstance(result, Iterator)
        self.assertEqual(list(result), list(iter(contents)) + extension)


    @patch.dict(
        envvars,
        {
            'SNOWFLAKE_ACCOUNT': 'snowflake',
            'SNOWFLAKE_USER': 'user',
            'SNOWFLAKE_PASSWORD': 'password',
            'SNOWFLAKE_ROLE': 'role',
            'SNOWFLAKE_WAREHOUSE': 'warehouse',
        },
        clear=True
    )
    @patch('snowflake.connector.connection.SnowflakeConnection.connect')
    @patch('snowflake.connector.connection.SnowflakeConnection.rest', new_callable=PropertyMock)
    def test_SnowflakeCursor(self, mock_property, mock_connect):
        result = snowflake_cursor(database='database', schema='schema')
        self.assertIsInstance(result, SnowflakeCursor)
