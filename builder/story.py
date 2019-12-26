# -*- coding: utf-8 -*-
"""Define chapter container.
"""
## public libs
from typing import Tuple
## local libs
from utils import assertion
from utils import util_tools as util
## local files
from builder.basecontainer import BaseContainer
from builder.chapter import Chapter
from builder.episode import Episode


## define types
ChapterLike = (Chapter, Episode)


class Story(BaseContainer):
    """The container class for chapters.
    """
    def __init__(self, title: str, *args: ChapterLike, note: str="", omit: bool=False):
        super().__init__(title,
                (assertion.isTuple(util.tupleFiltered(args, ChapterLike)),
                    assertion.isStr(note),
                    ), omit=omit)

    ## property
    @property
    def src(self) -> ChapterLike:
        return self.data[0]

    @property
    def note(self) -> str:
        return self.data[1]
