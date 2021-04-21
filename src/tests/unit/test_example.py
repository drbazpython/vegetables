import pytest
from django.test import SimpleTestCase

class TestExample(SimpleTestCase):

    def test_example1(self):
        result = "Test Example"
        expected_result = "Test Example"
        assert result == expected_result, 'Should pass this simple test'

