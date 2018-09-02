import multiprocessing
import time
import sys

print("""

  ___
 / _ \ _ __  _   _ _ __
| | | | '_ \| | | | '__|
| |_| | | | | |_| | |
 \___/|_| |_|\__,_|_|

""")

print("")
print("1. de Alt Alta Verilen sayıları Kopyalarayak Şifrene koya bilirsin zorluk seviyesi orta düzey :)")
print("")
print("2. de sana verilen passwordları deniye bilirsin zorluk seviyesi zor düzey :)")
print("")
Makon = input("[*-*]9 Haneli sifre üretme :)")
adıNJK = input("[*-*]Şifre için nick seç : ")
print("")
def eleman(say):
	print("K/B -->",say)
	return
	
if __name__=="__main__":
	Belirliyici = list()
	for n in range(9):
		mp = multiprocessing.Process(target=eleman, args=(n,))
		Belirliyici.append(mp)
		mp.start()
time.sleep(5)
print("")
time.sleep(5)
print(adıNJK+("38381038194813"))
print(adıNJK+("73882638274828"))
print(adıNJK+("84728472837283"))
print(adıNJK+("738N73K738383E"))
print(adıNJK+("YYK873K76Dk777"))
print(adıNJK+("6383K8348ypls638"))
print(adıNJK+("8384884489493ksl"))