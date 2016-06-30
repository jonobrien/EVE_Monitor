#!/home/jvo78226/eve_crest/venvcrest/bin/python
import pycrest

eve = pycrest.EVE()
eve()

def getEndpoints(eveObj):
    for endpoint in list(eveObj()._dict.items()):
        pass
    #print(endpoint)
#getEndpoints(eve)

# doc helpers for working with CREST data
def getByAttrVal(objlist, attr, val):
    ''' Searches list of dicts for a dict with dict[attr] == val '''
    matches = [getattr(obj, attr) == val for obj in objlist]
    index = matches.index(True)  # find first match, raise ValueError if not found
    return objlist[index]

def getAllItems(page):
    ''' Fetch data from all pages '''
    ret = page().items
    while hasattr(page(), 'next'):
        page = page().next()
        ret.extend(page().items)
    return ret
"""
region = getByAttrVal(eve.regions().items, 'name', 'Catch')
print(region)
print()
item = getByAttrVal(getAllItems(eve.itemTypes), 'name', 'Tritanium').href
print(item)
print()
mkt = getAllItems(region().marketSellOrders(type=item))
print(mkt)
print()
"""




# debug my broken views with pycrest fixes
public_crest = pycrest.EVE()
public_crest()

tranquility_user_count = public_crest().userCount_str
print(tranquility_user_count)
"""
incursions = []
for thing_that_looks_like_a_dict_but_isnt in public_crest.incursions().items:
    incursion = {}
    for key, value in thing_that_looks_like_a_dict_but_isnt._dict.items():
        incursion[key] = value._dict if hasattr(value, '_dict') else value
    incursions.append(incursion)
print(incursions)
print()
"""
inc = getAllItems(public_crest.incursions())
# same as the double nested for loop ^^
print(inc)
