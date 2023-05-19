from tv import remote_control

def main():
    TV = remote_control()

    print(""""This is your TV's remote control!
    Please select the action you want to execute.
    1. Turn the TV ON = 1
    2. Turn the TV OFF = 2
    3. Set the Volume = 3
    4. Set the Channel = 4
    5. Display current status = 5
    """)

while(True):
    remote_action = input(str("Select the number of your desired action to take: "))
    if remote_action == "1":
        TV.tv_on()
    else:
        break

