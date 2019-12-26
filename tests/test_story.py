# -*- coding: utf-8 -*-
"""Test: story.py
"""
## public libs
import unittest
## local files (test utils)
from testutils import printTestTitle, validatedTestingWithFail
## local files
from builder.chapter import Chapter
from builder.episode import Episode
from builder.story import Story


_FILENAME = "chapter.py"


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        printTestTitle(_FILENAME, "Story class")

    def setUp(self):
        pass

    def test_attributes(self):
        attrs = ("src", "note")
        ch1 = Chapter("melon")
        ch2 = Chapter("lemon")
        ep1 = Episode("apple")
        ep2 = Episode("orange")
        data = [
                (False, "test", (ch1, ch2), "a test",
                    ((ch1, ch2), "a test")),
                (False, "test", (ep1, ep2), "a test",
                    ((ep1, ep2), "a test")),
                ]
        def _checkcode(title, vals, note, expects):
            tmp = Story(title, *vals, note=note)
            self.assertIsInstance(tmp, Story)
            for a,v in zip(attrs, expects):
                with self.subTest(a=a, v=v):
                    self.assertEqual(getattr(tmp, a), v)
        validatedTestingWithFail(self, "class attributes", _checkcode, data)
