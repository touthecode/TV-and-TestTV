# Make the class
class Tv():

    # Create a constructor
    def __init__(self, on = "False", volume = 0, channel = 1):
        self.on = on
        self.volume = volume
        self.channel = channel
    # A function for turning the tv off
    def TvOff(self):
        self.on = True

