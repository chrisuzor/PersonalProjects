class Borg:

    """The Borg design pattern"""

    _shared_data = {}

    def __init__(self):
        self.__dict__ = self._shared_data  # make an attribute dictionary


class Singleton(Borg):

    """The singleton class"""

    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(
            kwargs
        )  # Update the attribute dictionary by inserting a new key-value pair

    def __str__(self):
        return str(self._shared_data)  # Returns the attribute dictionary


x = Singleton(HTTP="Hyper Text Transfer Protocol")
print(x)
y = Singleton(SNMP="Simple Network Management Protocol")
print(y)
