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

logging.basicConfig()
logger = logging.getLogger(__name__)

class KeepExtension(Extension):
    def __init__(self):
        super(KeepExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        # self.subscribe(ItemEnterEvent, ItemEnterEventListener())

class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        # pref_profiles_path = extension.preferences['profiles']
        logger.debug("uLauncher Keep ItemEnterEventListener")
        # Get query
        term = (event.get_argument() or "").lower()
        logger.debug("uLauncher Keep ItemEnterEventListener argument: %s" % term)
        # return KeepCreateAction.KeepCreateAction()
        return BaseAction()

class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        # pref_profiles_path = extension.preferences['profiles']
        logger.debug("uLauncher Keep KeywordQueryEventListener")
        # Get query
        term = (event.get_argument() or "").lower()
        logger.debug("uLauncher Keep KeywordQueryEventListener argument: %s" % term)
        return RenderResultListAction(list(term))

if __name__ == "__main__":
    KeepExtension().run()