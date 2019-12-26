# -*- coding: utf-8 -*-
"""Define tool for build.
"""
## public libs
## local libs
from utils import assertion
## local files
from builder.chapter import Chapter
from builder.episode import Episode
from builder.story import Story


class Build(object):
    """The tool class for build.
    """
    def __init__(self):
        self._date = "build date" # TODO

    ## property
    @property
    def date(self):
        return self._date

    ## methods
    def compile(self, title: str, *args) -> Story:
        tmp = []
        for v in args:
            if isinstance(v, (Chapter, Episode)):
                tmp.append(v)
        return Story(assertion.isStr(title), *tmp)
