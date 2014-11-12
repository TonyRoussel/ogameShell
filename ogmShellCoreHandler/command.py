import re
from ogmShellCoreHandler import constants

def printIntelDict(intel):
    for intelType, intelQuantity in intel.items():
        print(intelType, ': ', intelQuantity, sep='')
    return 0

def get(cmd, sessions):
    options = getLoadOptions(cmd.arg)
    if (options is None):
        return getError(constants.OPTION_UNKNOWN)
    planetSet = getLoadPlanetSet(cmd.arg, sessions.focusedSession)
    if (planetSet is None):
        return getError(constants.NO_MATCH)
    errorCode = getProcess(sessions.focusedSession, options, planetSet)########
    if (errorCode != 0):
        return getError(errorCode)
    return getDisplay(options, planetSet)#########

def getError(errorCode):
    if (errorCode == constants.OPTION_UNKNOWN):
        print('Unknown option passed')
    elif (errorCode == constants.NO_MATCH):
        print('Unknown planet error')
    else:
        print('Unknown error occured')
    return errorCode

def getLoadOptions(argList):
    if (len(argList) == 0):
        return {'help' : False,
               'unAttack' : True,
               'pendMsg' : True,
               'ships' : True,
               'resources' : True,
               'splitPlanet' : False}
    options = {'help' : False,
               'unAttack' : False,
               'pendMsg' : False,
               'ships' : False,
               'resources' : False,
               'splitPlanet' : False}
    for arg in argList:
        if (arg[0] != '-'):
            return options
        if (not re.match('^-[hUmSRp]+$', arg)):
            return None
        if ('h' in arg):
            options['help'] = True
        if ('U' in arg):
            options['unAttack'] = True
        if ('m' in arg):
            options['pendMsg'] = True
        if ('S' in arg):
            options['ships'] = True
        if ('R' in arg):
            options['resources'] = True
        if ('p' in arg):
            options['splitPlanet'] = True
    return options

def getLoadPlanetSet(argList, session):
    index = 0
    for index, arg in enumerate(argList):
        if (arg[0] != '-'):
            break
    if (len(argList) == 0 or len(argList[index:]) == 1 and argList[index:][0][0] == '-' ):
        index = 0
        argList = list(session.session.planets.keys())
    planetSet = {}
    for planetName in argList[index:]:
        if (not session.session.planetNameExist(planetName)):
            return None
        planetSet[planetName] = None
    return planetSet
