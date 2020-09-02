from reportlab.pdfgen import canvas
from os import system
from time import sleep

def mars():
	dataSiswa = {
		"nama" : "Planet ",
		"kelas" : "Mars",
		"laporan" : ""
	}

	class Data:

		def __init__(self, filename, documentTitle, heading):
			self.filename = filename
			self.documentTitle = documentTitle
			self.heading = heading
			self.info = """
			"""

	myData = Data(str(dataSiswa["nama"]+dataSiswa["kelas"]+".pdf"), "Planet", dataSiswa['laporan'])
	myPdf = canvas.Canvas(myData.filename)
	myPdf.setTitle(myData.documentTitle)

	#print on paper pdf
	myPdf.drawString(230, 810, myData.heading)#tengahnya 225,400

	myPdf.setFont("Times-Roman", 30)
	myPdf.setFillColorRGB(0,0,0)
	myPdf.drawString(260, 770, "Mars" )
	myPdf.line(30, 760, 560, 760)#(x1, y1, x2, y2)


	myText = myPdf.beginText(40, 720)
	myText.setFont("Times-Roman", 13)

	Lines = ["Planet information : ", "Name : Mars ", "Famous color : Red or Brown", "Diametre : 6779 km", "Satelite : Phobos & Deimos", "Description :", "The fourth planet from the sun, usually called the Red Planet because of its color which look", "like blood. The name 'Mars' was taken from a greek god of war, Ares", "The satelites' names were taken from his sons, Phobos means “fear,” and Deimos means 'panic'.", "Picture : "]
	for line in Lines:
		myText.textLine(line)
	myPdf.drawText(myText)

	myPdf.drawInlineImage("mars.jfif", 150, 290)
	saving()
	myPdf.save()

def Earth():
	from reportlab.pdfgen import canvas

	dataSiswa = {
		"nama" : "Planet ",
		"kelas" : "Earth",
		"laporan" : ""
	}

	class Data:

		def __init__(self, filename, documentTitle, heading):
			self.filename = filename
			self.documentTitle = documentTitle
			self.heading = heading
			self.info = """
			"""

	myData = Data(str(dataSiswa["nama"]+dataSiswa["kelas"]+".pdf"), "Planet", dataSiswa['laporan'])
	myPdf = canvas.Canvas(myData.filename)
	myPdf.setTitle(myData.documentTitle)

	#print on paper pdf
	myPdf.drawString(230, 810, myData.heading)#tengahnya 225,400

	myPdf.setFont("Times-Roman", 30)
	myPdf.setFillColorRGB(0,0,0)
	myPdf.drawString(250, 770, "Earth" )
	myPdf.line(30, 760, 560, 760)#(x1, y1, x2, y2)


	myText = myPdf.beginText(40, 720)
	myText.setFont("Times-Roman", 13)

	Lines = ["Planet information : ", "Name : Earth", "Famous color : Green & Blue", "Diametre : 12.472 km", "Satelite : Moon", "Description :", "The only planet where humans can life without any technology and the fourth planet from the sun", "Picture :"]
	for line in Lines:
		myText.textLine(line)
	myPdf.drawText(myText)

	myPdf.drawInlineImage("bumi2.png", 95, 330)
	saving()
	myPdf.save()
	

