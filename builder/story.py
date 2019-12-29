# -*- coding: utf-8 -*-
"""Define chapter container.
"""
## public libs
from __future__ import annotations
from typing import Tuple
## local libs
from utils import assertion
from utils import util_tools as util
## local files
from builder import __PRIORITY_NORMAL__
from builder.basecontainer import BaseContainer
from builder.chapter import Chapter


## define types


class Story(BaseContainer):
    """The container class for chapters.
    """
    def __init__(self, title: str, *args: Chapter, note: str="", priority: int=__PRIORITY_NORMAL__, omit: bool=False):
        super().__init__(title,
                (assertion.isTuple(util.tupleFiltered(args, Chapter)),
                    assertion.isStr(note),
                    ), priority=priority, omit=omit)

    ## property
    @property
    def chapters(self) -> Tuple[Chapter]:
        return self.data[0]

    @property
    def note(self) -> str:
        return self.data[1]

    ## methods
    def inherited(self, *args: Chapter, title: str="") -> Story:
        return Story(title if title else self.title,
                *args,
                note=self.note,
                priority=self.priority)
