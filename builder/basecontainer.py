# -*- coding: utf-8 -*-
"""Define base container.
"""
## public libs
## local libs
from utils import assertion
from utils.util_id import UtilityID
## local files
from . import __PRIORITY_MIN__, __PRIORITY_NORMAL__


class BaseContainer(object):
    """Base class for a container.
    """
    def __init__(self, title: str, data: tuple, omit: bool=False):
        self._data = assertion.isTuple(data)
        self._dataId = UtilityID.getNextId()
        self._priority = __PRIORITY_MIN__ if omit else __PRIORITY_NORMAL__
        self._title = assertion.isStr(title)

    ## property
    @property
    def data(self) -> tuple:
        return self._data

    @property
    def dataId(self) -> int:
        return self._dataId

    @property
    def priority(self) -> int:
        return self._priority

    @property
    def title(self) -> str:
        return self._title
