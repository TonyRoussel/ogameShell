from ogame.errors import BAD_UNIVERSE_NAME, BAD_DEFENSE_ID, NOT_LOGGED
import getpass
import ogmSessionsManager

class ogmShell(object):
        def __init__(self):
                self.sessions = ogmSessionsManager.ogmSessionsManager()
                self.inputHistory = list()
                self.userinput = None
                self.run()

        def run(self):
                try:
                        while True:
                                prompt = self.buildPrompt()
                                self.userinput = input(prompt)
                                builtinRet = self._builtin(self.userinput)
                                if (builtinRet == -1):
                                        break
                                elif (builtinRet == -2):
                                        continue
                except EOFError:
                        print("exit")

        def buildPrompt(self):
                focusSession = self.sessions.focusedSession
                if focusSession is None:
                        return ('> ')
                return ('{}@{} > '.format(focusSession.username, focusSession.universe))

        def _builtin(self, usrinput):
                if (usrinput is None or usrinput.strip() == ''):
                        return -2
                wordList = usrinput.split()
                if (usrinput.strip() == "exit"):
                        return -1
                elif (wordList[0] == 'log'):
                        self._log(wordList)
                return -3

        def _log(self, wordList):
                if (len(wordList) != 3):
                        print ('usage: log universe username')
                        return
                password = getpass.getpass("Password: ")
                try:
                        if (self.sessions.addSession(wordList[1], wordList[2], password) is False):
                                print ('Can\'t log. Your username or password may be wrong. Or maybe no interweb ?')
                        else:
                                print ('logged as ', wordList[2], '@', wordList[1], sep='')
                except BAD_UNIVERSE_NAME:
                        print ('Bad universe name')

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
