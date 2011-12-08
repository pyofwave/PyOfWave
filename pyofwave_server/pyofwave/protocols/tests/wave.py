import unittest
from pyofwave.protocols import wave

from lxml.builder import E

class TestMethods(unittest.TestCase):
    def testMethods(self):
        obj = wave.WaveProtocol(None, None)
        obj.is_stanza("operation")
        obj.handle_stanza(E.operation())

if __name__ == '__main__':
    unittest.main()
