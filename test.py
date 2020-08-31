from tkinter import *
from PIL import ImageTk, Image

my_test = Tk()
my_test.title("Let's play with me")

canvas = Canvas(my_test, width=525, height=350)
image1 = ImageTk.PhotoImage(Image.open("C:\\School\\mySchoolProject\\Creating PDF\\image2.png"))
background_label = Label(my_test, image=image1)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
canvas.grid()



'''
background_image1 = Image.open("C:\\School\\mySchoolProject\\Creating PDF\\image.jpg")
background_image2 = ImageTk.PhotoImage(background_image1)
w = background_image2.width()
h = background_image2.height()
my_test.geometry('%dx%d+0+0' % (w,h))

'''
'''
label1 = Label(my_test, text="Let's play !", width=20, height=2) 

label1.configure(foreground="red")
label1.configure(background="black")
label1.grid(column=0, row=0)

'''
def game_run2():
	pass

def game_run1():
	label2 = Label(my_test, text="(Saturday, 09:00 a.m) It's time for hiking, you and your friends split into 3 groups")
	label2.configure(fg= "black")
	label2.configure(bg="white")
	label2.configure(height=10)
	label2.grid(column=0, row=0)
	button3 = Button(my_test, text="Press to continue", command=game_run2, bg="red", fg="white")

def game_start():
	button1.grid_forget()
	label1 = Label(my_test, text="(Saturday, 08:00 a.m) Today is the day, you're going to the forest to camp with your friends")
	label1.configure(fg= "black")
	label1.configure(bg="white")
	label1.configure(height=10)
	label1.grid(column=0, row=0)
	button2 = Button(my_test, text="Press to continue", command=game_run1, bg="red", fg="white")
	button2.grid(column=0, row=1)



button1 = Button(my_test, text="Start game", bg="red", fg="white")
button1.grid(column=0, row=0)





if __name__ == "__main__":
	my_test.mainloop()