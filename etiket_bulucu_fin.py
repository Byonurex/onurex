import urllib.request
import re
import os

os.system('clear && clear')

print("""

 ____    _    _   _
/ ___|  / \  | | | |
\___ \ / _ \ | |_| |
 ___) / ___ \|  _  |
|____/_/   \_\_| |_|

""")

try:
    #Adresi Aldık
    onurex = input("SAH> ")
    print("60 Saniye içinde cevap gelmezse yeniden deneyiniz !")
    print("\n")

    html = urllib.request.urlopen(onurex)
    html = html.read()
    html = html.decode('utf-8')
    html = str(html)

    #regex ile etiketi belirtelim
    bulucu = "<title>(.*?)</title>"

    ara = re.search(bulucu, html)

    if ara:
        etiket = ara.group(0)

        icerik = ara.group(1)

        print("Etiket: " + etiket + "\n")
        print("İçerik: " + icerik)

    else:
        print("Etiket bulunamadı Hata !!!")

except:
        print("""
        Hata Oluşu 
        Hata Nedenleri...
        Sitenin sonuna / koydunmu ?
        Http / Https Koydunmu ?
        Yanlışmı yazdın ?
        Örnek : http://gmods.ml/
        """)