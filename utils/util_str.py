# -*- coding: utf-8 -*-
"""Define utility for strings.
"""
## public libs
from typing import Tuple
## local libs
from utils import assertion


## public methods
def strDividedBySplitter(val: str, splitter: str) -> Tuple[str, str]:
    return tuple(val.split(splitter)) if assertion.isStr(splitter) in assertion.isStr(val) else (val, val)

def dictFromStrBySplitter(val: (str, dict), splitter: str) -> dict:
    if isinstance(val, dict):
        return target
    elif isinstance(val, str):
        if splitter in val:
            tmp = val.split(splitter)
            return dict([(k,v) for k,v in zip(tmp[0::2], tmp[1::2])])
        else:
            return {}
    else:
        AssertionError("cannot convert dict from str, mismatch type: {type(val)} of {val}")
        return {}

