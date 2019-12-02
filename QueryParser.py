import gkeepapi
import re

COLOR_MAPPING = {
    "BLUE": gkeepapi._node.ColorValue.Blue,
    "RED": gkeepapi._node.ColorValue.Red,
    "GREEN": gkeepapi._node.ColorValue.Green,
    "BROWN": gkeepapi._node.ColorValue.Brown,
    "DARKBLUE": gkeepapi._node.ColorValue.DarkBlue,
    "GRAY": gkeepapi._node.ColorValue.Gray,
    "ORANGE": gkeepapi._node.ColorValue.Orange,
    "PINK": gkeepapi._node.ColorValue.Pink,
    "PURPLE": gkeepapi._node.ColorValue.Purple,
    "TEAL": gkeepapi._node.ColorValue.Teal,
    "WHITE": gkeepapi._node.ColorValue.White,
    "YELLOW": gkeepapi._node.ColorValue.Yellow
}

class KeepSentence:
    _mandatoryPhrase = None
    _optionalPhrase = None

    @property
    def mandatoryPhrase(self): 
        return self._mandatoryPhrase 
    @mandatoryPhrase.setter
    def mandatoryPhrase(self, mandatoryPhrase): 
        self._mandatoryPhrase = mandatoryPhrase
    @property
    def optionalPhrase(self): 
        return self._optionalPhrase 
    @optionalPhrase.setter
    def optionalPhrase(self, optionalPhrase): 
        self._optionalPhrase = optionalPhrase

class Mandatory:
    _titlePhrase = None
    _textPhrase = None

    @property
    def titlePhrase(self): 
        return self._titlePhrase 
    @titlePhrase.setter
    def titlePhrase(self, titlePhrase): 
        self._titlePhrase = titlePhrase
    @property
    def textPhrase(self): 
        return self._textPhrase
    @textPhrase.setter
    def textPhrase(self, textPhrase): 
        self._textPhrase = textPhrase

class Optional:
    _color = gkeepapi._node.ColorValue.White
    _pinned = False

    @property
    def pinned(self): 
        return self._pinned 
    @pinned.setter
    def pinned(self, pinned): 
        self._pinned = pinned

    @property
    def color(self): 
        return self._color
    @color.setter
    def color(self, color): 
        self._color = color

class Parser:
    k = KeepSentence()
    k.mandatoryPhrase = Mandatory()
    k.optionalPhrase = Optional()
    pSections = None

    def __init__(self, phrase):      
        self.pSections = [word for word in reversed(phrase.split(' '))] 
        self.optionalParse()
        self.mandatoryParse()

    def mandatoryParse(self):
        directive = self.pSections.pop()
        while (re.match("TEXT|TITLE", directive)):
            subPhrase = self.buildSubphrase()
            self.buildMandatoryElement(directive, subPhrase)
            directive = self.pSections.pop()
        if (len(self.pSections) > 0):
            self.pSections.append(directive)
            self.optionalParse()

    def buildMandatoryElement(self, directive, subPhrase):
        if (directive == "TITLE"):
            self.k.mandatoryPhrase.titlePhrase = subPhrase
        else:
            self.k.mandatoryPhrase.textPhrase = subPhrase

    def buildSubphrase(self):
        currentWord = self.pSections.pop()
        subPhrase = ""
        while (not re.match("|".join(COLOR_MAPPING.keys()), currentWord) and not re.match("TEXT|TITLE|TRUE", currentWord)):
            subPhrase = subPhrase + " " + currentWord
            if ( len(self.pSections) >0 ):
                currentWord= self.pSections.pop()
            else:
                break
        self.pSections.append(currentWord)
        return subPhrase.strip()

    def buildOptionalElement(self, element):
        if (re.match("|".join(COLOR_MAPPING.keys()), element)):
            self.k.optionalPhrase.color = COLOR_MAPPING[element]
        else:
            self.k.optionalPhrase.pinned = True 

    def optionalParse(self):
        currentWord = self.pSections.pop()
        while (re.match("|".join(COLOR_MAPPING.keys()), currentWord) or currentWord == "TRUE"): 
            self.buildOptionalElement(currentWord)
            if ( len(self.pSections) >0 ):
                currentWord= self.pSections.pop()
            else:
                break
        if (len(self.pSections) > 0):
            self.pSections.append(currentWord)