def merkurius():
	from reportlab.pdfgen import canvas

	dataSiswa = {
		"nama" : "Planet ",
		"kelas" : "Mercury",
		"laporan" : ""
	}

	class Data:

		def __init__(self, filename, documentTitle, heading):
			self.filename = filename
			self.documentTitle = documentTitle
			self.heading = heading
			self.info = """
			"""

	myData = Data(str(dataSiswa["nama"]+dataSiswa["kelas"]+".pdf"), "Planet", dataSiswa['laporan'])
	myPdf = canvas.Canvas(myData.filename)
	myPdf.setTitle(myData.documentTitle)

	#print on paper pdf
	myPdf.drawString(230, 810, myData.heading)#tengahnya 225,400

	myPdf.setFont("Times-Roman", 30)
	myPdf.setFillColorRGB(0,0,0)
	myPdf.drawString(240, 770, "Mercury" )
	myPdf.line(30, 760, 560, 760)#(x1, y1, x2, y2)


	myText = myPdf.beginText(40, 720)
	myText.setFont("Times-Roman", 13)

	Lines = ["Planet information : ", "Name : Mercury", "Famous color : dark gray", "Diametre : 4.879,4 km", "Satelite : none", "Description :", "The closest planet to the sun, the surface was rocky and the smallest planet in","solar system. The name 'Mercury' was taken from a Roman God, Mercury, the god of travelers","because of its speed to circle the sun.", "Picture :"]
	for line in Lines:
		myText.textLine(line)
	myPdf.drawText(myText)

	myPdf.drawInlineImage("mercury.jpg", 95, 330)
	saving()
	myPdf.save()
	

def venus():
	from reportlab.pdfgen import canvas

	dataSiswa = {
		"nama" : "Planet ",
		"kelas" : "Venus",
		"laporan" : ""
	}

	class Data:

		def __init__(self, filename, documentTitle, heading):
			self.filename = filename
			self.documentTitle = documentTitle
			self.heading = heading
			self.info = """
			"""

	myData = Data(str(dataSiswa["nama"]+dataSiswa["kelas"]+".pdf"), "Planet", dataSiswa['laporan'])
	myPdf = canvas.Canvas(myData.filename)
	myPdf.setTitle(myData.documentTitle)

	#print on paper pdf
	myPdf.drawString(230, 810, myData.heading)#tengahnya 225,400

	myPdf.setFont("Times-Roman", 30)
	myPdf.setFillColorRGB(0,0,0)
	myPdf.drawString(250, 770, "Venus" )
	myPdf.line(30, 760, 560, 760)#(x1, y1, x2, y2)


	myText = myPdf.beginText(40, 720)
	myText.setFont("Times-Roman", 13)

	Lines = ["Planet information : ", "Name : Venus", "Famous color : brown (the true color is white)", "Diametre : 12.104 km", "Satelite : none", "Description :", "The second closest planet to the sun, this planet is much bigger than mercury",". This planet was named after a Roman Goddess of love and beauty, also the only planet ","that named after a woman. The planet was named Venus because that's one of the five planets that ","shine so bright from what the ancient people knew", "Picture :"]
	for line in Lines:
		myText.textLine(line)
	myPdf.drawText(myText)

	myPdf.drawInlineImage("venus.jpg", 95, 300)
	saving()
	myPdf.save()
	

def jupiter():
	from reportlab.pdfgen import canvas

	dataSiswa = {
		"nama" : "Planet ",
		"kelas" : "Jupiter",
		"laporan" : ""
	}
	

	class Data:

		def __init__(self, filename, documentTitle, heading):
			self.filename = filename
			self.documentTitle = documentTitle
			self.heading = heading
			self.info = """
			"""

	myData = Data(str(dataSiswa["nama"]+dataSiswa["kelas"]+".pdf"), "Planet", dataSiswa['laporan'])
	myPdf = canvas.Canvas(myData.filename)
	myPdf.setTitle(myData.documentTitle)

	#print on paper pdf
	myPdf.drawString(230, 810, myData.heading)#tengahnya 225,400

	myPdf.setFont("Times-Roman", 30)
	myPdf.setFillColorRGB(0,0,0)
	myPdf.drawString(240, 770, "Jupiter" )
	myPdf.line(30, 760, 560, 760)#(x1, y1, x2, y2)


	myText = myPdf.beginText(40, 720)
	myText.setFont("Times-Roman", 13)

	Lines = ["Planet information : ", "Name : Jupiter", "Famous color : white, red, orange, brown, and yellow", "Diametre : 139.820 km", "Satelite : 4 Galileo Satelite, 72 more", "Description :", "The biggest planet in the solar system, the fifth planet from the sun","Jupiter has around 76 satelites which were orbiting it. Jupiter was known as a gas giant planet. It"," also the third brightest planet after moon and venus." ,"Picture :"]
	for line in Lines:
		myText.textLine(line)
	myPdf.drawText(myText)

	myPdf.drawInlineImage("jupiter.jpg", 95, 330)
	saving()
	myPdf.save()


