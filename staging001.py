import os

LastName = input("Last name: ")
Last = LastName.upper()

FirstName = input("First name: ")
First = FirstName.capitalize()

FyNo = input("FY Number: ")
FY = FyNo[:2] + '-' + FyNo[4:]

NewDir = (Last + ', ' + First + ' ' + str(FY))
os.makedirs(r'\\SUPERMAN\firstDir\{NewDir}')

print("Your case for " + Last + ", " + First + " " + str(FY) + " has been staged")

