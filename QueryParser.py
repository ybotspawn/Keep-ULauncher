import gkeepapi

class QueryParser:
    def __init__(self):
        pass
    def parse(self, stanza):

        # if stanza starts with a color or pinned
        #   optional
        # if stanza starts with title (DESC:)
        #   while true
        #   peek next stanza until hit another token
        # if stanza starts with text (TEXT:)
        #   while true
        #   peek next stanza until hit another token
        pass
    def match_optional(self, stanza):
        pass
    def match_mandatory(self, stanza):
        pass

class Mandatory:
    self.titlePhrase = None
    self.optionalPhrase = None
    self.textPhrase = None

class TitlePhrase:
    pass

class TextPhrase:
    pass

class Optional:
    self.leftOptional = None
    self.rightOptional = None
    self.color = None
    self.pinned = None

class Color:
    self.color = gkeepapi._node.ColorValue.White

class Pinned:
    self.pinned = True