def saturnus():
	from reportlab.pdfgen import canvas

	dataSiswa = {
		"nama" : "Planet ",
		"kelas" : "Saturn",
		"laporan" : ""
	}
	

	class Data:

		def __init__(self, filename, documentTitle, heading):
			self.filename = filename
			self.documentTitle = documentTitle
			self.heading = heading
			self.info = """
			"""

	myData = Data(str(dataSiswa["nama"]+dataSiswa["kelas"]+".pdf"), "Planet", dataSiswa['laporan'])
	myPdf = canvas.Canvas(myData.filename)
	myPdf.setTitle(myData.documentTitle)

	#print on paper pdf
	myPdf.drawString(230, 810, myData.heading)#tengahnya 225,400

	myPdf.setFont("Times-Roman", 30)
	myPdf.setFillColorRGB(0,0,0)
	myPdf.drawString(243, 770, "Saturn" )
	myPdf.line(30, 760, 560, 760)#(x1, y1, x2, y2)


	myText = myPdf.beginText(40, 720)
	myText.setFont("Times-Roman", 13)

	Lines = ["Planet information : ", "Name : Saturn", "Famous color : pale yellow with hint of orange", "Diametre : 116.460 km", "Satelite : Titan and 81 more", "Description :", "The sixth planet from the sun and the second largest planet in the solar system","Saturn has the most moons or satelite than any other planet. Saturn is the only planet which ring(asteroid) ","can be clearly seen using telescope" ,"Picture :"]
	for line in Lines:
		myText.textLine(line)
	myPdf.drawText(myText)

	myPdf.drawInlineImage("saturn.jpg", 50, 270)
	saving()
	myPdf.save()


def uranus():
	from reportlab.pdfgen import canvas

	dataSiswa = {
		"nama" : "Planet ",
		"kelas" : "Uranus",
		"laporan" : ""
	}
	

	class Data:

		def __init__(self, filename, documentTitle, heading):
			self.filename = filename
			self.documentTitle = documentTitle
			self.heading = heading
			self.info = """
			"""

	myData = Data(str(dataSiswa["nama"]+dataSiswa["kelas"]+".pdf"), "Planet", dataSiswa['laporan'])
	myPdf = canvas.Canvas(myData.filename)
	myPdf.setTitle(myData.documentTitle)

	#print on paper pdf
	myPdf.drawString(230, 810, myData.heading)#tengahnya 225,400

	myPdf.setFont("Times-Roman", 30)
	myPdf.setFillColorRGB(0,0,0)
	myPdf.drawString(245, 770, "Uranus" )
	myPdf.line(30, 760, 560, 760)#(x1, y1, x2, y2)


	myText = myPdf.beginText(40, 720)
	myText.setFont("Times-Roman", 13)

	Lines = ["Planet information : ", "Name : Uranus", "Famous color : light blue", "Diametre : 50.724 km", "Satelite : Miranda, Ariel, Umbriel, Titania, Oberon and 22 more", "Description :", "The seventh planet from the sun and sometimes people call it the twin with neptunus",". It's also the fourth largest mass from all planet, the name 'Uranus' was taken from a ","Greek God, Uranus" ,"Picture :"]
	for line in Lines:
		myText.textLine(line)
	myPdf.drawText(myText)

	myPdf.drawInlineImage("uranus.jfif", 95, 360)
	saving()
	myPdf.save()
	

