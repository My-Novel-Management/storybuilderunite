# -*- coding: utf-8 -*-
"""Define actor class for writing
"""
## public libs
from __future__ import annotations
## local libs
from utils import assertion
## local files
from builder import ActType, TagType
from builder.action import Action
from builder.baseactor import BaseActor
from builder.day import Day
from builder.item import Item
from builder.person import Person
from builder.stage import Stage
from builder.time import Time
from builder.who import Who


## type defines
AllDataType = (Day, Item, Person, Stage, Time, Who)


class Writer(BaseActor):
    """The actor class for writing
    """
    def __init__(self, roll: AllDataType,
            ):
        super().__init__(assertion.isInstance(roll, AllDataType))

    @classmethod
    def getWho(cls) -> Writer:
        return Writer(Who())

    ## act
    def be(self, *args, **kwargs) -> Action:
        return Action(*args, act_type=ActType.BE, **kwargs)

    def come(self, *args, **kwargs) -> Action:
        return Action(*args, act_type=ActType.COME, **kwargs)

    def destroy(self, *args, **kwargs) -> Action:
        return Action(*args, act_type=ActType.DESTROY, **kwargs)

    def go(self, *args, **kwargs) -> Action:
        return Action(*args, act_type=ActType.GO, **kwargs)

    def hear(self, *args, **kwargs) -> Action:
        return Action(*args, act_type=ActType.HEAR, **kwargs)

    def look(self, *args, **kwargs) -> Action:
        return Action(*args, act_type=ActType.LOOK, **kwargs)

    def move(self, *args, **kwargs) -> Action:
        return Action(*args, act_type=ActType.MOVE, **kwargs)

    def talk(self, *args, **kwargs) -> Action:
        return Action(*args, act_type=ActType.TALK, **kwargs)

    def think(self, *args, **kwargs) -> Action:
        return Action(*args, act_type=ActType.THINK, **kwargs)

    def wear(self, *args, **kwargs) -> Action:
        return Action(*args, act_type=ActType.WEAR, **kwargs)

    ## tag
    def br(self, num: (int, str)=1) -> Action:
        return Action(act_type=ActType.TAG, tag_type=TagType.BR, note=str(num))

    def comment(self, comment: str) -> Action:
        return Action(act_type=ActType.TAG, tag_type=TagType.COMMENT, note=comment)

    def hr(self) -> Action:
        return Action(act_type=ActType.TAG, tag_type=TagType.HR)

    def symbol(self, note: str) -> Action:
        return Action(act_type=ActType.TAG, tag_type=TagType.SYMBOL, note=note)

    def title(self, title: str) -> Action:
        return Action(act_type=ActType.TAG, tag_type=TagType.TITLE, note=title)

