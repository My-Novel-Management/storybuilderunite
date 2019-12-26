# -*- coding: utf-8 -*-
"""Example story
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('builder')
## public libs
## local libs
from builder.drawer import Drawer
from builder.world import World
from builder.writer import Writer
## local files
from config import DAYS, ITEMS, LAYERS, PERSONS, RUBIS, STAGES, TIMES, WORDS

D = Drawer
W = Writer
_ = Writer.getWho()
################################################################
#
# Sample step:
# 1) Create the world
#       世界を作成する。
# 2) Create a new chapter
#       章の作成。
# 3) Create a episode
#       エピソード作成。
# 4) Create a new scene
#       シーン作成。物語のベース。ここに様々なActionを追加する。
# 5) Create a new stage
#       舞台作成。シーンに必須要素
# 6) Create a new day and time
#       日時作成。シーンのサブ要素
# 7) Add a scene plot
#       シーンプロットの作成。概要のないシーンは原則使えない
# 8) Add scene actions
#       シーンアクションの追加。
#
################################################################


## scenes
def sc_getpeach(w: World):
    granma = W(w.granma)
    peach = W(w.peach)
    return w.scene("大きな桃", "桃を拾う",
            w.load("river"),
            w.load("granma_base"),
            granma.look("hair", "白髪混じりで細い髪質"),
            peach.come(),
            peach.look("size", "人間が二人掛かりで持てそうな大きさ"),
            peach.look("mate", "しっかりと色づき美味しそう"),
            granma.do("pickup", "桃を", D("$Sは流れてきた桃を木の棒で引き寄せると、")),
            _.do("get", D("手を伸ばしてそれを何とか岸に引き上げた"),),
            camera=w.granma,
            stage=w.on_river,
            day=w.in_getpeach, time=w.at_morning,
            )

def sc_birth(w: World):
    return w.scene("誕生", "$taroの誕生秘話",
            w.load("living"),
            stage=w.on_home,
            time=w.at_midmorning,
            )

def sc_known(w: World):
    return w.scene("鬼の悪事を知る", "村人から鬼の悪事を聞く",
            camera=w.taro,
            stage=w.on_vila,
            day=w.in_rumor, time=w.at_afternoon,
            )

def sc_desicion(w: World):
    return w.scene("決意", "鬼退治の決意をする",
            stage=w.on_home,
            time=w.at_night,
            )

def sc_voyage(w: World):
    return w.scene("旅立ち", "旅立つ$taro",
            )

def sc_meetdog(w: World):
    return w.scene("犬と会う", "犬を味方にする",
            )

def sc_meetmonkey(w: World):
    return w.scene("猿と会う", "猿を味方にする",
            )

def sc_meetbird(w: World):
    return w.scene("雉と会う", "雉を味方にする",
            )

def sc_island(w: World):
    return w.scene("鬼ヶ島", "鬼ヶ島で鬼退治をする",
            )

def sc_backhome(w: World):
    return w.scene("村に戻る", "宝物と共に村に戻った",
            )

## episodes
def ep_birth(w: World):
    return w.episode("$taro誕生",
            sc_birth(w),
            sc_known(w),
            sc_desicion(w),
            sc_voyage(w),
            )

def ep_ally(w: World):
    return w.episode("味方を得る",
            sc_meetdog(w),
            sc_meetmonkey(w),
            sc_meetbird(w),
            )

def ep_buster(w: World):
    return w.episode("鬼退治",
            sc_island(w),
            sc_backhome(w),
            )

## persons
def set_persons(w: World):
    taro = W(w.taro)
    granma = W(w.granma)
    return (
        w.block("taro_base",
            taro.wear(w.cloth_momo1),
            ),
        w.block("taro_battle",
            taro.wear(w.cloth_momo2),
            taro.wear(w.katana),
            taro.wear(w.flag),
            ),
        w.block("granma_base",
            granma.wear(w.cloth_boro),
            ),
        )

## stages
def set_stages(w: World):
    floor, ceil, wall = W(w.floor), W(w.ceil), W(w.wall)
    water, tree, land = W(w.water), W(w.tree), W(w.land)
    return (
        w.block("living",
            ceil.be(),
            floor.be(),
            wall.be(),
            ceil.look("質", "梁が露出した寒々としたもの"),
            floor.look("質", "板張りでところどころ穴が空いている粗末なもの"),
            wall.look("質", "漆喰で塗られている"),
            ),
        w.block("river",
            water.be(), land.be(), tree.be(2),
            water.look("mate", "綺麗で透き通っている"),
            ),
        )

## items

## main
def world():
    w = World("桃太郎")
    w.buildDB(PERSONS,
            STAGES, ITEMS, DAYS, TIMES, WORDS,
            RUBIS, LAYERS)
    w.entryBlock(
            *set_persons(w),
            *set_stages(w),
            )
    return w

def main(): # pragma: no cover
    w = world()
    return w.buildStory(
            ep_birth(w),
            ep_ally(w),
            ep_buster(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

