import os
from termcolor import colored

def ok():
  dork = open("BEN.txt")
  for i in dork:
    print(i)

os.system('clear')
print(colored("""
___  ____ ____ _  _    ____ ____ _    
|  \ |  | |__/ |_/     [__  |  | |    
|__/ |__| |  \ | \_    ___] |_\| |___ 
                                      
BY BENJAMIN TEAM BABY CYBER MAFIA""", 'blue'))
kimi =input("Mau Ngapain Om/tante/mbak/mas/mbah ?dll mau ngedork? y/n")
if(kimi == "y"):
  ok()
elif(kimi == "n"):
  print(colored("oke kalo tidak",'red'))
else:
  print("INPUT SALAH")