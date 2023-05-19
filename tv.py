# Make the class
class remote_control():

    # Create a parametrized constructor
    def __init__(self, power = "OFF", volume = 0, channel = 1):
        self.power = power
        self.volume = volume
        self.channel = channel
    # Create method to change power status of tv
    def tv_on(self):
        if self.power == "OFF":
            print("The TV is now turning ON!")
        else:
            print("Sorry but the TV is already turned ON!")
