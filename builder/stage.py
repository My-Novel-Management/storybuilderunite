# -*- coding: utf-8 -*-
"""Define data type of stage
"""
## public libs
## local libs
from utils import assertion
## local files
from builder.basedata import BaseData


class Stage(BaseData):
    """The data class of stage.

    Attributes:
        name (str): a stage name.
        note (str): 0. a note.
    """
    def __init__(self, name: str, note: str=""):
        super().__init__(name,
                (assertion.isStr(note),))

    ## property
    @property
    def note(self) -> str:
        return self.data[0]

