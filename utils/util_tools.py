# -*- coding: utf-8 -*-
"""Define utility for general.
"""
## public libs
## local libs
from utils import assertion


## public methods
def tupleFiltered(origin: (list, tuple), filter_type: (object, tuple)) -> tuple:
    return tuple(v for v in origin if isinstance(v, filter_type))

def tupleEvenStr(val: (str, list, tuple)) -> tuple:
    if isinstance(val, str):
        return (val,)
    else:
        return tuple(assertion.isList(val))
