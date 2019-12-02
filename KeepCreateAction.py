import gkeepapi
from ulauncher.api.shared.action.BaseAction import BaseAction
from QueryParser import *

class KeepCreateAction(BaseAction):
    """
    Runs a custom python action
    # Creating a note
    :param User property: Google Note user property for the creation of a new note
    :param Password property: Google Note password property for the creation of a new note
    :param Optional Pinned property: Property toggling the pinning of a note during creation
    :param Optional Title property: Google Note title property for the creation of a new note
    :param Optional Text property: Google Note text property for the creation of a new note
    :param Optional Color property: Google Note color for creating a note
    :param str method: method referenced in customaction
    """

    def __init__(self, username, password, data):
        self.username = username
        self.password = password
        self.parser = Parser(data)

    def run(self):
        self.keep = gkeepapi.Keep()
        self.keep.login(self.username, self.password)
        
        # try:
        note = self.keep.createNote(self.parser.k.mandatoryPhrase.titlePhrase, self.parser.k.mandatoryPhrase.textPhrase)
        note.pinned = self.parser.k.optionalPhrase.pinned
        note.color = self.parser.k.optionalPhrase.color
        # except Exception as error:
        #     raise RuntimeError("Error creating note: %s" % str(error))
        self.keep.sync()