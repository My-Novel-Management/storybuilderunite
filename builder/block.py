# -*- coding: utf-8 -*-
"""Define action container.
"""
## public libs
from typing import Tuple
## local libs
from utils import assertion
from utils import util_tools as util
## local files
from builder.action import Action
from builder.basecontainer import BaseContainer


class Block(BaseContainer):
    """The container class for actions. partial
    """
    def __init__(self, title: str, *args: Action, omit: bool=False):
        super().__init__(title,
                (assertion.isTuple(util.tupleFiltered(args, Action)),
                    ), omit=omit)

    ## property
    @property
    def acts(self) -> Tuple[Action, ...]:
        return self.data[0]
