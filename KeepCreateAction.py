import gkeepapi
from ulauncher.utils.decorator.run_async import run_async
from ulauncher.api.shared.action.BaseAction import BaseAction

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

    def parse_create_note(self, data):
        self.title = data.split(' ')[0]
        if len(data.split(' ')) > 1:
            self.text = data.replace(self.title, '').strip()
        else:
            self.text = ""

        if not self.title:
            self.title = "Placeholder"
        if not self.text:
            self.text = "Blank"

    def run(self):
        self.keep = gkeepapi.Keep()
        self.keep.login(self.username, self.password)
        
        # try:
        note = self.keep.createNote(self.title, self.text)
        # except Exception as error:
        #     raise RuntimeError("Error creating note: %s" % str(error))
        # self.sync_keep()
        self.keep.sync()
    
    # @run_async(daemon=True)
    # def sync_keep(self):
    #     self.keep.sync()