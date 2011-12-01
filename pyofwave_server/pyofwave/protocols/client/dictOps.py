"""
Dictionary operations for the client protocol.
"""

def flatten(dikt):
    """flattens dictionaries into one, using - to seperate paths."""
    rep = {}
    def combine(inner, i):
        if hasattr(inner, 'keys'):
            for key in inner.keys():
                rep[str(i)+'-'+key] = inner[key]
        else:
            rep[str(i)] = inner
                            
    if isinstance(dikt, dict):
        for key in dikt.keys():
            inner = flatten(dikt[key])
            combine(inner, key)
    
    elif hasattr(dikt, '__iter__'):
        for i in range(len(dikt)):
            inner = flatten(dikt[i])
            combine(inner, i)
  
    else:
        return dikt
    
    return rep

if __name__ == '__main__':
    data = {'Star Trek' : {"Spock": "spock@federation.gov",},
            'Firefly' : {"Malcom" : "malcom@serenity.ship",
                         "Shepherd" : "shepherd@serenity.ship"},
            'Doctor Who' : {"The Master" : "master@timelords.gal",},
            'Star Wars' : {"Yoda" : "yoda.jedi.org",}
            }
    
    print flatten(data)
    
    data = {'Star Trek' : ["spock@federation.gov",],
            'Firefly' : ["malcom@serenity.ship",
                         "shepherd@serenity.ship"],
            'Doctor Who' : ["master@timelords.gal",],
            'Star Wars' : ["yoda.jedi.org",]
            }
    
    print flatten(data)