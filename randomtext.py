# -*- coding: utf-8 -*-
import re
from random import choice

def randword(match):
    pattern = match.group(1) if not isinstance(match, unicode) else match
    if '(' in pattern:
        return randword(re.sub(r"\((.*?)\)", randword, pattern))
    elif '|' in pattern:
        return choice(pattern.split("|"))
    else:
        return "(" + pattern + ")"


def generate(pattern, data={}):
    """
    Simple random text generator.
    Text should be passed with following syntax:
    (Text|Script|Data|Information) of {key} is (power|nothing)
    Where (...|) is list of words separated by '|' sybmol.
    Where {key} is key of element in data dict.
    """
    while True:
        pattern, n = re.subn(r"\((.*)\)", randword, pattern)
        if not n: break
    return re.sub(r"\{(.*?)\}", lambda(match): data[match.group(1)] if match.group(1) in data else '', pattern)