def neptunus():
	from reportlab.pdfgen import canvas

	dataSiswa = {
		"nama" : "Planet ",
		"kelas" : "Neptunus",
		"laporan" : ""
	}
	

	class Data:

		def __init__(self, filename, documentTitle, heading):
			self.filename = filename
			self.documentTitle = documentTitle
			self.heading = heading
			self.info = """
			"""

	myData = Data(str(dataSiswa["nama"]+dataSiswa["kelas"]+".pdf"), "Planet", dataSiswa['laporan'])
	myPdf = canvas.Canvas(myData.filename)
	myPdf.setTitle(myData.documentTitle)

	#print on paper pdf
	myPdf.drawString(230, 810, myData.heading)#tengahnya 225,400

	myPdf.setFont("Times-Roman", 30)
	myPdf.setFillColorRGB(0,0,0)
	myPdf.drawString(240, 770, "Neptunus" )
	myPdf.line(30, 760, 560, 760)#(x1, y1, x2, y2)


	myText = myPdf.beginText(40, 720)
	myText.setFont("Times-Roman", 13)

	Lines = ["Planet information : ", "Name : Neptune", "Famous color : dark blue", "Diametre : 49.244 km", "Satelite : Triton, Thalassa and 15 more", "Description :", "The farthest planet to the sun, sometimes called as a twin with uranus because they look alike",". This planet has the third largest mass from all planet in solar system and around","17 times bigger than earth", "Picture :"]
	for line in Lines:
		myText.textLine(line)
	myPdf.drawText(myText)

	myPdf.drawInlineImage("neptune.jpg", 70, 250)
	saving()
	myPdf.save()


def LkCa():
	from reportlab.pdfgen import canvas

	dataSiswa = {
		"nama" : "Exoplanet ",
		"kelas" : "LkCa 15 b",
		"laporan" : ""
	}
	

	class Data:

		def __init__(self, filename, documentTitle, heading):
			self.filename = filename
			self.documentTitle = documentTitle
			self.heading = heading
			self.info = """
			"""

	myData = Data(str(dataSiswa["nama"]+dataSiswa["kelas"]+".pdf"), "Planet", dataSiswa['laporan'])
	myPdf = canvas.Canvas(myData.filename)
	myPdf.setTitle(myData.documentTitle)

	#print on paper pdf
	myPdf.drawString(230, 810, myData.heading)#tengahnya 225,400

	myPdf.setFont("Times-Roman", 30)
	myPdf.setFillColorRGB(0,0,0)
	myPdf.drawString(220, 770, "LkCa 15 b" )
	myPdf.line(30, 760, 560, 760)#(x1, y1, x2, y2)


	myText = myPdf.beginText(40, 720)
	myText.setFont("Times-Roman", 13)

	Lines = ["Planet information : ", "Planet type : Young Gas giant", "Constellation : Taurus-Auriga Star Forming Region", "Distance : 430 light years", "Temperature : -5000°C", "Mass : 1908 M⊕", "Observation speed : x 1000","Description : "," this planet has a disk, a left over dust, over it. The dust can be collide or stick together","in the disk. The core of the planet is called 'planetesimal'. ", "Picture :"]
	for line in Lines:
		myText.textLine(line)
	myPdf.drawText(myText)

	myPdf.drawInlineImage("LkCa 15 b.jpg", 70, 300)
	saving()
	myPdf.save()
		

def WASP():
	from reportlab.pdfgen import canvas

	dataSiswa = {
		"nama" : "Exoplanet ",
		"kelas" : "WASP-121b",
		"laporan" : ""
	}
	

	class Data:

		def __init__(self, filename, documentTitle, heading):
			self.filename = filename
			self.documentTitle = documentTitle
			self.heading = heading
			self.info = """
			"""

	myData = Data(str(dataSiswa["nama"]+dataSiswa["kelas"]+".pdf"), "Planet", dataSiswa['laporan'])
	myPdf = canvas.Canvas(myData.filename)
	myPdf.setTitle(myData.documentTitle)

	#print on paper pdf
	myPdf.drawString(230, 810, myData.heading)#tengahnya 225,400

	myPdf.setFont("Times-Roman", 30)
	myPdf.setFillColorRGB(0,0,0)
	myPdf.drawString(220, 770, "WASP-121b" )
	myPdf.line(30, 760, 560, 760)#(x1, y1, x2, y2)


	myText = myPdf.beginText(40, 720)
	myText.setFont("Times-Roman", 13)

	Lines = ["Planet information : ", "Planet type : Hot Jupiter", "Constellation : Puppis", "Distance : 880 light years", "Temperature : 2500°C", "Mass : 376 M⊕", "Observation speed : x 5000","Description : ","Hot jupiter is gas giant exoplanet, but it much much closer orbit to its star","When day time, the temperature could reach thousand of degrees Kelvin which cause a lot of","contrast between day and night time in temperature.", "Picture :"]
	for line in Lines:
		myText.textLine(line)
	myPdf.drawText(myText)

	myPdf.drawInlineImage("WASP-121b.jpg", 70, 330)
	saving()
	myPdf.save()
		

