from ogmShellCoreHandler import lexer
from ogame.errors import BAD_UNIVERSE_NAME, BAD_DEFENSE_ID, NOT_LOGGED, CANT_LOG

import getpass

class ogmShellCore(object):
    def __init__(self):
        self._lexer = lexer()

    def run(self, usrinput, sessions):
        #LEXING
        tokenList = lexer.lexIt(usrinput)
        #PARSING
        #EXECUTION
        self._builtin(usrinput, sessions)

    def _builtin(self, usrinput, sessions):
        if (usrinput is None or usrinput.strip() == ''):
            return -2
        wordList = usrinput.split()
        if (usrinput.strip() == "exit"):
            return -1
        elif (wordList[0] == 'log'):
            self._log(wordList, sessions)
            return -2
        elif (wordList[0] == 'switch'):
            self._switch(wordList, sessions)
            return -2
        return -3

    def _log(self, wordList, sessions):
        if (len(wordList) != 3):
            print ('usage: log universe username')
            return
        password = getpass.getpass("Password: ")
        try:
            sessions.addSession(wordList[1], wordList[2], password)
        except BAD_UNIVERSE_NAME:
            print ('Bad universe name')
        except CANT_LOG:
            print ('Can\'t log. Your username or password may be wrong. Or maybe no interweb ?')
        else:
            print ('logged as ', wordList[2], '@', wordList[1], sep='')

    def _switch(self, wordList, sessions):
        sessions.switchFocus()
