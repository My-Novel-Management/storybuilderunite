# -*- coding: utf-8 -*-
"""Test: util_str.py
"""
## public libs
import unittest
## local files (test utils)
from testutils import printTestTitle, validatedTestingWithFail
## local files
import utils.util_str as util


_FILENAME = "util_str.py"


class MethodsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        printTestTitle(_FILENAME, "util str methods")

    def setUp(self):
        pass

    def test_strDividedBySplitter(self):
        data = [
                (False, "tes,t", ",",
                    ("tes","t")),
                ]
        validatedTestingWithFail(self, "strDividedBySplitter",
                lambda v, sp, expect: self.assertEqual(
                    util.strDividedBySplitter(v, sp), expect), data)

    def test_dictFromStrBySplitter(self):
        data = [
                (False, "ta:Taro:ha:Hana", ":",
                    {"ta":"Taro","ha":"Hana"}),
                ]
        validatedTestingWithFail(self, "dictFromStrBySplitter",
                lambda v, sp, expect: self.assertEqual(
                    util.dictFromStrBySplitter(v, sp), expect), data)
