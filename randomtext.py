# -*- coding: utf-8 -*-
import re
from random import choice

def generate(pattern, data={}):
    """
    Simple random text generator.
    Text should be passed with following syntax:
    (Text|Script|Data|Information) of {key} is (power|nothing)
    Where (...|) is list of words separated by '|' sybmol.
    Where {key} is key of element in data dict.
    """
    while True:
        pattern, n = re.subn(r"\(([^()]+)\)", lambda(match): choice(match.group(1).split("|")) 
                             if '|' in match.group(1) else "(" + match.group(1) + ")", pattern)
        if not n: break
    return re.sub(r"\{(.*?)\}", lambda(match): data[match.group(1)] if match.group(1) in data else '', pattern)

print generate(u"((Такое|Сякое (такое|нетакое)!) вот такое|(Пфап|фпфпа))", {})