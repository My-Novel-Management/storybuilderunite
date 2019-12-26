# -*- coding: utf-8 -*-
"""Define actor class for expression
"""
## public libs
## local libs
from utils import assertion
from utils import util_tools as util
## local files
from builder.baseactor import BaseActor
from builder.shot import Shot
from builder.who import Who


class Drawer(BaseActor):
    """The actor class for expression

    Attributes:
        shot (Shot): a shot object
    """
    # TODO: rollをどうするか考える
    def __init__(self, *args: str,
            ):
        super().__init__(Who())
        self._shot = Shot(*args)

    ## property
    @property
    def shot(self) -> Shot:
        return self._shot
