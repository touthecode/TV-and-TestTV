# Make the class
class Tv():

    # Create a constructor
    def __init__(self, on = False, volume = 0, channel = 1):
        self.on = on
        self.volume = volume
        self.channel = channel
    # A function for turning the tv on
    def TvOff(self):
        self.on = True
    # A function for turning the tv off   
    def TvOn(self):
        self.on = False
    # A function to get the value of "channel"
    def GetChannel(self):
        return self.channel
    # A function to set parameters on the value of "channel"
    def SetChannel(self, channel):
        if self.on and 1 <= channel <= 120:
            self.channel = channel


