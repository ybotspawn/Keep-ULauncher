import os
import json
import logging
import distutils.spawn
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.item.SmallResultItem import SmallResultItem
from ulauncher.api.shared.action import BaseAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from KeepCreateAction import KeepCreateAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction

logging.basicConfig()
logger = logging.getLogger(__name__)

class KeepExtension(Extension):
    def __init__(self):
        super(KeepExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        # self.subscribe(ItemEnterEvent, ItemEnterEventListener())    

# class ItemEnterEventListener(EventListener):
#     def on_event(self, event, extension):
#         # pref_profiles_path = extension.preferences['profiles']
#         logger.debug("uLauncher Keep ItemEnterEventListener")
#         # return KeepCreateAction.KeepCreateAction()
#         return BaseAction()

class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items = []
        items.append(ExtensionResultItem(icon='images/keep-icon.svg', name="Create new note", description='C', on_enter=ExtensionCustomAction("create", keep_app_open=True)))
        items.append(ExtensionResultItem(icon='images/keep-icon.svg', name="Search existing notes", description='S', on_enter=ExtensionCustomAction("create", keep_app_open=True)))
        return RenderResultListAction(items)

if __name__ == "__main__":
    KeepExtension().run()