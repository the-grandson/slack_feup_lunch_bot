# Python code to add current script to the registry
# module to edit the windows registry 
# Script copied from: https://www.geeksforgeeks.org/autorun-a-python-script-on-windows-startup/

import winreg as reg 
import getpass
import os
import sys

USER_NAME = getpass.getuser()

def AddToStartup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = "C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup" % (USER_NAME)
    with open(bat_path + '\\' + "launch_lunch_bot.bat", "w+") as bat_file:
        bat_file.write("echo off\n%s %s\\app.py" % (sys.executable,file_path))
 
def AddToRegistry():
 
    # in python __file__ is the instant of
    # file path where it was executed 
    # so if it was executed from desktop,
    # then __file__ will be 
    # c:\users\current_user\desktop
    pth = os.path.dirname(os.path.realpath(__file__))
     
    # name of the python file with extension
    s_name="app.py"    
     
    # joins the file name to end of path address
    address=os.path.join(pth,s_name) 
     
    # key we want to change is HKEY_CURRENT_USER 
    # key value is Software\Microsoft\Windows\CurrentVersion\Run
    key = reg.HKEY_CURRENT_USER
    key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
     
    # open the key to make changes to
    open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS)
     
    # modify the opened key
    reg.SetValueEx(open,"slack_lunch_bot",0,reg.REG_SZ,address)
     
    # now close the opened key
    reg.CloseKey(open)
 
# Driver Code
if __name__=="__main__":
    AddToStartup()
    AddToRegistry()