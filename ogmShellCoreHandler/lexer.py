from ogmShellCoreHandler import constants, token
import shlex

class lexer(object):
    def __init__(self):
        self._blockSeparator = ';'
        self._cmdAnd = '&&'
        self._cmdOr = '||'
        self._specialString = [self._blockSeparator, self._cmdAnd, self._cmdOr]
        self.specialCorrespondance = {self._blockSeparator : constants.SEP, self._cmdAnd : constants.AND, self._cmdOr : constants.OR}

    def lexIt(self, strings):
        tokenList = list()
        stringsList = shlex.split(strings)
        cmdDummy = True
        for string in stringsList:
            if (string in self._specialString):
                cmdDummy = True
                tokenList.append(token.token(string, self.specialCorrespondance[string]))
                continue
            if (cmdDummy is True):
                tokenList.append(token.token(string, constants.CMD))
                cmdDummy = False
                continue
            tokenList.append(token.token(string, constants.ARG))
        return tokenList
            
