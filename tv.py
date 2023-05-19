# Make the class
class Tv():
    # Create a constructor
    def __init__(self, on = False, volume = 1, channel = 1):
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
    # A function to get the value of "volume"
    def GetVolume(self):
        return self.volume
    # A function to set parameters on the value of "volume"
    def SetVolume(self, volume):
        if self.on and 1 <= volume <= 7:
            self.volume = volume
    # A function to add 1 to the value of channel
    def ChannelPlus(self, channel):
        if self.on and 1 <= channel <= 120:
            self.channel += 1
    # A function to minus 1 to the value of channel
    def ChannelMinus(self, channel):
        if self.on and 1 <= channel <= 120:
            self.channel -= 1
    # A function to add 1 to the value of volume
    def VolumePlus(self, volume):
        if self.on and 1 <= volume <= 120:
            self.volume += 1
    # A function to minus 1 to the value of volume
    def VolumeMinus(self, volume):
        if self.on and 1 <= volume <= 120:
            self.volume -= 1