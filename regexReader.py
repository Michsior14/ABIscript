__author__ = 'lataman'
import schemeContainer, utilities
import re

class regexReader(object):
    def __init__(self, lang):
        self.patternBase = schemeContainer(lang)
