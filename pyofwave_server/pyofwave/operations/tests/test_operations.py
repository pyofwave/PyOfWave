from twisted.trial import unittest

class TestOperations(unittest.TestCase):
    def testNewOperation(self):
        NS = "pyofwave.info/test"
        E = ElementMaker(namespace=NS)
        # print "tests.py", E.response()
    
        class op(Operation):
            print E.response()
            @staticmethod
            def r(*args, **kwargs):
                g = globals()
                print g["NS"], g["op"]
                ## print "args:", args
                ## print "kwargs:", kwargs
                print g["E"], g.keys()
                return E.response("success", status=400)
