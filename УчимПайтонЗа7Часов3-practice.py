#the program which opens the website
import os

if 'www' in 'www.youtube.com':
    print("right") #оператор in проверяет, есть ли последовательность www в www.youtube.com

site = input("Enter any website: ")
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