import os

#Last will make all characters uppercase
LastName = input("Last name: ")
Last = LastName.upper()

#First will take the input and capitalize only the first initial of the name provided
FirstName = input("First name: ")
First = FirstName.capitalize()

#This will ask the user for the FY number. It also ensures that the user only adds numbers and provides
#a friendly exception if they enter anything else that's not a number.
while True:
    try:
        FyNo = int(input("FY Number: "))
        stgn = str(FyNo)
        num = stgn[:2] + '-' + stgn[2:]
        break
    except ValueError:
        print("Oops! Numbers only, please!")

#NewDir combines the 3 inputs from the user
NewDir = (Last + ', ' + First + ' ' + str(num))

#By default the program will write the staged folder to current working directory.
#This is where we tell our program to change directory to the the network path, e.g (r'\\UNCpath\Goes\Here\'). 
#Make sure the network path is mounted on the host prior to using this option.

# os.chdir(r'ENTER_NETWORK_PATH_HERE')

#This will write it on the current working directory unless a netowrk path is provided
os.makedirs(NewDir)

#This just confirms to the user that the folder has been staged
print("Your case for " + Last + ", " + First + " " + str(num) + " has been staged")