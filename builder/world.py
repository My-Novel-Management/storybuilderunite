# -*- coding: utf-8 -*-
"""Define class that world management.
"""
## public libs

## local files (utility)
from utils import assertion
from utils.utildict import UtilityDict
## local files
from builder import __PREFIX_DAY__, __PREFIX_STAGE__, __PREFIX_TIME__, __PREFIX_WORD__
from builder.block import Block
from builder.buildtool import Build
from builder.chapter import Chapter
from builder.day import Day
from builder.episode import Episode
from builder.item import Item
from builder.layer import Layer
from builder.person import Person
from builder.rubi import Rubi
from builder.scene import Scene
from builder.stage import Stage
from builder.story import Story
from builder.time import Time
from builder.word import Word


class World(UtilityDict):
    """Story builder world class.
    """
    def __init__(self, title: str):
        self._title = assertion.isStr(title)
        self._rubis = {}
        self._layers = {}
        self._blocks = {}

    ## property
    @property
    def rubis(self) -> dict:
        return self._rubis

    @property
    def layers(self) -> dict:
        return self._layers

    @property
    def blocks(self) -> dict:
        return self._blocks

    @property
    def title(self) -> str:
        return self._title

    ## methods (build)
    def buildDB(self, persons: list, stages: list, items: list,
            days: list, times: list, words: list,
            rubis: list, layers: list) -> bool:
        '''Build database
        '''
        self.setPersons(persons)
        self.setStages(stages)
        self.setItems(items)
        self.setDays(days)
        self.setTimes(times)
        self.setWords(words)
        self.setRubis(rubis)
        self.setLayers(layers)
        return True

    def buildStory(self, *args: (Chapter, Episode)) -> bool:
        '''Build story object and Output creation
        '''
        builder = Build()
        builder.compile(self.title, *args)
        return True

    def entryBlock(self, *args: Block) -> bool:
        '''Entry to block database
        '''
        for v in args:
            self._blocks[v.title] = v
        return True

    def setPersons(self, persons: list):
        for v in persons:
            self.__setitem__(v[0], Person(*v[1:]))
        return self

    def setStages(self, stages: list):
        for v in stages:
            self.__setitem__(__PREFIX_STAGE__ + v[0], Stage(*v[1:]))
        return self

    def setItems(self, items: list):
        for v in items:
            self.__setitem__(v[0], Item(*v[1:]))
        return self

    def setDays(self, days: list):
        for v in days:
            self.__setitem__(__PREFIX_DAY__ + v[0], Day(*v[1:]))
        return self

    def setTimes(self, times: list):
        for v in times:
            self.__setitem__(__PREFIX_TIME__ + v[0], Time(*v[1:]))
        return self

    def setWords(self, words: list):
        for v in words:
            self.__setitem__(__PREFIX_WORD__ + v[0], Word(*v[1:]))
        return self

    def setRubis(self, rubis: list):
        for v in rubis:
            self._rubis[v[0]] = Rubi(*v)
        return self

    def setLayers(self, layers: list):
        for v in layers:
            self._layers[v[0]] = Layer(*v[1:])
        return self

    ## methods (scenes)
    def block(self, title: str, *args, **kwargs) -> Block:
        '''Create a block
        '''
        return Block(title, *args, **kwargs)

    def chapter(self, title: str, *args, **kwargs) -> Chapter:
        '''Create a chapter
        '''
        return Chapter(title, *args, **kwargs)

    def episode(self, title: str, *args, **kwargs) -> Episode:
        '''Create a episode
        '''
        return Episode(title, *args, **kwargs)

    def load(self, key: str) -> Block:
        '''Load entried block
        '''
        return assertion.hasKey(key, self.blocks)

    def scene(self, title: str, *args, **kwargs) -> Scene:
        '''Create a scene
        '''
        return Scene(title, *args, **kwargs)
