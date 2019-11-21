import gkeepapi
import re

TEXT_REGEX = "TEXT:"
TITLE_REGEX = "DESC:"
PINNED_REGEX = "TRUE|FALSE"
COLOR_REGEX = "BLUE|RED|GREEN|BROWN|DARKBLUE|GRAY|ORANGE|PINK|PURPLE|TEAL|WHITE|YELLOW"

class QueryParser:
    def __init__(self):
        pass
    def parse(self, stanza):
        # if stanza starts with a color or pinned --- match_optional
        #   optional
        # if stanza starts with title (DESC:)
        #   while true
        #   peek next stanza until hit another token
        # if stanza starts with text (TEXT:)
        #   while true
        #   peek next stanza until hit another token
        pass
    def match_optional(self, stanza):
        if (True):
            return True
        pass
    def match_mandatory(self, stanza):
        pass

class Mandatory:
    self.titlePhrase = None
    self.optionalPhrase = None
    self.textPhrase = None

class TitlePhrase:
    self.title = None

class TextPhrase:
    self.text = None

class Optional:
    self.leftOptional = None
    self.rightOptional = None
    self.color = None
    self.pinned = None

class Color:
    self.color = gkeepapi._node.ColorValue.White

class Pinned:
    self.pinned = True
