from ogmSession import *

class ogmSessionsManager(object):
    def __init__(self):
        self.sessions = list()
        self.locked = list()
        self.focusedSession = None

    def getSession(self, universe, username):
        """Return and set as focusedSession the session specified by username\
        and universe parameter, or False if no session can be found with the\
        provided id"""
        for session in self.sessions:
            if (session.identifier == (universe, username)):
                self.focusedSession = session
                return self.focusedSession
        return False

    def getSessionId(self, universe, username):
        for index, session in enumerate(self.sessions):
            if (session.identifier == (universe, username)):
                return index
        return False

    def addSession(self, universe, username, password):
        existingSession = self.getSession(universe, username)
        if (existingSession is not False):
            self.focusedSession = existingSession
            return True
        newSession = ogmSession(universe, username, password)
        if (newSession.log() is False):
            return False
        self.sessions.append(newSession)
        self.locked.append(0)
        self.focusedSession = self.sessions[-1]
        return True

    def popSession(self, universe, username):
        index = self.getSessionId(universe, username)
        if (index is False):
            return False
        self.sessions.pop(index)
        self.locked.pop(index)
        self.switchFocus()
        return True

    def switchFocus(self):
        sessionsLen = len(self.sessions)
        if (sessionsLen == 0):
            self.focusedSession = None
            return False
        if (self.focusedSession is None or sessionsLen == 1):
            self.focusedSession = self.sessions[0]
            return self.focusedSession
        focusIndex = self.getSessionId(*self.focusedSession.identifier)
        if (focusIndex == sessionsLen - 1):
            self.focusedSession = self.sessions[0]
            return self.focusedSession
        self.focusedSession = self.sessions[focusIndex + 1]
        return self.focusedSession

    @property
    def focusedSession(self):
        return self._focusedSession

    @focusedSession.setter
    def focusedSession(self, session):
        self._focusedSession = session

    @property
    def sessions(self):
        return self._sessions

    @sessions.setter
    def sessions(self, aList):
        self._sessions = aList

# Test
if (__name__ == "__main__"):
    import getpass
    universe = input("! type your universe: ")
    username = input("! type your username: ")
    password = getpass.getpass("! type your password: ")
    universe2 = input("! type your universe: ")
    username2 = input("! type your username: ")
    password2 = getpass.getpass("! type your password: ")
    
    sessions = ogmSessionsManager()
    print("addSession 1:", sessions.addSession(universe, username, password))
    print("addSession 2:", sessions.addSession(universe2, username2, password2))
    print("popSession 1:", sessions.popSession(universe, username))
    print("popSession 2:", sessions.popSession(universe2, username2))
    print ("test done")
