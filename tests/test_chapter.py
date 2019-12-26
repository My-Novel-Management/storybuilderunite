# -*- coding: utf-8 -*-
"""Test: chapter.py
"""
## public libs
import unittest
## local files (test utils)
from testutils import printTestTitle, validatedTestingWithFail
## local files
from builder.chapter import Chapter
from builder.episode import Episode


_FILENAME = "chapter.py"


class ChapterTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        printTestTitle(_FILENAME, "Chapter class")

    def setUp(self):
        pass

    def test_attributes(self):
        attrs = ("episodes", "note")
        ep1 = Episode("apple")
        ep2 = Episode("orange")
        data = [
                (False, "test", (ep1, ep2), "a test",
                    ((ep1, ep2), "a test")),
                ]
        def _checkcode(title, vals, note, expects):
            tmp = Chapter(title, *vals, note=note)
            self.assertIsInstance(tmp, Chapter)
            for a,v in zip(attrs, expects):
                with self.subTest(a=a, v=v):
                    self.assertEqual(getattr(tmp, a), v)
        validatedTestingWithFail(self, "class attributes", _checkcode, data)
