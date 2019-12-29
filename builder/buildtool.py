# -*- coding: utf-8 -*-
"""Define tool for build.
"""
## public libs
from collections import Counter as PyCounter
import datetime
import os
## local libs
from utils import assertion
from utils import util_tools as util
## local files
from builder import __BASE_COLUMN__, __BASE_ROW__
from builder import WordClasses
from builder.analyzer import Analyzer
from builder.chapter import Chapter
from builder.checker import Checker
from builder.converter import Converter
from builder.counter import Counter
from builder.datapack import DataPack
from builder.episode import Episode
from builder.extractor import Extractor
from builder.formatter import Formatter
from builder.parser import Parser
from builder.person import Person
from builder.layer import Layer
from builder.story import Story


class Build(object):
    """The tool class for build.
    """
    __BUILD_DIR__ = "build"
    __PERSON_DIR__ = "person"
    __ANALYZE_DIR__ = "analyze"
    __LAYER_DIR__ = "layer"
    __EXTENTION__ = "md"
    def __init__(self, filename: str, extention: str=__EXTENTION__,
            builddir: str=__BUILD_DIR__,
            column: int=__BASE_COLUMN__, row: int=__BASE_ROW__):
        self._builddir = assertion.isStr(builddir)
        self._date = datetime.date.today()
        self._extention = assertion.isStr(extention)
        self._filename = assertion.isStr(filename)
        self._column = assertion.isInt(column)
        self._row = assertion.isInt(row)

    ## property
    @property
    def builddir(self) -> str:
        return self._builddir

    @property
    def date(self) -> datetime.date:
        return self._date

    @property
    def extention(self) -> str:
        return self._extention

    @property
    def filename(self) -> str:
        return self._filename

    @property
    def column(self) -> int:
        return self._column

    @property
    def row(self) -> int:
        return self._row

    ## methods
    def compile(self, title: str, priority: int,
            tags: dict, prefix: str,
            *args) -> Story:
        ''' compile source
            1. serialize (block to actions)
            2. filter by priority
            3. replace pronouns
            4. replace tags
        '''
        tmp = Story(assertion.isStr(title),
                *util.tupleFiltered(args, Chapter))
        cnv = Converter(tmp)
        serialized = cnv.srcSerialized()
        filtered = cnv.srcFilterByPriority(priority, src=serialized)
        replacedP = cnv.srcReplacedPronouns(filtered)
        replacedT = cnv.srcReplacedTags(tags, prefix, replacedP)
        return replacedT

    def output(self, src: Story, rubis: dict, layers: dict,
            stages: dict, daytimes: dict, fashions: dict, foods: dict,
            mecabdir: str,
            formattype: str,
            is_rubi: bool,
            is_scenario: bool, is_analyze: bool,
            is_comment: bool, is_debug: bool) -> bool:
        '''output data
            0. basic info
            1. outline
            2. conte
            3. description (or scenario)
            4. info
                - kanji
                - wordclass
                - stage layer
                - fashion layer
                - food layer
                - time layer
                - custom layers
                - persons
        '''
        analyzer = Analyzer(mecabdir)
        self.toInfoOfGeneral(src, is_debug)
        self.toOutline(src, is_debug)
        self.toConte(src, is_debug)
        if is_scenario:
            self.toScenario(src, is_debug)
        else:
            self.toDescription(src, rubis, is_rubi, is_debug)
        ## informations
        self.toInfoOfKanji(src, is_debug)
        if is_analyze:
            self.toInfoOfWordClass(src, analyzer, is_debug)
        ## layers
        self.toInfoOfStages(src, stages, is_debug)
        self.toInfoOfFashions(src, fashions, is_debug)
        self.toInfoOfFoods(src, foods, is_debug)
        self.toInfoOfTimes(src, daytimes, is_debug)
        self.toInfoOfCustom(src, layers, is_debug)
        self.toInfoOfPersons(src, is_debug)
        ## check
        if is_analyze:
            self.toCheckObjects(src, is_debug)
        return True

    ## methods (output data)
    def toCheckObjects(self, src: Story, is_debug: bool) -> bool:
        # TODO
        #   - Objectの出入り確認
        checker = Checker(src)
        if checker.objectInOut():
            print("OK Object In-Out")
        else:
            raise AssertionError("Object In-Out missed")
        return True

    def toConte(self, src: Story, is_debug: bool) -> bool:
        # TODO
        #   - 各要素の表示形式調整
        title = f"Conte of {src.title}"
        res = Parser(src).toContes()
        return self.outputTo(Formatter.toConte(title, res),
                self.filename, "_cnt", self.extention, self.builddir, is_debug)

    def toDescription(self, src: Story, rubis: dict, is_rubi: bool, is_debug: bool) -> bool:
        # TODO
        #   - format type
        title = f"Text of {src.title}"
        res = Parser(src).toDescriptionsWithRubi(rubis) if is_rubi else Parser(src).toDescriptions()
        return self.outputTo(Formatter.toDescription(title, res),
                self.filename, "", self.extention, self.builddir, is_debug)

    def toInfoOfCustom(self, src: Story, layers: dict, is_debug: bool) -> bool:
        # TODO
        extr = Extractor(src)
        title = f"Custom info of {src.title}"
        res = []
        for k,v in layers.items():
            res.append(DataPack("head", f"{k}:{v.name}"))
            res.extend(extr.descsHasWord(v.words))
        return self.outputTo(Formatter.toLayerInfo(title, res),
                self.filename, "_custom", self.extention,
                os.path.join(self.builddir, self.__LAYER_DIR__), is_debug)

    def toInfoOfFashions(self, src: Story, layers: dict, is_debug: bool) -> bool:
        # TODO
        extr = Extractor(src)
        title = f"Fashion info of {src.title}"
        res = []
        for k,v in layers.items():
            res.append(DataPack("head", f"{k}:{v.name}"))
            res.extend(extr.descsHasWord(v.words))
        return self.outputTo(Formatter.toLayerInfo(title, res),
                self.filename, "_fashion", self.extention,
                os.path.join(self.builddir, self.__LAYER_DIR__), is_debug)

    def toInfoOfFoods(self, src: Story, layers: dict, is_debug: bool) -> bool:
        # TODO
        extr = Extractor(src)
        title = f"Food info of {src.title}"
        res = []
        for k,v in layers.items():
            res.append(DataPack("head", f"{k}:{v.name}"))
            res.extend(extr.descsHasWord(v.words))
        return self.outputTo(Formatter.toLayerInfo(title, res),
                self.filename, "_food", self.extention,
                os.path.join(self.builddir, self.__LAYER_DIR__), is_debug)

    def toInfoOfGeneral(self, src: Story, is_debug: bool) -> bool:
        # TODO
        #   - colum, rowの指定を可能に。ない場合はデフォルト
        #   - 基本情報と詳細情報を分割し、基本は常にコンソールでも
        cnt = Counter(src)
        title = "General Info:"
        res_base = [DataPack("total", cnt.countCharsOfShot()),
                DataPack("manupaper", cnt.countAsManupaperRows(self.column)),
                DataPack("rows", self.row), DataPack("columns", self.column),
                DataPack("chapters", cnt.countChapter()),
                DataPack("episodes", cnt.countEpisode()),
                DataPack("scenes", cnt.countScene()),
                DataPack("actions", cnt.countAction())]
        res_addition = [
                ]
        def _alwaysDisplayOnConsole(infodata, is_debug):
            if not is_debug:
                self.outputToConsole(infodata)
            return infodata
        return self.outputTo(
                _alwaysDisplayOnConsole(Formatter.toGeneralInfo(title, res_base), is_debug),
                self.filename, "_info", self.extention, self.builddir, is_debug)

    def toInfoOfKanji(self, src: Story, is_debug: bool):
        # TODO
        cnt = Counter(src)
        title = f"Kanji info of {src.title}"
        total = cnt.countCharsOfShot()
        kanji = cnt.countKanjiOfShot()
        res = [DataPack("total", total),
                DataPack("kanji", kanji)]
        return self.outputTo(Formatter.toKanjiInfo(title, res),
                self.filename, "_kanji", self.extention,
                os.path.join(self.builddir, self.__ANALYZE_DIR__), is_debug)

    def toInfoOfPersons(self, src: Story, is_debug: bool) -> bool:
        # TODO
        extr = Extractor(src)
        persons = extr.persons
        def _buildLayer(p: Person):
            last, first, full, exfull = Converter.personNamesConstructed(p)
            tmp = Layer(p.name,
                    (p.name, last, first, full, exfull))
            return tmp
        is_succeeded = True
        for p in persons:
            lay = _buildLayer(p)
            title = f"Persons info of {p.name}"
            res = extr.descsHasWord(lay.words)
            is_succeeded = self.outputTo(Formatter.toLayerInfo(title, res),
                p.name, "", self.extention,
                os.path.join(self.builddir, self.__PERSON_DIR__), is_debug)
            if not is_succeeded:
                AssertionError("Person info error!", p)
        return is_succeeded

    def toInfoOfStages(self, src: Story, layers: dict, is_debug: bool) -> bool:
        # TODO
        extr = Extractor(src)
        title = f"Stage info of {src.title}"
        res = []
        for k,v in layers.items():
            res.append(DataPack("head", f"{k}:{v.name}"))
            res.extend(extr.descsHasWord(v.words))
        return self.outputTo(Formatter.toLayerInfo(title, res),
                self.filename, "_stage", self.extention,
                os.path.join(self.builddir, self.__LAYER_DIR__), is_debug)

    def toInfoOfTimes(self, src: Story, layers: dict, is_debug: bool) -> bool:
        # TODO
        extr = Extractor(src)
        title = f"Day Time info of {src.title}"
        res = []
        for k,v in layers.items():
            res.append(DataPack("head", f"{k}:{v.name}"))
            res.extend(extr.descsHasWord(v.words))
        return self.outputTo(Formatter.toLayerInfo(title, res),
                self.filename, "_daytime", self.extention,
                os.path.join(self.builddir, self.__LAYER_DIR__), is_debug)

    def toInfoOfWordClass(self, src: Story, analyzer: Analyzer, is_debug: bool) -> bool:
        # TODO
        title = f"Word class info of {src.title}"
        wcls = analyzer.collectionsWordClassByMecab(src)
        res = []
        def _create(title, name):
            base = PyCounter([v[0] for v in wcls[name]])
            maxnum = base.most_common()[0][1] if base.most_common() else 0
            res.append(DataPack("head", title))
            for i in reversed(range(maxnum)):
                tmp = []
                for w,c in base.most_common():
                    if c == i + 1:
                        tmp.append(w)
                if tmp:
                    res.append(DataPack("count", f"{i + 1}: {','.join(tmp)}"))
        for v in WordClasses:
            _create(v.value, v.name)
        return self.outputTo(Formatter.toWordClassInfo(title, res),
                self.filename, "_wordcls", self.extention,
                os.path.join(self.builddir, self.__ANALYZE_DIR__), is_debug)

    def toOutline(self, src: Story, is_debug: bool) -> bool:
        # TODO
        title = f"Outline of {src.title}"
        res = Parser(src).toOutlines()
        return self.outputTo(Formatter.toOutline(title, res),
                self.filename, "_out", self.extention, self.builddir, is_debug)

    def toScenario(self, src: Story, is_debug: bool) -> bool:
        # TODO
        print("__unimplement scenario mode__")
        return True

    ## methods (output)
    def outputTo(self, data: list, filename: str, suffix: str, extention: str,
            builddir: str, is_debug: bool) -> bool:
        if is_debug:
            return self.outputToConsole(data)
        else:
            return self.outputToFile(data, filename, suffix, extention, builddir)

    def outputToConsole(self, data: list) -> bool:
        for v in data:
            print(v)
        return True

    def outputToFile(self, data: list, filename: str, suffix: str, extention: str,
            builddir: str) -> bool:
        if not os.path.isdir(builddir):
            os.makedirs(builddir)
        fullpath = os.path.join(builddir, "{}{}.{}".format(
            assertion.isStr(filename), assertion.isStr(suffix),
            assertion.isStr(extention)
            ))
        with open(fullpath, 'w') as f:
            for v in data:
                f.write(f"{v}\n")
        return True


        return True

