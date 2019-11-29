import gkeepapi
import re

TEXT_REGEX = "TEXT:"
TITLE_REGEX = "DESC:"
PINNED_REGEX = "TRUE|FALSE"
COLOR_REGEX = "BLUE|RED|GREEN|BROWN|DARKBLUE|GRAY|ORANGE|PINK|PURPLE|TEAL|WHITE|YELLOW"

class KeepSentence:
    mandatoryPhrase = None
    optionalPhrase = None

class Mandatory:
    titlePhrase = None
    textPhrase = None

class TitlePhrase:
    title = None

class TextPhrase:
    text = None

class Optional:
    color = gkeepapi._node.ColorValue.White
    pinned = False

class Parser:
    k = KeepSentence()
    k.mandatoryPhrase = Mandatory()
    k.optionalPhrase = Optional()
    pSections = None

    def __init__(self, phrase):      
        self.pSections = self.reverse(phrase)
        self.parseKeepSentence()
    
    def reverse(self, phrase): # convert to a new array rather than a string that in turn gets turned back into an array?
        return [word for word in reversed(phrase.split(' '))] 

    def parseKeepSentence(self): 
        self.optionalParse()
        self.mandatoryParse()

    def mandatoryParse(self):
        directive = self.pSections.pop()
        while (directive == "TEXT:" or directive =="DESC:"):
            subPhrase = self.buildSubphrase()
            self.buildMandatoryElement(directive, subPhrase)
            directive = self.pSections.pop()
        if (len(self.pSections) > 0):
            self.pSections.append(directive)
            self.optionalParse()

    def buildMandatoryElement(self, directive, subPhrase):
        if (directive == "DESC:"):
            self.k.mandatoryPhrase.titlePhrase = subPhrase
        else:
            self.k.mandatoryPhrase.textPhrase = subPhrase

    def buildSubphrase(self):
        currentWord = self.pSections.pop()
        subPhrase = ""
        while (not re.match(COLOR_REGEX, currentWord) and currentWord != "TRUE" and currentWord != "DESC:" and currentWord != "TEXT:"):
            subPhrase = subPhrase + " " + currentWord
            if ( len(self.pSections) >0 ):
                currentWord= self.pSections.pop()
            else:
                break
        self.pSections.append(currentWord)
        return subPhrase.strip()

    def buildOptionalElement(self, element):
        if (re.match(COLOR_REGEX, element)):
            self.k.optionalPhrase.color = gkeepapi._node.ColorValue.Blue
        else:
            self.k.optionalPhrase.pinned = True 

    def optionalParse(self):
        currentWord = self.pSections.pop()
        while (re.match(COLOR_REGEX, currentWord) or currentWord == "TRUE"): 
            self.buildOptionalElement(currentWord)
            if ( len(self.pSections) >0 ):
                currentWord= self.pSections.pop()
            else:
                break
        if (len(self.pSections) > 0):
            self.pSections.append(currentWord)