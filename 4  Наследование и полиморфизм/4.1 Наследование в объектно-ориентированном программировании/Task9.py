class Layer:
    def __init__(self):
        self.next_layer = None
        self.name = 'Layer'

    def __call__(self, layer):
        self.next_layer = layer
        return layer
    
class Input(Layer):
    def __init__(self, inputs):
        super().__init__()
        self.name = 'Input'
        self.inputs = inputs

class Dense(Layer):
    def __init__(self, inputs, outputs, activation):
        super().__init__()
        self.name = 'Dense'
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation

class NetworkIterator(Layer):
    def __init__(self, network):
        super().__init__()
        self.network = network

    def __iter__(self):
        layer = self.network
        while layer != None:
            yield layer
            layer = layer.next_layer
