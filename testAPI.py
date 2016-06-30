#!/home/jvo78226/eve_crest/venvcrest/bin/python
import pycrest

eve = pycrest.EVE()


def getEndpoints(eveObj):
    for endpoint in list(eveObj()._dict.items()):
        print(endpoint)


getEndpoints(eve)