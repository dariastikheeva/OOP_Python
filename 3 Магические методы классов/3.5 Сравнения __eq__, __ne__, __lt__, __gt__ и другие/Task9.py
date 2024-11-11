class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    def __gt__(self, body):
        return self.ro * self.volume > body.ro * body.volume
    
    def __eq__(self, body):
        if isinstance(body, Body):
            return self.ro * self.volume == body.ro * body.volume
        else:
            return self.ro * self.volume == body
    
    def __lt__(self, body):
        return self.ro * self.volume < body
