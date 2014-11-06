import ogmSessionsManager
import ogmShellCoreHandler
import readline

class ogmShell(object):
        def __init__(self):
                self.sessions = ogmSessionsManager.ogmSessionsManager()
                self.core = ogmShellCoreHandler.ogmShellCore()
                self.inputHistory = list()
                self.userinput = None
                self.run()

        def run(self):
                try:
                        while True:
                                prompt = self.buildPrompt()
                                self.userinput = input(prompt)
                                if (self.core.run(self.userinput, self.sessions) == -1):
                                        break
                except EOFError:
                        print("exit")

        def buildPrompt(self):
                focusSession = self.sessions.focusedSession
                if focusSession is None:
                        return ('> ')
                return ('{}@{} > '.format(focusSession.username, focusSession.universe))

        @property
        def sessions(self):
                return self._sessions

        @sessions.setter
        def sessions(self, sessionsHandler):
                self._sessions = sessionsHandler

        @property
        def userinput(self):
                return self._userinput

        @userinput.setter
        def userinput(self, userinput):
                self._userinput = userinput
                if (self.userinput is not None and self.userinput.strip() != ''):
                        self.inputHistory.append(self.userinput)

        @property
        def inputHistory(self):
                return self._inputHistory

        @inputHistory.setter
        def inputHistory(self, inputHistory):
                self._inputHistory = inputHistory

# Test
if (__name__ == "__main__"):
        sh = ogmShell()

        print('HISTORY')
        print(sh.inputHistory)

        del(sh)
        print ("test done")
