import copy


class Prototype:
    def __init__(self):
        self.objects = {}

    def register_object(self, name, obj):
        """Register an object"""
        self.objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self.objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update it's attributes"""
        obj = copy.deepcopy(self.objects[name])
        obj.__dict__.update(attr)
        return obj


class Car:
    def __init__(self):
        self.name = "Camry"
        self.color = "Silver"
        self.options = "Ex"

    def __str__(self):
        return "{} | {} | {}".format(self.name, self.color, self.options)


c = Car()
prototype = Prototype()
prototype.register_object("camry", c)

c1 = prototype.clone("camry")
print(c1)
