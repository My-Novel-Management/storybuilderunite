# -*- coding: utf-8 -*-
"""Example story
"""
## path setting
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('builder')
## public libs
## local libs
from builder.world import World
from builder.writer import Writer
## local files
from assets import basic, accessory
from config import AREAS, DAYS, ITEMS, LAYERS, PERSONS, RUBIS, STAGES, TIMES, WORDS


W = Writer
_ = Writer.getWho()
d = Writer.continuedAct

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
# NOTE:
#   create each scenes
def sc_get_peach(w: World):
    gma = W(w.granma)
    return w.scene("桃を拾う",
            w.comment("序盤。おばあさんが桃を拾う"),
            w.eventStart("桃太郎誕生"),
            gma.be("あるところにおじいさんとおばあさんがいました", "&"),
            gma.explain("おじいさんは山へ芝刈りに、おばあさんは川へ洗濯に出かけました"),
            gma.wear("渋染の着物にほつれた草履", "ぼさぼさの白髪"),
            gma.wear("目は小豆のよう"),
            gma.wear("肌はシミが目立つ"),
            gma.come("洗濯物を籠に入れ、河原にやってきた$Sでしたが、", "&"),
            gma.do("川の上流からどんぶらこと大きな桃が流れてくるのを見つけました。それを見て思います"),
            d("じっと立って桃を見つめて"),
            gma.talk("あれまあ、なんて大きな桃なんでしょう"),
            d("おじいさんが好きそうだ"),
            gma.think("拾って帰って、おじいさんと一緒に食べようかしらね", "#桃をゲット"),
            gma.have(w.peach, "そう考え、何とか木の棒を使ってこちらに引き寄せ、ひと抱えもある桃を手に入れました"),
            gma.go("それを籠に入れ、家に帰りました"),
            camera=w.granma,
            area=w.Vila,
            stage=w.on_river,
            day=w.in_birth, time=w.at_midmorning,
            )

def sc_birth_taro(w: World):
    gma, gpa = W(w.granma), W(w.granpa)
    taro = W(w.taro)
    return w.scene("誕生",
            w.br(),
            gma.be("#居間に座っていた"),
            gpa.be(),
            gma.talk("おじいさん見ておくれよ、この大きな桃"),
            gpa.talk("ありゃまあ、なんてぇ大きな桃だよ",
                "早速$meが切ってやろう"),
            gpa.have(w.blade, "ナタを手にした$Sは大きく振り上げると、一気に桃に向かってブスリ、とやりました"),
            taro.be("#$S誕生する", "桃はパカーと真っ二つに割れて、中から玉のような赤子が出てきました"),
            gma.wear("たすき掛け"),
            gma.talk("おじいさん、こりゃあ人の子だ！？　なんてことだ！"),
            _.talk("子どもがいない$meに神様が授けて下さったんだよぉ"),
            gpa.talk("よし！", "$taroと名付けよう",
                "今日からお前は$taroだ"),
            taro.explain("こうして$Sは生まれました"),
            w.eventEnd("桃太郎誕生"),
            stage=w.on_home,
            time=w.at_noon,
            )

def sc_voyage(w: World):
    taro = W(w.taro)
    gma, gpa = W(w.granma), W(w.granpa)
    dango = W(w.dango)
    return w.scene("旅立ち",
            w.symbol("◆"),
            taro.be(),
            taro.explain("$Sはすくすくと育ち、あっという間に大きく逞しく成長しました"),
            taro.do("ある日、村人から鬼の悪行を聞いた$Sは考えました"),
            taro.think("――何とか鬼を退治して村に恩返しがしたい"),
            taro.explain("そこでおじいさんとおばあさんを前にして、鬼退治をしたいと言い出したのです"),
            gma.be(),gpa.be(),
            gma.look("#神妙な顔で座っている"),
            gma.talk("どうしても行くというのかい？"),
            taro.talk("$meの決意は固いです", "何よりここまで育ててくれたあなたたちや村の人たちに恩返しがしたい"),
            gpa.talk("ばあさんや、男の子というのはいつか自分のやることを見つけて旅立つものだ",
                "行かせてやろうじゃないか"),
            gpa.have(w.katana, "そう言うと$Sは$katanaを持ってきて、$taroに渡します"),
            gpa.talk("これをお持ちなさい", "かつて鬼を切ったと言われる名刀だ"),
            taro.talk("こんな大切なものを", "$meは絶対に鬼をやっつけてきます"),
            gma.talk("それじゃあ$meは$dangoでも作ろうかね", w.dango),
            taro.talk("ありがとうございます"),
            gma.do("団子を作って", w.dango),
            taro.have(w.dango, "おばあさんからは$dangoを貰った"),
            dango.look("きな粉がまぶされ、美味しそうだ"),
            taro.explain("こうして$Sは翌朝早くに旅立っていきました"),
            w.eventStart("鬼退治"),
            taro.go(),
            camera=w.taro,
            day=w.in_voyage, time=w.at_morning,
            )

