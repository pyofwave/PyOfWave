from pyofwave.protocols import WaveProtocol

# Test stream, not sure if this would work asynchronous
class Stream(object):
    SCHEDULE = []

    @classmethod
    def loop(cls):
        while cls.SCHEDULE:
            (callback, data, done) = cls.SCHEDULE[0]
            del cls.SCHEDULE[0]
            if callback:
                callback(data)
                done and done()
            elif isinstance(data, float) and data < time.time():
                if cls.SCHEDULE:
                    cls.SCHEDULE.append((callback, data, done))
                else:
                    done and done()
            else:
                done and done()

    class IO(object):
        def add_timeout(self, when, callback):
            Stream.SCHEDULE.append((None, time.time(), callback))

    def __init__(self, name, app, dest):
        self.name = name
        self.dest = dest
        self.reader = None
        self.closed = None
        self.socket = None
        self.io = self.IO()

        print '%s: OPEN' % self.name
        self.target = app.Core(self, **app.settings)

    def read(self, callback):
        self.reader = callback
        return self

    def shutdown(self, callback=None):
        self.on_close(callback)
        self.SCHEDULE.append((None, None, self.close))

    def on_close(self, callback):
        self.closed = callback

    def write(self, data, callback=None):
        print '%s:' % self.name, data
        if self.dest:
            self.SCHEDULE.append((self.dest, data, callback))
        return self

    def close(self):
        print '%s: CLOSED' % self.name
        self.closed and self.closed()
