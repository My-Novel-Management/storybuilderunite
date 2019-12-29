# -*- coding: utf-8 -*-
"""Define tool for check
"""
## public libs
## local libs
from utils import assertion
from utils.util_tools import toSomething
## local files
from builder import ActType, TagType
from builder.action import Action
from builder.chapter import Chapter
from builder.episode import Episode
from builder.scene import Scene
from builder.shot import Shot
from builder.story import Story


## define types
StoryLike = (Story, Chapter, Episode, Scene)


class Checker(object):
    """The tool class for check
    """
    def __init__(self, src: StoryLike):
        self._src = assertion.isInstance(src, StoryLike)

    ## property
    @property
    def src(self) -> StoryLike:
        return self._src

    ## methods
    def objectInOut(self, src: StoryLike=None) -> bool:
        return toSomething(self,
                storyFnc=_objectInOutIn,
                chapterFnc=_objectInOutInChapter,
                episodeFnc=_objectInOutInEpisode,
                sceneFnc=_objectInOutInScene,
                src=src if src else self.src)


## privates
''' check object in-out
'''
def _objectInOutIn(story: Story) -> bool:
    return not len([v for v in story.chapters if not _objectInOutInChapter(v)]) > 0

def _objectInOutInChapter(chapter: Chapter) -> bool:
    return not len([v for v in chapter.episodes if not _objectInOutInEpisode(v)]) > 0

def _objectInOutInEpisode(episode: Episode) -> bool:
    return not len([v for v in episode.scenes if not _objectInOutInScene(v)]) > 0

def _objectInOutInScene(scene: Scene) -> bool:
    # TODO
    #   itemの管理
    tmp = {}
    msg = []
    isSucceeded = True
    for act in scene.actions:
        if not act.tag_type is TagType.NONE:
            continue
        elif act.act_type is ActType.BE:
            tmp[act.subject.name] = 1
        elif act.act_type is ActType.COME:
            tmp[act.subject.name] = 1
        elif act.act_type is ActType.GO:
            if act.subject.name in tmp:
                tmp[act.subject.name] = 0
            else:
                msg.append(f"Cannot find {act.subject.name}, when GO! in {scene.title}")
                isSucceeded = False
        elif act.act_type is ActType.DESTROY:
            if act.subject.name in tmp:
                tmp[act.subject.name] = 0
            else:
                msg.append(f"Cannot find {act.subject.name}, when DESTROY! in {scene.title}")
                isSucceeded = False
        elif act.act_type in (ActType.TALK, ActType.THINK, ActType.ACT, ActType.WEAR):
            if not act.subject.name in tmp:
                msg.append(f"Cannot find {act.subject.name}, when ACT! in {scene.title}")
                isSucceeded = False
    if not isSucceeded:
        for v in msg:
            print(v)
    return isSucceeded
