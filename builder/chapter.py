# -*- coding: utf-8 -*-
"""Define episode container.
"""
## public libs
from __future__ import annotations
from typing import Tuple
## local libs
from utils import assertion
from utils.util_str import tupleFiltered
## local files
from builder import __PRIORITY_NORMAL__
from builder.basecontainer import BaseContainer
from builder.episode import Episode


## define class
class Chapter(BaseContainer):
    """The container class for episodes.
    """
    def __init__(self, title: str, *args: Episode,
            note: str="", priority: int=__PRIORITY_NORMAL__):
        super().__init__(title,
                assertion.isTuple(tupleFiltered(args, Episode)),
                note=note,
                priority=priority)

    ## methods
    def inherited(self, *args: Episode, title: str="", note: str=None) -> Chapter:
        return Chapter(title if title else self.title,
                *args,
                note=note if note else self.note,
                priority=self.priority)
