# -*- coding: utf-8 -*-
"""Define action container.
"""
## public libs
from typing import Optional, Tuple
## local libs
from utils import assertion
from utils import util_tools as util
## local files
from builder.action import Action
from builder.basecontainer import BaseContainer
from builder.day import Day
from builder.person import Person
from builder.stage import Stage
from builder.time import Time
from builder.when import When
from builder.where import Where
from builder.who import Who

## define types
PersonLike = (Person, Who)
StageLike = (Stage, Where)
DayLike = (Day, When)
TimeLike = (Time, When)


class Scene(BaseContainer):
    """The container class for actions.
    """
    def __init__(self, title: str, *args: Action,
            camera: Optional[Person]=None,
            stage: Optional[Stage]=None,
            day: Optional[Day]=None,
            time: Optional[Time]=None,
            note: str="", omit: bool=False):
        super().__init__(title,
                (assertion.isTuple(util.tupleFiltered(args, Action)),
                    assertion.isInstance(camera, PersonLike) if camera else Who(),
                    assertion.isInstance(stage, StageLike) if stage else Where(),
                    assertion.isInstance(day, DayLike) if day else When(),
                    assertion.isInstance(time, TimeLike) if time else When(),
                    assertion.isStr(note),
                ), omit=omit)

    ## property
    @property
    def actions(self) -> Tuple[Action, ...]:
        return self.data[0]

    @property
    def camera(self) -> PersonLike:
        return self.data[1]

    @property
    def stage(self) -> StageLike:
        return self.data[2]

    @property
    def day(self) -> DayLike:
        return self.data[3]

    @property
    def time(self) -> TimeLike:
        return self.data[4]

    @property
    def note(self) -> str:
        return self.data[5]

