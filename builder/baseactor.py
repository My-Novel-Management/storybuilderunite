# -*- coding: utf-8 -*-
"""Define base actor.
"""
## public libs
## local libs
from utils import assertion
from utils.util_id import UtilityID
## local files
from builder.basedata import BaseData


class BaseActor(object):
    """Base class for a data.
    """
    def __init__(self, roll: BaseData):
        self._actId = UtilityID.getNextId()
        self._roll = assertion.isInstance(roll, BaseData)

    @property
    def actId(self) -> int:
        return self._actId

    @property
    def roll(self) -> BaseData:
        return self._roll
