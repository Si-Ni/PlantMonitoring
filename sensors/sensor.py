class Sensor:
    def __init__(self, pin):
        self.pin = pin

    def read(self):
        raise NotImplementedError
