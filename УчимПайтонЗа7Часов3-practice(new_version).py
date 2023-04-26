#the program which opens the website (cicle)
import os

while True:
    site = input("Enter any website: \n")
    if site == "break":
        break

    if 'https://' in site:
        os.system('start ' + site)
        print("full adress")

    elif 'www.' in site:
        site = 'https://' + site
        os.system('start ' + site)
        print("almost full adress")

    else:
        site = 'https://www.' + site
        os.system('start ' + site)
        print("It's OK")