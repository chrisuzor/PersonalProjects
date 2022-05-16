import types


class Strategy:
    """The Strategy Pattern class"""

    def __init__(self, function=None):
        self.name = "Default Strategy"

        # If a reference to a function is provided, replace the executed method with a given function
        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):
        """The default method that prints the name of the strategy being used"""
        print("{} is used!".format(self.name))


# replacement method 1
def strategy_one(self):
    print("{} is used to execute method 1".format(self.name))


# replacement method 2
def strategy_two(self):
    print("{} is used to execute method 2".format(self.name))


# Let's create our default strategy
s0 = Strategy()
s0.execute()

# Let's create the first variation of our default strategy by providing another method to strategy
s1 = Strategy(strategy_one)
s1.name = "Strategy One"
s1.execute()


s2 = Strategy(strategy_two)
s2.name = "Strategy Two"
s2.execute()
