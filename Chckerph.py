from os import system
    
# Check the requirements
try:
    from phonenumbers import parse
    from phonenumbers import geocoder
    from phonenumbers import carrier
    import datetime
    from colorama import Fore
    import random
    from tqdm import tqdm
    import time
except ImportError:
    system("pip install phonenumbers ")
    system("pip install os ")
    system("pip install datetime ")
    system("pip install colorama ")
    system("pip install random ")
    system("pip install tqdm ")
    system("pip install time ")
    exit("\n\nRun script Again")

# Start APP   
os.system("cls")
print(Fore.RED+ """______________                         ______________            ______              
___  __ \__  /___________________      __  ____/__  /_______________  /______________
__  /_/ /_  __ \  __ \_  __ \  _ \     _  /    __  __ \  _ \  ___/_  //_/  _ \_  ___/
_  ____/_  / / / /_/ /  / / /  __/     / /___  _  / / /  __/ /__ _  ,<  /  __/  /    
/_/     /_/ /_/\____//_/ /_/\___/      \____/  /_/ /_/\___/\___/ /_/|_| \___//_/     
                                                                                     """+Fore.RESET)

unumber = input(Fore.LIGHTCYAN_EX+"Please Enter Some Phone Number : "+Fore.RESET)
print('\n',"Please Wait...",'\n')
time.sleep(5)
print("Search For Number...")
time.sleep(4)
for i in tqdm(range(10)):
    
    pass
print(Fore.GREEN+ "Ture"+Fore.RESET)
time.sleep(5)
print("Search For Operator...")
time.sleep(4)
for i in tqdm(range(10)):

    pass
print(Fore.GREEN+ "Ture"+Fore.RESET)
time.sleep(5)
print("Search For Location...")
time.sleep(4)
for i in tqdm(range(10)):

    pass
print(Fore.GREEN+ "Ture"+Fore.RESET,'\n')
time.sleep(5)
print("Almost Completed...",'\n')
time.sleep(3)
try:
    number = parse(unumber)
    print(" Region/Location:",'\n')
    print(Fore.LIGHTMAGENTA_EX+ geocoder.description_for_number(number,'en')+Fore.RESET)
    print('\n',"Operator:",'\n')
    print(Fore.YELLOW+carrier.name_for_number(number,'en')+Fore.RESET)
except:
    print("Someting Went Wrong")
