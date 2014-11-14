import re
from collections import Counter

from ogmShellCoreHandler import constants

import pprint##########

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
    errorCode = getProcess(sessions.focusedSession, options, planetSet)
    if (errorCode != 0):
        return getError(errorCode)
    pprint.pprint(planetSet)#########
    return 0##########
    return getDisplay(options, planetSet)#########

def getProcess(session, options, planetSet):
    if (options['help']):
        return (getUsage())
    for planetName in planetSet:
        if options['resources']:
            planetSet[planetName]['resources'] = session.session.getResources(planetName)
        if options['ships']:
            planetSet[planetName]['ships'] = session.session.getShips(planetName)
        #planetSet[planetName]['unAttack'] = session.session.isUnderAttack(planetName) if options['unAttack'] else None
    if options['pendMsg']:
        planetSet['!general'] = getProcessGeneral(session, options)
    if (options['resources'] or options['ships']):
        planetSet['!sum'] = getProcessSum(planetSet, options)
    return 0

def getProcessGeneral(session, options):
    generalInfo = {}
    if options['pendMsg']:
        generalInfo['pendMsg'] = session.session.pendingMsgQuantity()
    return generalInfo

def getProcessSum(planetSet, options):
    sumInfo = {}
    if options['resources']:
        resources = Counter({})
        for planetName in planetSet:
            if planetName[0] != '!':
                resources += Counter(planetSet[planetName]['resources'])
        sumInfo['resources'] = resources
    if options['ships']:
        ships = Counter({})
        for planetName in planetSet:
            ships += Counter(planetSet[planetName]['ships'])
        sumInfo['ships'] = ships
    return sumInfo
    

def getUsage():
    print("usage: get [OPTION]... [PLANETNAME]...")
    print("OPTIONS:")
    print("     -h display this help")
    print("     -U under attack status")
    print("     -m pending messages quantity")
    print("     -S ships quantity")
    print("     -R display resources status")
    print("     -p display informations planet by planet (sum is added at the end)")
    return 0

def getError(errorCode):
    if (errorCode == constants.OPTION_UNKNOWN):
        print('Unknown option passed')
    elif (errorCode == constants.NO_MATCH):
        print('Unknown planet error')
    else:
        print('Unknown error occured')
    return errorCode

def getLoadOptions(argList):
    optionsDefault = {'help' : False,
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
    index = -1
    for index, arg in enumerate(argList):
        if (arg[0] != '-'):
            if (index != 0):
                return options
            return optionsDefault
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
    if (index >= 0):
        return options
    return optionsDefault

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
            print(planetName, 'doesn\'t match any planet name on this session')
            return None
        planetSet[planetName] = {'!id': session.session.getPlanetIdByName(planetName)}
    return planetSet
