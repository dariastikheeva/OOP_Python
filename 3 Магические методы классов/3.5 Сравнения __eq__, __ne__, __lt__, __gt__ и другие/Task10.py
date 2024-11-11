class Thing:
    def __init__(self, name, mass):
        self.name = name.lower()
        self.mass = mass

    def __eq__(self, other):
        return self.name == other.name and self.mass == other.mass

class Box:
    def __init__(self):
        self.things = []

    def add_thing(self, obj):
        self.things.append(obj)

    def get_things(self):
        return self.things

    def __eq__(self, other):
        return all(item in other.things for item in self.things)
