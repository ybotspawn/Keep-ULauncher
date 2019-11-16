import time
import os
import logging
import subprocess
import tempfile
from ulauncher.api.shared.action.BaseAction import BaseAction

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

    def load_libraries(self):
        pass

    def run(self):

        keep = gkeepapi.Keep()
        success = keep.login(creds[0].replace(' ', '').replace('\n',''), creds[1])


        note = keep.createNote('Todo', 'Eat breakfast')
        note.pinned = True
        note.color = gkeepapi.node.ColorValue.Blue



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