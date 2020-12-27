import os
#from pathlib import Path #need to check this

LastName = input("Last name: ")
Last = LastName.upper()

FirstName = input("First name: ")
First = FirstName.capitalize()

RegNo = input("Registration Number: ")
Reg = RegNo[:3] + '-' + RegNo[3:]



print("Your case for " + Last + ", " + First + " " + str(Reg) + " has been staged")

