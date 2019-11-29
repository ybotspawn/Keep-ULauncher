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
    color = None
    pinned = None

class Parser:
    k = KeepSentence()
    k.mandatoryPhrase = Mandatory()
    k.optionalPhrase = Optional()
    pSections = None

    def __init__(self, phrase):      
        self.pSections = self.reverse(phrase).strip().split(' ')
        self.parseKeepSentence()
    
    def reverse(self, phrase): # convert to a new array rather than a string that in turn gets turned back into an array?
        self.pSections = phrase.split(' ')
        reversed = ""
        while (len(self.pSections)>0):
            reversed = reversed + " " + self.pSections.pop()
        return reversed

    def parseKeepSentence(self): #### MAKE THESE CALL EACH OTGHER
        self.optionalParse()#"DESC: Test Title TEXT: The yellow bird meets the red bee BLUE TRUE")
        self.mandatoryParse()
        if (len(self.pSections) >0):
            self.optionalParse()

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
        while (currentWord != "BLUE" and currentWord != "TRUE" and currentWord != "DESC:" and currentWord != "TEXT:"):
            subPhrase = subPhrase + " " + currentWord
            if ( len(self.pSections) >0 ):
                currentWord= self.pSections.pop()
            else:
                break
        self.pSections.append(currentWord)
        return subPhrase.strip()

    def buildOptionalElement(self, element):
        if (element == "BLUE"):
            self.k.optionalPhrase.color = gkeepapi._node.ColorValue.Blue
        else:
            self.k.optionalPhrase.pinned = True # should we only allow PINNED??? thus no false will be accepted as an argument?

    def optionalParse(self):
        currentWord = self.pSections.pop()
        while (currentWord == "BLUE" or currentWord == "TRUE"): # using BLUE and PINNED right now
            self.buildOptionalElement(currentWord)
            if ( len(self.pSections) >0 ):
                currentWord= self.pSections.pop()
            else:
                break
        if (len(self.pSections) > 0):
            self.pSections.append(currentWord)



phrase = "BLUE DESC: Test Title TRUE TEXT: The yellow bird meets the red bee"
# optional mandatory optional mandatory
parser = Parser(phrase)


print(parser.k.mandatoryPhrase.titlePhrase)
print(parser.k.mandatoryPhrase.textPhrase)
print(parser.k.optionalPhrase.pinned)
print(parser.k.optionalPhrase.color)