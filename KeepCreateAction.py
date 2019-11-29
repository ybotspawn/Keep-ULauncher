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
        self.parse_create_note(data)
        
    def keep_app_open(self):
        return False

    # def parse_create_note(self, data):
    #     self.title = data.split(' ')[0]
    #     if len(data.split(' ')) > 1:
    #         self.text = data.replace(self.title, '').strip()
    #     else:
    #         self.text = ""

    #     if not self.title:
    #         self.title = "Placeholder"
    #     if not self.text:
    #         self.text = "Blank"

    def parse_create_note(self, data):
        self.parser = Parser(data)
        self.value = "PCN"
        # self.assertEqual(parser.k.mandatoryPhrase.textPhrase, "The yellow bird meets the red bee")
        # self.assertEqual(parser.k.mandatoryPhrase.titlePhrase, "Test Title")
        # self.assertEqual(parser.k.optionalPhrase.pinned, False)
        # self.assertEqual(parser.k.optionalPhrase.color, gkeepapi._node.ColorValue.Blue)

    def run(self):
        self.keep = gkeepapi.Keep()
        self.keep.login(self.username, self.password)
        
        # try:
        note = self.keep.createNote(self.parser.mandatoryParse.titlePhrase, self.parser.mandatoryParse.textPhrase)
        note.pinned = True
        note.color =gkeepapi._node.ColorValue.Pink
        # except Exception as error:
        #     raise RuntimeError("Error creating note: %s" % str(error))
        self.keep.sync()