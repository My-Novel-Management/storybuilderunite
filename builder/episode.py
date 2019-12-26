# -*- coding: utf-8 -*-
"""Define scene container.
"""
## public libs
from typing import Tuple
## local libs
from utils import assertion
from utils import util_tools as util
## local files
from builder.basecontainer import BaseContainer
from builder.scene import Scene


class Episode(BaseContainer):
    """The container class for scenes.

    Attributes:
        title (str): a episode title
        scenes (tuple:Scene): 0. scenes
        note (str): 1. a note
    """
    def __init__(self, title: str, *args: Scene, note: str="", omit: bool=False):
        super().__init__(title,
                (assertion.isTuple(util.tupleFiltered(args, Scene)),
                    assertion.isStr(note),
                ), omit=omit)

    ## property
    @property
    def scenes(self) -> Tuple[Scene, ...]:
        return self.data[0]

    @property
    def note(self) -> str:
        return self.data[1]

