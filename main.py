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
    def test_results(self):
        return [
            ExtensionResultItem(
                name="A",
                description="Letter A",
                keyword="a"
            ), 
            ExtensionResultItem(
                name="B",
                description="Letter B",
                keyword="b"
            ),ExtensionResultItem(
                name="C",
                description="Letter C",
                keyword="C"
            )]
    

# class ItemEnterEventListener(EventListener):
#     def on_event(self, event, extension):
#         # pref_profiles_path = extension.preferences['profiles']
#         logger.debug("uLauncher Keep ItemEnterEventListener")
#         # return KeepCreateAction.KeepCreateAction()
#         return BaseAction()

class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items = []
        items.append(ExtensionResultItem(icon='images/keep-icon.svg', name="A", description='A', on_enter=ExtensionCustomAction("d", keep_app_open=True)))
        return RenderResultListAction(items)

if __name__ == "__main__":
    KeepExtension().run()