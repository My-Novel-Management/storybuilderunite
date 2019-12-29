# -*- coding: utf-8 -*-
"""Define utility for compare
"""
## public libs
from typing import Tuple
## local libs
## local files
from builder.action import Action
from builder.basecontainer import BaseContainer
from builder.block import Block
from builder.chapter import Chapter
from builder.episode import Episode
from builder.scene import Scene
from builder.story import Story


## methods
def equalsContainers(a: (Story, Chapter, Episode, Scene), b: (Story, Chapter, Episode, Scene)) -> bool:
    return type(a) is type(b) and _equalsBaseContainer(a, b)

def equalsContainerLists(alist: tuple, blist: tuple) -> bool:
    for a,b in zip(alist, blist):
        if not equalsContainers(a, b):
            return False
    return True


## privates
def _equalsBaseContainer(a: BaseContainer, b: BaseContainer) -> bool:
    return a.title == b.title and len(a.data) == len(b.data) and len(a.data[0]) == len(b.data[0]) and a.priority == b.priority
