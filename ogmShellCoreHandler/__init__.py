from ogmShellCoreHandler import lexer, parser, constants
from ogame.errors import BAD_UNIVERSE_NAME, BAD_DEFENSE_ID, NOT_LOGGED, CANT_LOG
import getpass

class ogmShellCore(object):
    def __init__(self):
        self._lexer = lexer.Lexer()
        self._parser = parser.Parser()

    def run(self, usrinput, sessions):
        #LEXING
        tokenList = self._lexer.lexIt(usrinput)
        #PARSING
        treeList = self._parser.parse(tokenList)
        #EXECUTION
        for tree in treeList:
            retCode = self._treeWalker(tree)################
            if (retCode == constants.EXIT_CODE):
                raise EOFError
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

    def _treeWalker(self, tree):
        ret = self._nodeRun(tree.cmd)
        if (ret == constants.EXIT_CODE or (tree.left is None and tree.right is None)):
            return ret
        if (tree.left is not None and ret == 0):
            return self._treeWaler(tree.left)
        if (tree.right is not None and ret != 0):
            return self._treeWaler(tree.right)
        return ret

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

    def _printTreeDebug(self, treeList):
        for tree in treeList:
            print ('NEW TREE')
            leaf = tree
            while True:
                print ('cmd', leaf.cmd.prg)
                print ('arg', leaf.cmd.arg)
                if (leaf.left is None and leaf.right is None):
                    break
                if (leaf.left is not None):
                    print ('Going Left')
                    leaf = leaf.left
                    continue
                print ('Going Right')
                leaf = leaf.right
