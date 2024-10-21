class Car:
    def ckeck_model(self, model):
        return isinstance(model, str) and 1 < len(model) < 101

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, model):
        if self.ckeck_model(model):
            self.__model = model