def mo_ally(w: World):
    taro = W(w.taro)
    dog, monkey, bird = W(w.dog), W(w.monkey), W(w.bird)
    return (w.scene("家来1",
            taro.hasThat(w.dango),
            w.load("犬を仲間に"),
            dog.talk("助かりました", "ところで$taroさんはどこに行くのですか？"),
            taro.talk("鬼を退治しに行くところなんだ"),
            dog.talk("それなら$meがお供しましょう", "鬼はこの牙が苦手と言います"),
            _.explain("こうして犬は$CSの家来となりました"),
            w.eventPoint("鬼退治", "犬を仲間にする"),
            area=w.Land,
            stage=w.on_street,
            day=w.in_voyage.nextDay(),
            time=w.at_afternoon,
            ),
            w.scene("家来2",
            taro.hear("誰かの話しかける声"),
            taro.do("またしばらく歩いていきます。今度は猿が木の上から話しかけます"),
            monkey.be("#木の上に"),
            monkey.talk("おい、なんか美味そうなもん持ってるな"),
            taro.talk("ああ、これか", "おばあさんが作ってくれた$dangoだ"),
            monkey.talk("一つ$meにくれねえか？"),
            taro.talk("いいけれども、ただでという訳にはいかないな"),
            taro.do("$Sが猿を見て渋ると、猿はこう返しました"),
            monkey.talk("それなら何でも一つ言うことを聞いてやろう",
                "$meは力こそないが、知恵はよく働く",
                "悪評高い鬼のやつらにだって知恵比べなら負けはしねえ"),
            taro.talk("それなら$meと一緒に鬼退治に来てくれませんか？"),
            monkey.have(w.dango, "二つ返事で頷くと、$Sは$dangoを貰って一気に口に放り込んだ"),
            taro.explain("こうして犬に続き猿も家来にした$Sだったが、その行く手を阻むように川が横たわっていた"),
            time=w.at_afternoon.elapsedMin(30),
            ),
            w.scene("家来3",
            taro.talk("困ったなあ"),
            bird.come("そこに$Sが優雅に翼を広げてやってくる"),
            bird.talk("おや、噂の$taroさんじゃありませんか", "どうかされましたか？"),
            taro.talk("いや、実は川が渡れずに困っていたんだ"),
            bird.talk("それなら$meが仲間たちを呼んで渡してあげましょう"),
            _.do("そう言うと$Sはピーと鳴き、仲間を沢山集め、$taroたちを向こう岸へと運んでくれた"),
            taro.do("$Sはお礼にと$dangoを渡したが、$birdは鬼退治に行くという話を聞き、一緒に行ってくれることになった"),
            taro.explain("$Sは家来として犬、猿、雉とそれぞれ引き連れ、$on_islandを目指しました"),
            time=w.at_afternoon.elapsedHour(2),
            ),
            w.scene("船で",
                taro.explain("船で$on_islandを目指した"),
                stage=w.on_ship,
            ),
            )