def Osiris():
	from reportlab.pdfgen import canvas

	dataSiswa = {
		"nama" : "Exoplanet ",
		"kelas" : "Osiris",
		"laporan" : ""
	}
	

	class Data:

		def __init__(self, filename, documentTitle, heading):
			self.filename = filename
			self.documentTitle = documentTitle
			self.heading = heading
			self.info = """
			"""

	myData = Data(str(dataSiswa["nama"]+dataSiswa["kelas"]+".pdf"), "Planet", dataSiswa['laporan'])
	myPdf = canvas.Canvas(myData.filename)
	myPdf.setTitle(myData.documentTitle)

	#print on paper pdf
	myPdf.drawString(230, 810, myData.heading)#tengahnya 225,400

	myPdf.setFont("Times-Roman", 30)
	myPdf.setFillColorRGB(0,0,0)
	myPdf.drawString(220, 770, "Osiris" )
	myPdf.line(30, 760, 560, 760)#(x1, y1, x2, y2)


	myText = myPdf.beginText(40, 720)
	myText.setFont("Times-Roman", 13)

	Lines = ["Planet information : ", "Planet type : Hot Jupiter", "Constellation : Pegasus", "Distance : 154 light years", "Temperature : 1130°C", "Mass : 226 M⊕", "Observation speed : real time","Description : "," Known as HD209458b, the planet has a very strong wind, going from the west to east. The wind's","speed is almost 5 km per seconds, which is about ten times faster than concorde. ", "Because of the temperature, it is really possible for it to rain molten iron, silicates, or even glass","Picture :"]
	for line in Lines:
		myText.textLine(line)
	myPdf.drawText(myText)

	myPdf.drawInlineImage("osiris.jpeg", 70, 300)
	saving()
	myPdf.save()
	

def Kepler():
	from reportlab.pdfgen import canvas

	dataSiswa = {
		"nama" : "Exoplanet ",
		"kelas" : "Kepler-62e",
		"laporan" : ""
	}
	

	class Data:

		def __init__(self, filename, documentTitle, heading):
			self.filename = filename
			self.documentTitle = documentTitle
			self.heading = heading
			self.info = """
			"""

	myData = Data(str(dataSiswa["nama"]+dataSiswa["kelas"]+".pdf"), "Planet", dataSiswa['laporan'])
	myPdf = canvas.Canvas(myData.filename)
	myPdf.setTitle(myData.documentTitle)

	#print on paper pdf
	myPdf.drawString(230, 810, myData.heading)#tengahnya 225,400

	myPdf.setFont("Times-Roman", 30)
	myPdf.setFillColorRGB(0,0,0)
	myPdf.drawString(220, 770, "Kepler-62e" )
	myPdf.line(30, 760, 560, 760)#(x1, y1, x2, y2)


	myText = myPdf.beginText(40, 720)
	myText.setFont("Times-Roman", 13)

	Lines = ["Planet information : ", "Planet type : Super Earth", "Constellation : Lyra", "Distance : 1200 light years", "Temperature : -3°C", "Mass : 4,5 M⊕", "Observation speed : real time","Description : ","The super earth is a type of planet which have thicker atmosphere and stronger gravity than Earth.","This type of form is really common in the galaxy which size is around neptune or earth. ","This planet has a huge ocean in which because of the pressure it makes the waves really high. ","(known as Water World)", "Picture :"]
	for line in Lines:
		myText.textLine(line)
	myPdf.drawText(myText)

	myPdf.drawInlineImage("kepler-62e.jfif", 70, 300)
	saving()
	myPdf.save()	
	

