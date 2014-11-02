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
