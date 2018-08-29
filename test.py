import sys
import time
import os
from urllib2 import *
from platform import system

def http():
	print
	print
	os.system("toilet -f pagga 'Http Header       ' | lolcat")
	time.sleep(1)
	print
	os.system("curl https://api.hackertarget.com/httpheaders/?q=" + ip)
	print(" ")