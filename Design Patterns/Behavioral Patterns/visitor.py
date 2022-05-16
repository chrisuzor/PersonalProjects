class House(object):
    def accept(self, visitor):
        """Interface to accept a visitor"""
        # Triggers the visiting operation
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self, "worked on by", hvac_specialist)

    def work_on_electricity(self, electrician):
        # Note that we now have a reference to the electrician object
        print(self, "worked on by", electrician)

    def __str__(self):
        """Simply return the class name when the House object is printed"""
        return self.__class__.__name__


class Visitor(object):
    """Abstract visitor"""

    def __str__(self):
        """Simply return the class name when the visitor object is printed out"""
        return self.__class__.__name__


class HvacSpecialist(Visitor):
    """Concrete visitor: HVAC specialist"""

    def visit(self, house):
        house.work_on_hvac(self)  # Note that the visitor now has a reference


class Electrician(Visitor):
    """Concrete visitor: electrician"""

    def visit(self, house):
        # Note that the visitor now has a reference to the house object
        house.work_on_electricity(self)


# Create an HVAC specialist
hvac_specialist = HvacSpecialist()
# Create an electrician
electrician = Electrician()
# Create a House
house = House()
house.accept(hvac_specialist)
house.accept(electrician)
