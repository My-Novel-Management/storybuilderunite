# -*- coding: utf-8 -*-
"""Define container for action objects.
"""
## public libs
from typing import Any, Union, Tuple
## local libs
from utils import assertion
from utils import util_tools as util
## local files
from builder import ActType, TagType
from builder.basecontainer import BaseContainer
from builder.day import Day
from builder.item import Item
from builder.person import Person
from builder.shot import Shot
from builder.stage import Stage
from builder.time import Time
from builder.who import Who


## define types
AllSubjects = (Person, Day, Item, Stage, Time, Who)


class Action(BaseContainer):
    """The container class for an action.

    Attributes:
        acts (tuple:Any): actions
        subject (Person): a subject
    """
    __TITLE__ = "__action__"
    def __init__(self, *args: Any, subject: AllSubjects=None,
            act_type: ActType=ActType.ACT,
            tag_type: TagType=TagType.NONE,
            note: str="", omit: bool=False):
        super().__init__(Action.__TITLE__,
                (
                    assertion.isTuple(util.tupleFiltered(args, (str, Shot))),
                    assertion.isInstance(subject, AllSubjects) if subject else Who(),
                    assertion.isInstance(act_type, ActType),
                    assertion.isInstance(tag_type, TagType),
                    assertion.isStr(note),
                ), omit=omit)

    ## property
    @property
    def acts(self) -> Tuple[Union[str, Shot], ...]:
        return self.data[0]

    @property
    def subject(self) -> AllSubjects:
        return self.data[1]

    @property
    def act_type(self) -> ActType:
        return self.data[2]

    @property
    def tag_type(self) -> TagType:
        return self.data[3]

    @property
    def note(self) -> str:
        return self.data[4]
