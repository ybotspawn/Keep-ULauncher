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
    mandatoryPhrase = None
    optionalPhrase = None

class Mandatory:
    titlePhrase = None
    textPhrase = None

class Optional:
    color = gkeepapi._node.ColorValue.White
    pinned = False

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