def Cancri():
	from reportlab.pdfgen import canvas

	dataSiswa = {
		"nama" : "Exoplanet ",
		"kelas" : "55 Cancri e",
		"laporan" : ""
	}
	

	class Data:

		def __init__(self, filename, documentTitle, heading):
			self.filename = filename
			self.documentTitle = documentTitle
			self.heading = heading
			self.info = """
			"""

	myData = Data(str(dataSiswa["nama"]+dataSiswa["kelas"]+".pdf"), "Planet", dataSiswa['laporan'])
	myPdf = canvas.Canvas(myData.filename)
	myPdf.setTitle(myData.documentTitle)

	#print on paper pdf
	myPdf.drawString(230, 810, myData.heading)#tengahnya 225,400

	myPdf.setFont("Times-Roman", 30)
	myPdf.setFillColorRGB(0,0,0)
	myPdf.drawString(220, 770, "55 Cancri e" )
	myPdf.line(30, 760, 560, 760)#(x1, y1, x2, y2)


	myText = myPdf.beginText(40, 720)
	myText.setFont("Times-Roman", 13)

	Lines = ["Planet information : ", "Planet type : Super Earth", "Constellation : Cancer", "Distance : 40 light years", "Temperature : 1700°C", "Mass : 8.6 M⊕", "Observation speed : real time","Description : "," The planet has around thousands degrees of Kelvin or in Celcius, so this planet is","incredibly hot and has a very strong gravitional field. This planet has a lot of lava which make the surface destroyed ","which make it possible that the atmosphere contains metal-rock fro the surface and rain silicates", "Picture :"]
	for line in Lines:
		myText.textLine(line)
	myPdf.drawText(myText)

	myPdf.drawInlineImage("cancri.jpg", 70, 300)
	saving()
	myPdf.save()	
	

def trappist():
	from reportlab.pdfgen import canvas

	dataSiswa = {
		"nama" : "Exoplanet ",
		"kelas" : "TRAPPIST-1e",
		"laporan" : ""
	}
	

	class Data:

		def __init__(self, filename, documentTitle, heading):
			self.filename = filename
			self.documentTitle = documentTitle
			self.heading = heading
			self.info = """
			"""

	myData = Data(str(dataSiswa["nama"]+dataSiswa["kelas"]+".pdf"), "Planet", dataSiswa['laporan'])
	myPdf = canvas.Canvas(myData.filename)
	myPdf.setTitle(myData.documentTitle)

	#print on paper pdf
	myPdf.drawString(230, 810, myData.heading)#tengahnya 225,400

	myPdf.setFont("Times-Roman", 30)
	myPdf.setFillColorRGB(0,0,0)
	myPdf.drawString(220, 770, "TRAPPIST-1e" )
	myPdf.line(30, 760, 560, 760)#(x1, y1, x2, y2)


	myText = myPdf.beginText(40, 720)
	myText.setFont("Times-Roman", 13)

	Lines = ["Planet information : ", "Planet type : Terestial", "Constellation : Aquarius", "Distance : 40 light years", "Temperature : -21.8°C", "Mass : 0.62 M⊕", "Observation speed : real time","Description : "," This planet and the six other also orbiting a star and have the fairly size of Earth, which ","made it look like a miniature of the solar system. This star size was alike with the Jupiter's ","This system can cause the planet become close to the sun in some point", "Picture :"]
	for line in Lines:
		myText.textLine(line)
	myPdf.drawText(myText)

	myPdf.drawInlineImage("trappist.jpg", 70, 350)
	saving()
	myPdf.save()
	

def saving():
	system('cls')	
	n = 0
	print("Dowloading pdf 0 %")
	sleep(0.5)
	while n != 100:
		system('cls')
		n += 1
		print("Dowloading pdf", (n), " %")

	system('cls')
	print("Complete 100 %")
	sleep(0.5)