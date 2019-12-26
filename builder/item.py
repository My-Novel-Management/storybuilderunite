# -*- coding: utf-8 -*-
"""Define data type of item
"""
## public libs
## local libs
from utils import assertion
## local files
from builder.basedata import BaseData


class Item(BaseData):
    """The data class of item.

    Attributes:
        name (str): a item name
        note (str): 0. a note
    """
    def __init__(self, name: str, note: str=""):
        super().__init__(name,
                (assertion.isStr(note),
                    ))

    ## property
    @property
    def note(self) -> str:
        return self.data[0]
