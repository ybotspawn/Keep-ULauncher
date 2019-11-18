import os
import json
import logging
import gkeepapi
import distutils.spawn
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.item.SmallResultItem import SmallResultItem
from ulauncher.api.shared.action import BaseAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent

logging.basicConfig()
logger = logging.getLogger(__name__)

class KeepExtension(Extension):
    def __init__(self):
        super(KeepExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())    

class ItemEnterEventListener(EventListener):
    def parse_create_note(self, query):
        self.title = query.split(' ')[0]
        if len(query.split(' ')) > 1:
            self.text = query.split(' ')[1] # testing purposes
        else:
            self.text = "Blank text"

    def on_event(self, event, extension):
        # logger.debug("uLauncher Keep ItemEnterEventListener: entry")
        data = event.get_data()
        # logger.info("uLauncher Keep ItemEnterEventListener, got data: %s" % str(data))
        on_enter = data["text"]
        parse_create_note(on_enter)
        keep = gkeepapi.Keep()
        keep.login(extension.preferences["keyuser"], extension.preferences["keycode"])
        if (True): # Placeholder for create vs search logic
            note = keep.createNote(self.title, self.text)
        keep.sync()
        return HideWindowAction()        

class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items = []
        query = event.get_argument()
        items.append(ExtensionResultItem(icon='images/keep-icon.svg', name="Create", description='Create a new note', on_enter=ExtensionCustomAction({"id": 1, "text": query}, keep_app_open=True)))
        # items.append(ExtensionResultItem(icon='images/keep-icon.svg', name="Search", description='Search existing notes', on_enter=ExtensionCustomAction("create", keep_app_open=True)))
        return RenderResultListAction(items)

if __name__ == "__main__":
    KeepExtension().run()