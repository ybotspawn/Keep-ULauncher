import time
import os
import logging
import subprocess
import tempfile
from ulauncher.api.shared.action.BaseAction import BaseAction
from ulauncher.utils.decorator.run_async import run_async

class CustomAction(BaseAction):
    """
    Runs a custom python action

    :param str pkgfile: customaction json file
    :param str library: library referenced in customaction
    :param str method: method referenced in customaction
    """

    def __init__(self, script, args=None):
        self.script = script
        self.args = args

    def run(self):
        file = tempfile.NamedTemporaryFile(prefix='ulauncher_RunScript_', delete=False)

        try:
            file.write(self.script.encode())
        except Exception:
            file.close()
            raise
        else:
            file.close()

        try:
            os.chmod(file.name, 0o777)
            logger.debug('Running a script from %s', file.name)
            subprocess.Popen(["%s %s" % (file.name, self.args)],
                             shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
            self.remove_temp_file(file.name)
        except Exception:
            self.remove_temp_file(file.name)
            raise