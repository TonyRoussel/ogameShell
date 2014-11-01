from ogmShellCoreHandler import constants, token

class lexer(object):
    def __init__(self):
        self._blockSeparator = ';'
        self._cmdAnd = '&&'
        self._cmdOr = '||'
        self._specialString = [self._blockSeparator, self._cmdAnd, self._cmdOr]
        self.specialCorrespondance = {self._blockSeparator : SEP, self._cmdAnd : AND, self._cmdOr : OR}

    def lexIt(self, strings):
        tokenList = list()
        stringsList = strings.split()
        cmdDummy = True
        for string in stringsList:
            if (string in self._specialString):
                cmdDummy = True
                tokenList.append(token(string, self.specialCorrespondance[string]))
                continue
            if (cmdDummy is True):
                tokenList.append(token(string, CMD))
                cmdDummy = False
                continue
            tokenList.append(token(string, ARG))
        return tokenList
            
