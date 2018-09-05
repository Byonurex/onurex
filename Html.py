import urllib.request
import time

print("""
1. Http / Https Yazmayı unutma :)
2. Site urlsinin sonuna / koyma :)

""")

s = input("Site : ")
print("")
time.sleep(2)
x = urllib.request.urlopen(s)

print (x.read())