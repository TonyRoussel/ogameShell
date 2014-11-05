class Tree(object):
    def __init__(self, cmd, leftTree = None, rightTree = None):
        self.cmd = cmd
        self.left = leftTree
        self.right = rightTree

    @property
    def cmd(self):
        return self._cmd

    @cmd.setter
    def cmd(self, value):
        self._cmd = value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left = value

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right = value




class Cmd(object):
    def __init__(self, prgString, argList = list()):
        self.prg = prgString
        self.arg = argList

    @property
    def prg(self):
        return self._prg

    @prg.setter
    def prg(self, value):
        self._prg = value

    @property
    def arg(self):
        return self._arg

    @arg.setter
    def arg(self, value):
        self._arg = value

    @property
    def nxt(self):
        return self._nxt

    @nxt.setter
    def nxt(self, value):
        self._nxt = value

