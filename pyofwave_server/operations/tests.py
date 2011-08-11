def operation(ip, foo):
    """A simple Operation to test against."""
    
def result(ip, foo, bar):
    """A simple Operation to test return values against."""
    return {'Star Trek' : {"Spock": "spock@federation.gov",},
            'Firefly' : {"Malcom" : "malcom@serenity.ship",
                         "Shepherd" : "shepherd@serenity.ship"},
            'Doctor Who' : {"The Master" : "master@timelords.gal",},
            'Star Wars' : {"Yoda" : "yoda.jedi.org",}
            }

def error(ip):
    """A simple Operation to test errors against."""
    from .. import operations
    raise operations.OperationError(500, cause="I can't let you do that.",  reason="DON'T SHUT ME DOWN!")
