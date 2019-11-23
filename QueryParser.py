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
        components = stanza.split()
        self.query = Query()
        for component in components:
            print(component)
            if (match_optional(component)): # if stanza starts with a color or pinned --- match_optional
                #   optional
                
                pass
        
        
        # if stanza starts with title (DESC:)
        #   while true
        #   peek next stanza until hit another token
        # if stanza starts with text (TEXT:)
        #   while true
        #   peek next stanza until hit another token
    def build_append_optional(self, component):
        pass
    def match_optional(self, component):
        if (True):
            return True
        pass
    def match_mandatory(self, component):
        pass

class Query:
    self.mandatoryPhrase = None
    self.optionalPhrase = None

class Mandatory:
    self.titlePhrase = None
    self.textPhrase = None

class TitlePhrase:
    self.title = None

class TextPhrase:
    self.text = None

class Optional:
    self.color = None
    self.pinned = None

class Color:
    self.color = gkeepapi._node.ColorValue.White

class Pinned:
    self.pinned = True
