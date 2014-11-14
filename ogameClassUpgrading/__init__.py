import ogame
from bs4 import BeautifulSoup


class OGameO(ogame.OGame):
    def __init__(self, universe, username, password):
        super(OGameO, self).__init__(universe, username, password)
        self.planets = self.getPlanetsDict()

    def getPlanetNameById(self, id_search):
        for name, id_register in self.planets.items():
            if id_search == id_register:
                return (name)
        return None

    def getPlanetIdByName(self, planetName):
        if (planetName not in self.planets):
            raise BAD_PLANET_NAME
        return self.planets[planetName]

    def planetNameExist(self, name):
        return name in self.planets

    def getPlanetsDict(self):
        """Returns the planets name"""
        planetsName = dict()
        res = self.session.get(self.get_url('overview')).content
        soup = BeautifulSoup(res)
        planets = soup.findAll('div', {'class': 'smallplanet'})
        for planet in planets:
            name = planet.find('span', {'class': 'planet-name'}).string
            if name == None:
                continue
            id = planet['id'].replace('planet-', '')
            planetsName[name] = id
        return planetsName

    def getResources(self, name):
        if (name not in self.planets):
            raise BAD_PLANET_NAME
        id = self.planets[name]
        resources = self.get_resources(id)
        return (resources)

    def getTotalResources(self, toGet = ['metal', 'crystal', 'deuterium']):
        resources = dict()
        for typeToGet in toGet:
            resources[typeToGet] = 0
        for planet_name, planet_id in self.planets.items():
            resourcesCurrent = self.getResources(planet_name)
            for resourcesType, quantity in resourcesCurrent.items():
                if (resourcesType not in resources):
                    continue
                resources[resourcesType] += quantity
        return (resources)

    def getShips(self, name):
        if (name not in self.planets):
            raise BAD_PLANET_NAME
        id = self.planets[name]
        ships = self.get_ships(id)
        return (ships)

    def friendlyMissionInProgress(self):
        json = self.fetch_eventbox()
        return json.get('friendly', 0)

    def pendingMsgQuantity(self):
        res = self.session.get(self.get_url('overview')).content
        soup = BeautifulSoup(res)
        newMsgQ = soup.find('a', {'id': 'message_alert_box'})
        newMsgQ = newMsgQ.text.strip() if newMsgQ is not None else 0
        return newMsgQ

    def stupid(self, planet_id):
        url = self.get_url('fetchResources', planet_id)
        code = self.session.get(url, allow_redirects=False).status_code
        return code


    def testFunction(self):
        print("test ok")







# Test
if (__name__ == "__main__"):
    import getpass
    universe = input("! type your universe: ")
    username = input("! type your username: ")
    password = getpass.getpass("! type your password: ")

    ogm = OGameO(universe, username, password)
    print ("Log: ", str(ogm.is_logged()))
    """print ("RESOURCES")
    for planet_name, planet_id in ogm.planets.items():
        print (planet_name, 'TURN')
        resources = ogm.getResources(planet_name)
        print ('Metal:', resources['metal'])
        print ('Crystal:', resources['crystal'])
        print ('Deut:', resources['deuterium'])
        print ('Energy:', resources['energy'])
        print ('')
    print (ogm.getTotalResources(['metal', 'deuterium', 'crystal']))
    print ("\nShips")
    for planet_name, planet_id in ogm.planets.items():
        print (planet_name, 'TURN')
        ships = ogm.getShips(planet_name)
        for shipsType, shipsQuantity in ships.items():
            if (shipsQuantity == 0):
                continue
            print (shipsType, ': ', shipsQuantity, sep='')
        print ('')"""
    print ('new msg:', ogm.pendingMsgQuantity())
    print ('friendly mission in progress:', ogm.friendlyMissionInProgress())
    print ('underAttack:', ogm.is_under_attack())
    #print ('stupid:', ogm.stupid(1111))
    ogm.testFunction()
