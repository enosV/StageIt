import os

#Last will make all characters uppercase
LastName = input("Last name: ")
Last = LastName.upper()

#First will take the input and capitalize only the first initial of the name provided
FirstName = input("First name: ")
First = FirstName.capitalize()

#RegNo takes any given number and format its into Reg
RegNo = input("Registration Number: ")
Reg = RegNo[:2] + '-' + RegNo[2:]

#NewDir combines the input from the user
NewDir = (Last + ', ' + First + ' ' + str(Reg))

#This is where we tell our program to change directory over to the the network path. The path needs to be mounted prior to setting the path. By default is commented and needs to be commented out to be used.
#os.chdir(r'ENTER_NETWORK_PATH_HERE')

#This will write it on the current working directory (this changes if a path is privided above)
os.makedirs(NewDir)

#This just confirms to the user that the folder has been staged
print("Your case for " + Last + ", " + First + " " + str(Reg) + " has been staged")

