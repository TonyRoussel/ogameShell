class token(object):
    def __init__(self, string, tokType):
        self.string = string
        self.tokType = tokType

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, value):
        self._string = value

    @property
    def toktype(self):
        return self._toktype

    @toktype.setter
    def toktype(self, value):
        self._toktype = value
