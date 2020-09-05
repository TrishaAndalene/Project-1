
from json import load, dump
from datetime import datetime
from os import system
import feature
from time import sleep
import pdfmars




time = datetime.now()
print("%s%02d%2d" % (time.year, time.month, time.day))

statusload = feature.loadstat()

if statusload : 
	feature.loginpass()
	sleep(2)
	print("Checking complete ...")
	sleep(2)
	print("Welcome")
	sleep(1.5)
	system('cls')
	print("Unpacking items .")
	sleep(0.5)
	system('cls')
	print("Unpacking items ..")
	sleep(0.5)
	system('cls')
	print("Unpacking items ...")
	sleep(0.5)
	system('cls')
	print("Loading data .")
	sleep(0.5)
	system("cls")
	print("Loading data ..")
	sleep(0.5)
	system('cls')
	print("Loading data ...")
	sleep(1)
	pilih = "0"
	feature.menu()

	while pilih != "Q":
		system('cls')
		feature.menu2()
		pilih = input("Option : ")
		if pilih == "1":
			feature.menu1()
			ch = "0"
			while ch != "Q":
				system('cls')
				feature.menu1()
				ch = input("Option : ")
				if ch == "1":
					feature.itemlist()
				elif ch == "2":
					feature.add()
				elif ch == "3":
					feature.rem()
				elif ch == "4":
					feature.search()
		elif pilih == "2":
			feature.menu3()
			ch = "0"
			while ch != "Q":
				system('cls')
				feature.menu3()
				ch = input("Option : ")
				if ch == "1":
					feature.cel()
					pil = "0"
					while pil != "4":
						system('cls')
						feature.cel()
						pil = input("Option : ")
						if pil == "1":
							feature.cel1()
						elif pil == "2":
							feature.cel2()
						elif pil == "3":
							feature.cel3()

				elif ch == "2":
					feature.rea()
					pil = "0"
					while pil != "4":
						system('cls')
						feature.rea()
						pil = input("Option : ")
						if pil == "1":
							feature.rea1()
						elif pil == "2":
							feature.rea2()
						elif pil == "3":
							feature.rea3()

				elif ch == "3":
					feature.far()
					pil = "0"
					while pil != "4":
						system('cls')
						feature.far()
						pil = input("Option : ")
						if pil == "1":
							feature.far1()
						elif pil == "2":
							feature.far2()
						elif pil == "3":
							feature.far3()

				elif ch == "4":
					feature.kel()
					pil = "0"
					while pil != "4":
						system('cls')
						feature.kel()
						pil = input("Option : ")
						if pil == "1":
							feature.kel1()
						elif pil == "2":
							feature.kel2()
						elif pil == "3":
							feature.kel3()

		elif pilih == "3":
			feature.planetarium()
			feature.pdf()
			a = "0"
			while a != "x":
				system('cls')
				feature.pdf()
				a = input("Download : ")
				if a == "1":
					pdfmars.merkurius()
				elif a =="2":
					pdfmars.venus()
				elif a == "3":
					pdfmars.Earth()
				elif a == "4":
					pdfmars.mars()
				elif a == "5":
					pdfmars.jupiter()
				elif a == "6":
					pdfmars.saturnus()
				elif a == "7":
					pdfmars.uranus()
				elif a == "8":
					pdfmars.neptunus()
				elif a == "9":
					pdfmars.LkCa()
				elif a =="10":
					pdfmars.WASP()
				elif a =="11":
					pdfmars.Osiris()
				elif a == "12":
					pdfmars.Kepler()
				elif a == "13":
					pdfmars.Cancri()
				elif a =="14":
					pdfmars.trappist()

	
	if pilih == "Q":
		system('cls')
		print("Closing application .")
		sleep(0.5)
		system('cls')
		print("Closing application ..")
		sleep(0.5)
		system('cls')
		print("Closing application ...")
		sleep(0.5)
		system('cls')
			
else:
	print("Apps is not responding ..")

