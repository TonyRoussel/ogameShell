from ogmShellCoreHandler import constants, token, tree

class Parser(object):
    def parse(self, tokenList):
        if (self._isCoherent(tokenList) is False):
            return None
        tokenGroup = self._cutSEP(tokenList)
        treeList = self._treePlanter(tokenGroup)
        return treeList

    def _isCoherent(self, tokenList):
        mustCMD = True
        if (self._isSpecialToken(tokenList[-1]) is True):
            print ('Error near \'', tokenList[-1].string, '\'', sep='')
            return False
        for token in tokenList:
            if (mustCMD is True and token.tokType != constants.CMD):
                print ('Error near \'', token.string, '\'', sep='')
                return False
            if (self._isSpecialToken(token) is True):
                mustCMD = True
                continue
            mustCMD = False
        return True

    def _isSpecialToken(self, token):
        return not (token.tokType == constants.CMD or token.tokType == constants.ARG)

    def _cutSEP(self, tokenList):
        tokenGroup = []
        subGroup = []
        for token in tokenList:
            if (token.tokType != constants.SEP):
                subGroup.append(token)
            else:
                tokenGroup.append(subGroup)
                subGroup = []
        tokenGroup.append(subGroup)
        return tokenGroup

    def _treePlanter(self, tokenGroup):
        treeList = []
        for tokenList in tokenGroup:
            treeList.append(self._treeSeed(tokenList))
        return treeList

    def _treeSeed(self, tokenList):
        leaf = tree.Tree(tree.Cmd(tokenList[0].string))
        directionIndex = self._argSeek(tokenList[1:], leaf)
        if (directionIndex is None):
            return leaf
        if (tokenList[directionIndex].tokType == constants.AND):
            leaf.left = self._treeSeed(tokenList[directionIndex + 1:])
        else:
            leaf.right = self._treeSeed(tokenList[directionIndex + 1:])
        return leaf

    def _argSeek(self, tokenList, leaf):
        for index, token in enumerate(tokenList):
            if (self._isSpecialToken(token) is True):
                return index + 1
            leaf.cmd.arg.append(token.string)
        return None