def sc_island(w: World):
    taro = W(w.taro)
    daemon = W(w.daemon)
    return w.scene("$on_island",
            w.comment("$taroは鬼退治をする"),
            taro.existsThat(),
            taro.come("$Sは家来と共に$on_islandへとやってきた"),
            daemon.be("酒とご馳走で祝勝会をしている"),
            taro.talk("やい！", "村の人たちから奪った宝物は返してもらうぞ"),
            daemon.talk("うるさいわ。一体何だというんだ？"),
            taro.talk("$meは$taroだ。お前らを成敗する！"),
            taro.do("$Sは家来と共にその場にいた鬼たちをあっという間に組み伏せた"),
            daemon.talk("参りました。どうか、命だけは……"),
            taro.talk("もうこれ以上村の人に悪さをするんじゃないぞ？", "いいな？"),
            taro.explain("こうして鬼たちから宝物を巻き上げ、村に持ち帰りました"),
            stage=w.on_island_int,
            )

## episodes
# NOTE:
#   create each episodes and set scenes
def ep_birth_momotaro(w: World):
    return w.episode("$taro誕生",
            sc_get_peach(w),
            sc_birth_taro(w),
            note="流れてきた大きな桃には赤子（$taro）が入っていた",
            )

def ep_ally(w: World):
    return w.episode("味方",
            sc_voyage(w),
            *mo_ally(w),
            )

def ep_buster_daemon(w: World):
    return w.episode("$w_daemon退治",
            sc_island(w),
            note="道中で家来を手に入れて、鬼退治する",
            )

## persons
def set_persons(w: World):
    w.setTexture("taro", "黒くて長い髪、すらりと長身")

def life_taro(w: World):
    taro = W(w.taro)
    return w.lifenote("$taroの成長",w.taro,
                taro.do("よく食べてよく眠る子だった"),
                taro.do("朝起きたらいきなり走り回り、畑仕事を手伝う"),
                taro.do("ご飯は三合をぺろりと平らげ、おじいさんおばあさんを驚かせた"),
                )

def hist_taro(w: World):
    return w.createHistories(
            (1, "猪に勝つ"),
            (5, "相撲で負けなし"),
            )

def hist_granma(w: World):
    return w.createHistories(
            ("50:5", "おじいさんと再婚"),
            ("0100-05-05", "最初の結婚をする"),
            (74, "桃太郎を授かる"),
            )

## stages
def set_stages(w: World):
    w.setTexture("on_home", "板張りの床、ところどころ割れている")

## items

## block
def bk_dog(w: World):
    taro, dog = W(w.taro), W(w.dog)
    return w.block("犬を仲間に",
            taro.come("村を出た$Sは街道を歩いていた"),
            dog.be("すると前方で一匹の犬がうずくまっている"),
            taro.talk("どうしたんだ？"),
            dog.talk("お腹が空いて動けないのです"),
            taro.do("そこで$Sは持っていた$dangoを、犬にやった"),
            dog.have(w.dango),
            taro.explain("犬は実に美味しそうにその$dangoを食べていた。",
                "それはそのはずで、村でも一番の美味さだと$taroは思っている。",
                "最初からその魔力に犬が魅せられるのは分かりきっていたのだ"),
            )

## main
def ch_main(w: World):
    # NOTE:
    #   create chapters and set episodes
    return w.chapter("main",
            ep_birth_momotaro(w),
            ep_ally(w),
            ep_buster_daemon(w),
            )

def create_world():
    # NOTE:
    #   create a world. using everywhere
    w = World("桃太郎")
    #   set common data
    w.setCommonData()
    #   set base asset
    w.setAssets(basic.ASSET)
    w.setAssets(accessory.ASSET)
    #   set DB (user)
    w.buildDB(PERSONS,
            AREAS, STAGES, DAYS, TIMES, ITEMS, WORDS,
            RUBIS, LAYERS)
    #   set base year
    w.setBaseDate(113)
    w.setBaseArea("Zero")
    #   set textures
    set_persons(w)
    set_stages(w)
    #   set blocks
    w.entryBlock(bk_dog(w),)
    #   set history
    w.entryHistory(w.taro, *hist_taro(w))
    w.entryHistory(w.granma, *hist_granma(w))
    #   set lifenotes
    w.entryLifeNote(
            life_taro(w),
            )
    #   set outline
    w.setOutline("桃太郎が鬼退治をする")
    return w

def main(): # pragma: no cover
    w = create_world()
    return w.build(
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

