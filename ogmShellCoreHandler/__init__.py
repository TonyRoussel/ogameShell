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
            retCode = self._treeWalker(tree, sessions)
            if (retCode == constants.EXIT_CODE):
                raise EOFError
 
    def _builtin(self, cmd, sessions):
        if (cmd.prg == "exit"):
            return constants.EXIT_CODE
        elif (cmd.prg == 'log'):
            return self._log(cmd, sessions)
        elif (cmd.prg == 'switch'):
            return self._switch(cmd, sessions)
        return 1

    def _treeWalker(self, tree, sessions):
        ret = self._nodeRun(tree.cmd, sessions)
        if (ret == constants.EXIT_CODE or (tree.left is None and tree.right is None)):
            return ret
        if (tree.left is not None and ret == 0):
            return self._treeWalker(tree.left, sessions)
        if (tree.right is not None and ret != 0):
            return self._treeWalker(tree.right, sessions)
        return ret

    def _nodeRun(self, cmd, sessions):
        ret = self._builtin(cmd, sessions)
        if (ret <= 0):
            return ret
        # ret = self._ogameLayer(cmd, sessions)##############
        # if (ret >= 0):
        #     return ret
        return self._noCommand(cmd)

    def _noCommand(self, cmd):
        print (cmd.prg, ': command not found', sep='')
        return 1

    def _log(self, cmd, sessions):
        if (len(cmd.arg) != 2):
            print ('usage: log universe username')
            return
        password = getpass.getpass("Password for " + cmd.arg[1] + ": ")
        try:
            sessions.addSession(cmd.arg[0], cmd.arg[1], password)
        except BAD_UNIVERSE_NAME:
            print ('Bad universe name')
            return -1
        except CANT_LOG:
            print ('Can\'t log. Your username or password may be wrong. Or maybe no interweb ?')
            return -1
        else:
            print ('logged as ', cmd.arg[1], '@', cmd.arg[0], sep='')
            return 0

    def _switch(self, cmd, sessions):
        sessions.switchFocus()
        return 0

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
