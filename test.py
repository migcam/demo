import unittest
from fibonacci import dynamic_fibbo

def test_fibbo__low(self):
    expected = 144
    value = 12
    result = dynamic_fibbo(value)
    self.assertEqual(expected, result, "Fibbo pequeño no es igual")

def test_fibbo__big(self):
    expected = 222232244629420445529739893461909967206666939096499764990979600
    value = 300
    result = dynamic_fibbo(value)
    self.assertEqual(expected, result, "Fibbo grande no es igual")
