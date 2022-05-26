# Start (Import libraries)

import os
from os import system
import sys
import time
import platform 
try:
    import datetime
    import phonenumbers
    from phonenumbers import parse
    from phonenumbers import geocoder
    from phonenumbers import carrier
    from phonenumbers import timezone
    from colorama import Fore
    import random
    from tqdm import tqdm
except:
    print("Installing prerequisites")
    system("pip install phonenumbers")
    system("pip install colorama")
    system("pip install random")
    exit('\n',"Run script Again")

# End (Import libraries)

# Start (Banner & Clearing)

def clear():
   result = platform.uname()[0]
   if result == "Windows":
      system("cls")
   elif result == "Linux":
      system("clear")
clear()

print(Fore.RED+ """
______________                         ______________            ______              
___  __ \__  /___________________      __  ____/__  /_______________  /______________
__  /_/ /_  __ \  __ \_  __ \  _ \     _  /    __  __ \  _ \  ___/_  //_/  _ \_  ___/
_  ____/_  / / / /_/ /  / / /  __/     / /___  _  / / /  __/ /__ _  ,<  /  __/  /    
/_/     /_/ /_/\____//_/ /_/\___/      \____/  /_/ /_/\___/\___/ /_/|_| \___//_/     
                                                                                     """+Fore.RESET)

# End (Banner & Clearing)

# Start (APP & Get Input From User)

try:
    unumber = input(Fore.LIGHTCYAN_EX+" Please Enter Some Phone Number : "+Fore.RESET)
except:
    print(Fore.RED+ "You canceled the program!"+Fore.RESET)
    sys.exit()

try:
    usenumber = int(unumber)
except:
    print('\n',Fore.YELLOW+"Cause of error : You entered a string value."+Fore.RESET)
    print('\n',Fore.RED+"Please Just Enter The integer Value"+Fore.RESET)
    sys.exit()

# End (APP & Get Input From User)

# Start (Wrong Progress bar)

def wrn():
    try:
        print('\n',"Please Wait...",'\n')
        time.sleep(2)
        print("Search For Number...")
        time.sleep(3)
        for i in tqdm(range(0)):
            
            pass
        print(Fore.RED+ "False"+Fore.RESET)
        time.sleep(2)
        print("Search For Operator...")
        time.sleep(3)
        for i in tqdm(range(0)):

            pass
        print(Fore.RED+ "False"+Fore.RESET)
        time.sleep(2)
        print("Search For Location...")
        time.sleep(3)
        for i in tqdm(range(0)):

            pass
        print(Fore.RED+ "False"+Fore.RESET,'\n')
        time.sleep(2)
        print(Fore.RED+ "Error Result:"+Fore.RESET,'\n')
        time.sleep(3)
        print('\n',Fore.RED+ "The format entered is incorrect!"+Fore.RESET)
        print('\n',Fore.YELLOW+ "* Notice : Please enter the phone number using the country code [Example : +98...] *"+Fore.RESET)
    except:
        print(Fore.RED+ "You canceled the program!"+Fore.RESET)
        sys.exit

# End (Wrong Progress bar)

# Start (Check + Is in User Input or Not)

if "+" in unumber:

# Start (True Progress bar)

    try:
        print('\n',"Please Wait...",'\n')
        time.sleep(2)
        print("Search For Number...")
        time.sleep(3)
        for i in tqdm(range(10)):
                    
                    pass
        print(Fore.GREEN+ "Ture"+Fore.RESET)
        time.sleep(2)
        print("Search For Operator...")
        time.sleep(3)
        for i in tqdm(range(10)):

                    pass
        print(Fore.GREEN+ "Ture"+Fore.RESET)
        time.sleep(2)
        print("Search For Location...")
        time.sleep(3)
        for i in tqdm(range(10)):

                    pass
        print(Fore.GREEN+ "Ture"+Fore.RESET,'\n')
        time.sleep(2)
        print("Almost Completed...",'\n')
        time.sleep(3)
    except:
        print(Fore.RED+ "You canceled the program!"+Fore.RESET)
        sys.exit()

# End (True Progress bar)

else:
    wrn()

# End (Check + Is in User Input or Not)   

# Start (Show Result's)

try:
    number = parse(unumber)
    timeZone = timezone.time_zones_for_number(number)
    country = Fore.LIGHTMAGENTA_EX+ geocoder.description_for_number(number,'en')+Fore.RESET
    print("Region/City:",'\n')
    print(timeZone,country)
    print('\n',"Operator:",'\n')
    print(Fore.YELLOW+carrier.name_for_number(number,'en')+Fore.RESET)
    print('\n',"Validation number:",'\n')
    try:
        valid = phonenumbers.is_valid_number(number)+Fore.RESET
        print(valid)
    except:
        possible = phonenumbers.is_possible_number(number)
    print(possible)
    print('\n',"Prees Enter For Exit")
    input(" [!] Press Enter... ")
except:
    print("")
    sys.exit()

# End (Show Result's)
