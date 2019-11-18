import gkeepapi
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

    # def __init__(self, username, password, title=None, text=None):
    #     self.username = username
    #     self.password = password
    #     # self.pinned = pinned
    #     self.title = title
    #     self.text = text
    #     # self.color = color
    #     # self.args = args
    def __init__(self, field):
        self.t = field
        self.run()
        
    def keep_app_open(self):
        return False

    def run(self):
        pass
# keep = gkeepapi.Keep()
# keep.login(self.username, self.password)

# # try:
# note = keep.createNote(self.title, self.text)
# note.pinned = self.pinned
# note.color = self.color
# keep.sync()
# except Exception as error:
#     raise RuntimeError("Error creating note: %s" % str(error))