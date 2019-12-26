# -*- coding: utf-8 -*-
"""Define episode container.
"""
## public libs
from typing import Tuple
## local libs
from utils import assertion
from utils import util_tools as util
## local files
from builder.basecontainer import BaseContainer
from builder.episode import Episode


class Chapter(BaseContainer):
    """The container class for episodes.
    """
    def __init__(self, title: str, *args: Episode, note: str="", omit: bool=False):
        super().__init__(title,
                (assertion.isTuple(util.tupleFiltered(args, Episode)),
                    assertion.isStr(note),
                ), omit=omit)

    ## property
    @property
    def episodes(self) -> Tuple[Episode, ...]:
        return self.data[0]

    @property
    def note(self) -> str:
        return self.data[1]
