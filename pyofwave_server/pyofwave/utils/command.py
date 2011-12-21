from zope import interface

class CommandInterface(interface.Interface):
    """
    Command pattern interface
    """
    def __init__(self, mergeable=False):
        self.mergeable = mergeable

    def do(self):
        """
        Execute this command
        """
        raise NotImplementedError

    # def mergeWith(self, aCommand):
    #     """
    #     Merge this command with another
    #     """
    #     raise NotImplementedError







