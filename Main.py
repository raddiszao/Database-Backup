import ftplib, time, threading, os, sys
from urllib.request import Request, urlopen
import urllib.request
import ssl
import os, subprocess
from datetime import datetime
username = ""
hostname = ""
password = ""
database = ""

class Update:
    def __init__(self):
        self.count = 1
        self.session = ftplib.FTP('','','')
        print("%s - Database backup initialized." %(datetime.now().strftime("%H:%M:%S")))
        self.update()
    
    def update(self):
        databaseFile = "heibbo_" + str(time.time()) + str(".sql")
        with open(databaseFile,'w') as output:
            c = subprocess.Popen(['mysqldump', '-u',username,'-p%s'%password,database], stdout=output, shell=True)
            time.sleep(10)
            file = open(databaseFile, 'rb')                  # file to send
            self.session.storbinary('STOR public_html/databases/' + str(databaseFile), file)     # send the file
            print("%s - Database %s backup successfully send." %(datetime.now().strftime("%H:%M:%S"), databaseFile))
            file.close()

Update()
