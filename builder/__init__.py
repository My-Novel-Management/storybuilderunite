# -*- coding: utf-8 -*-
__VERSION__ = "0.0.1"
__TITLE__ = "StoryBuilder"
__DESC__ = "Tool for building a story"


from enum import Enum, auto


## common values
__PRIORITY_NORMAL__ = 5
__PRIORITY_MAX__ = 10
__PRIORITY_MIN__ = 0

__PREFIX_STAGE__ = "on_"
__PREFIX_DAY__ = "in_"
__PREFIX_TIME__ = "at_"
__PREFIX_WORD__ = "w_"


## enums
class ActType(Enum):
    ACT = auto() # basic action
    BE = auto() # put object in scene
    DESTROY = auto() # vanish object
    WEAR = auto() # put on object
    MOVE = auto() # moving object
    HEAR = auto() # sound effect
    LOOK = auto() # paint object
    COME = MOVE | BE
    GO = MOVE | DESTROY
    TALK = auto() # dialogue
    THINK = auto() # monologue
    TAG = auto() # tag

class TagType(Enum):
    NONE = auto()
    BR = auto() # break line
    COMMENT = auto() # comment
    HR = auto() # horizontal line
    SYMBOL = auto() # symbol mark
    TITLE = auto() # title
