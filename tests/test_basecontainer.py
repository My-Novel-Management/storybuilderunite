# -*- coding: utf-8 -*-
"""Test: basecontainer.py
"""
## public libs
import unittest
## local files (test utils)
from testutils import printTestTitle, validatedTestingWithFail
## local files
from builder.basecontainer import BaseContainer
from tests import __BASE_ID__


_FILENAME = "basecontainer.py"


class BaseContainerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        printTestTitle(_FILENAME, "BaseContainer class")

    def setUp(self):
        pass

    def test_attributes(self):
        attrs = ("title", "data", "dataId")
        data = [
                (False, ("test",("a",)),
                    ("test", ("a",), __BASE_ID__ + 1)),
                ]
        def _checkcode(vals, expects):
            tmp = BaseContainer(*vals)
            self.assertIsInstance(tmp, BaseContainer)
            for a,v in zip(attrs, expects):
                with self.subTest(a=a, v=v):
                    self.assertEqual(getattr(tmp, a), v)
        validatedTestingWithFail(self, "class attributes", _checkcode, data)

