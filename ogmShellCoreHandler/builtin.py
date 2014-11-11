from ogmShellCoreHandler import constants

def focus(cmd, sessions):
    if (len(cmd.arg) == 0):
        focusUsage()
        return 1
    logReq = cmd.arg[0].split('@')
    if (len(logReq) == 1):
        return focusUsername(logReq, sessions)###########
    else:
        return focusIdentifier(logReq, sessions)#########
    return 4

def focusUsage():
    print("usage: focus USERNAME@UNIVERSE or focus USERNAME")
    print("if only the username is provided and multiple sessions match,\
     focus is unchanged and the login possibility are displayed")
    return 0

def focusUsername(logReq, sessions):
    match = sessions.getSessionByUsername(logReq[0])
    if (len(match) == 0):
        return focusError(constants.NO_MATCH)
    if (len(match) > 1):
        return focusError(constants.TOO_MUCH_MATCH, match)
    sessions.focusedSession = match[0]
    return 0

def focusIdentifier(logReq, sessions):
    session = sessions.getSession(logReq[1], logReq[0])
    if (session is False):
        return focusError(constants.NO_MATCH)
    sessions.focusedSession = session
    return 0

def focusError(errorCode, matchList=None):
    if (errorCode is constants.NO_MATCH):
        print("No sessions match the provided id")
        return errorCode
    if (errorCode is constants.TOO_MUCH_MATCH):
        print("Multiple sessions matched: ")
        for session in match:
            print("{}@{}".format(session.username, session.uiverse))
        return errorCode
    return constants.UNHANDLED
