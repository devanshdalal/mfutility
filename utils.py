#!/usr/bin/env python
import argparse

MC = 'MC'
VRO = 'VRO'

def ParseCmd(argv):
    """Parses the command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--source', nargs='+', choices=[MC, VRO],
        help='The source of scraping')
    parser.add_argument('--clean', help='clean', action='store_true')
    args = parser.parse_args(argv[1:])
    return args

def RemoveSpaces(l):
    if len(l)>0 and isinstance(l[0], list):
        return map(lambda x: filter(lambda y: not y.isspace(), x), l)
    else:
        return filter(lambda y: not y.isspace(), l)
