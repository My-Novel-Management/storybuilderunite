# -*- coding: utf-8 -*-
"""Define data type of shot
"""
## public libs
## local libs
from utils import assertion
from utils import util_tools as util
## local files
from builder.basedata import BaseData


class Shot(BaseData):
    """The data class of shot.

    Attributes:
        infos (tuple): 0. a info
    """
    __NAME__ = "__shot__"
    def __init__(self, *args: str):
        super().__init__(Shot.__NAME__,
                (assertion.isTuple(util.tupleFiltered(args, str)),
                    ))

    ## property
    @property
    def infos(self) -> tuple:
        return self.data[0]
