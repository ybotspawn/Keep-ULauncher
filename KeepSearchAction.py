import gkeepapi
from ulauncher.api.shared.action.BaseAction import BaseAction
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.item.SmallResultItem import SmallResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from QueryParser import *

class KeepSearchAction(BaseAction):
    """
    Runs a custom python action
    # Creating a note
    :param User property: Google Note user property for the creation of a new note
    :param Password property: Google Note password property for the creation of a new note
    
    :param params property: Dictionary containing properties and filters for these properties
    
    :param str method: method referenced in customaction
    """

    def __init__(self, username, password, data):
        self.username = username
        self.password = password

    def run(self):
        self.keep = gkeepapi.Keep()
        self.keep.login(self.username, self.password)
        
        notes = self.keep.find(func=lambda x: x.pinned == True)
        items = []
        for g in notes: # need to limit the output somehow
            items.append(ExtensionResultItem(icon='images/keep-icon.svg', name=g.title, description=g.text, on_enter=OpenUrlAction(g.url))) # need to limit the lenght of the text variable
        return RenderResultListAction(items)

# Taken form the gkeepapi
# # Find by string
# gnotes = keep.find(query='Title')

# # Find by labels
# gnotes = keep.find(labels=[keep.findLabel('todo')])

# # Find by colors
# gnotes = keep.find(colors=[gkeepapi.node.ColorValue.White])

# # Find by pinned/archived/trashed state
# gnotes = keep.find(pinned=True, archived=False, trashed=False)
