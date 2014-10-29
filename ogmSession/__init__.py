from ogameClassUpgrading import *

class ogmSession(object):
    def __init__(self, universe, username, password):
        self.universe = universe
        self.username = username
        self._password = password
        self.session = None

    def log(self):
        if (self.session is not None and self.logged is True):
            return True
        self.session = OGameO(self.universe, self.username, self._password)
        return (self.logged())

    def logged(self):
        return (self.session.is_logged())

    @property
    def universe(self):
        return self._universe

    @universe.setter
    def universe(self, universe):
        self._universe = universe

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def session(self):
        return self._session

    @session.setter
    def session(self, session):
        self._session = session

    @property
    def identifier(self):
        return (self.universe, self.username)

    @identifier.setter
    def identifier(self, whatever):
        self._identifier = self.identifier

        
# Test
if (__name__ == "__main__"):
    import getpass
    universe = input("! type your universe: ")
    username = input("! type your username: ")
    password = getpass.getpass("! type your password: ")
    
    ogmSess = ogmSession(universe, username, password)
    print("log return", ogmSess.log())
    print("identifier is", ogmSess.identifier)
    print("ogm session active:", ogmSess.session.is_logged())
    print("test done")
