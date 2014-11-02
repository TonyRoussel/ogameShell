class Cmd(object):
    def __init__(self, prgString, argList, nxtCmd = None):
        self.prg = prgString
        self.arg = argList
        self.nxt = nxtCmd

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
