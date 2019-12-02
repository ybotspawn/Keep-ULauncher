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
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from KeepCreateAction import KeepCreateAction

logging.basicConfig()
logger = logging.getLogger(__name__)

class KeepExtension(Extension):
    def __init__(self):
        super(KeepExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())    

class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        eventData = event.get_data()
        data = eventData["data"]
        return KeepCreateAction(extension.preferences["keyuser"], extension.preferences["keycode"], data).run()

class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items = []
        data = event.get_argument()
        items.append(ExtensionResultItem(icon='images/keep-icon.svg', name="Create", description='Create a new note (eg COLOR TITLE Note title TEXT Your Note Text)', on_enter=ExtensionCustomAction({"id": 1, "data": data}, keep_app_open=False)))
        # items.append(ExtensionResultItem(icon='images/keep-icon.svg', name="Search", description='Search existing notes', on_enter=ExtensionCustomAction("create", keep_app_open=True)))
        return RenderResultListAction(items)

if __name__ == "__main__":
    KeepExtension().run()