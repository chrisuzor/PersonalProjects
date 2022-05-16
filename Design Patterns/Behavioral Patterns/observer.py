class Subject(object):
    """Represents what is being observed"""

    def __init__(self):
        # This is where references to all observers are stored
        # Note this is a one - to - many relationship
        self.observers = []

    def attach(self, observer):
        # If the observer is not already in the observers list, append the observer to the list
        if observer not in self.observers:
            self.observers.append(observer)

    def detach(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        # For all the observers in the list, Don't notify the observer who is actually updating the temperature ...
        # Alert the observers!
        for observer in self.observers:
            if modifier != observer:
                observer.update(self)


class Core(Subject):
    """Inherits from the subject class"""

    def __init__(self, name=""):
        Subject.__init__(self)
        self.name = name  # Set the name of the core
        self.temp = 0  # Initialize the temperature of the core

    @property  # Getter that gets the core temperature
    def temp(self):
        return self.temp

    @temp.setter  # Setter that sets the core temperature
    def temp(self, temp):
        self.temp = temp
        # Notify the observers whenever somebody changes the core temperature
        self.notify()


class TempViewer:
    def update(self, subject):  # Alert method that is invoked when the ..
        print(
            "Temperature Viewer: {} has Temperature {}".format(
                subject.name, subject.temp
            )
        )


# Let's create our subjects
c1 = Core("One")
c2 = Core("Two")

# Let's create our observers
v1 = TempViewer()
v2 = TempViewer()

# Let's attach our observers to the first core
c1.attach(v1)
c1.attach(v2)

# Let's change the temperature of our first core
c1.temp = 80
c2.temp = 90
