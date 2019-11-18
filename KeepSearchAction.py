import gkeepapi
import time
import os
import logging
import subprocess
import tempfile
from ulauncher.api.shared.action.BaseAction import BaseAction

class KeepSearchAction(BaseAction):
    """
    Runs a custom python action

    :param str method: method referenced in customaction
    """

    def __init__(self):
        pass