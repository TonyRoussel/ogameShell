from ogmShellCoreHandler import constants

def printIntelDict(intel):
    for intelType, intelQuantity in intel.items():
        print(intelType, ': ', intelQuantity, sep='')
    return 0

def get(cmd, sessions):
    options = getLoadOptions(cmd.arg)#########
    if (options is None):
        return constants.OPTION_UNKNOWN
    planetSet = getLoadPlanetSet(cmd.arg)#########
    if (planetSet is None):
        return constants.NO_MATCH
    errorCode = getProcess(sessions.focusedSession, options, planetSet)########
    if (errorCode != 0):
        return getError(errorCode)###########
    return getDisplay(options, planetSet)#########
