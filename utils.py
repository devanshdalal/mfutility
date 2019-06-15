#!/usr/bin/env python

def RemoveSpaces(l):
    if len(l)>0 and isinstance(l[0], list):
        return map(lambda x: filter(lambda y: not y.isspace(), x), l)
    else:
        return filter(lambda y: not y.isspace(), l)