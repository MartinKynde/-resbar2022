import matplotlib
import numpy
from numpy import ndarray

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style, pyplot as plt

import tkinter as tk
from tkinter import ttk
from itertools import cycle
from PIL import ImageTk, Image

LARGE_FONT = ("Verdana", 12)
style.use("dark_background")

from matplotlib import *
f = Figure(figsize=(12, 6), dpi=100)

f.suptitle("Børsbar 2022",fontsize=35)
a = f.add_subplot(111)
#gs = matplotlib.gridspec.GridSpec(2, 3)
#a = f.add_subplot(gs[0,0])
#b = f.add_subplot(gs[0,1])
#c = f.add_subplot(gs[0,-1])
#a1 = f.add_subplot(gs[1,0])
#b1 = f.add_subplot(gs[1,1])
#c1 = f.add_subplot(gs[1,-1])
#image = f.add_subplot(gs[2,:])

data1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0]
data2 = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45 ,50, 55, 60]
data3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0]
data4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0]
data5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0]
data6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0]

time = 60

import matplotlib.image as mpimg

def simple_interest(p, r, t):
    si=(p*r*t)/1000
    a= p+si

    return a

p = 1000
t = 5
# animation function
def animate(self):
    firstyear = open('FirstYear.txt', 'r').read()
    lines = firstyear.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            y = float(y)
            y = simple_interest(p, 1*y, 1)
          #  xs.append(float(x))
            xs.append(x)
            ys.append(float(y))
    a.clear()
    a.plot(xs, ys, color="blue", linewidth=2, marker='o')



    #  a.set_title("First Year")


    secondyear = open('SecondYear.txt', 'r').read()
    lines1 = secondyear.split('\n')
    xs1 = []
    ys1 = []
    for line in lines1:
        if len(line) > 1:
            x1, y1 = line.split(',')
            y1 = float(y1)
            y1 = simple_interest(p, 1 * y1, 1)
            xs1.append(x1)
            ys1.append(float(y1))
   # a.clear()
    a.plot(xs1, ys1, color="green", linewidth=2, marker='o')
   # a.set_title("Second Year")


    thirdyear = open('ThirdYear.txt', 'r').read()
    lines2 = thirdyear.split('\n')
    xs2 = []
    ys2 = []
    for line in lines2:
        if len(line) > 1:
            x2, y2 = line.split(',')
            y2 = float(y2)
            y2 = simple_interest(p, 1 * y2, 1)
            xs2.append(x2)
            ys2.append(float(y2))
  #  a.clear()
    a.plot(xs2, ys2, color="purple", linewidth=2, marker='o')
    #c.set_title("Third Year")


    fourthyear = open('FourthYear.txt', 'r').read()
    lines3 = fourthyear.split('\n')
    xs3 = []
    ys3 = []
    for line in lines3:
        if len(line) > 1:
            x3, y3 = line.split(',')
            y3 = float(y3)
            y3 = simple_interest(p, 1 * y3, 1)
            xs3.append(x3)
            ys3.append(float(y3))
   # a.clear()
    a.plot(xs3, ys3,  color="orange", linewidth=2, marker='o')
    #a1.set_title("Fourth Year")


    fifthyear = open('FifthYear.txt', 'r').read()
    lines4 = fifthyear.split('\n')
    xs4 = []
    ys4 = []
    for line in lines4:
        if len(line) > 1:
            x4, y4 = line.split(',')
            y4 = float(y4)
            y4 = simple_interest(p, 1 * y4, 1)
            xs4.append(x4)
            ys4.append(float(y4))
   # a.clear()
    a.plot(xs4, ys4, linewidth=2, marker='o')
   # b1.set_title("Fifth Year")

    phdansatte = open('PhdAnsatte.txt', 'r').read()
    lines5 = phdansatte.split('\n')
    xs5 = []
    ys5 = []
    for line in lines5:
        if len(line) > 1:
            x5, y5 = line.split(',')
            y5 = float(y5)
            y5 = simple_interest(p, 1 * y5, 1)
            xs5.append(x5)
            ys5.append(float(y5))
#    a.clear(
    a.plot(xs5, ys5, color="pink", linewidth=2, marker='o')
    a.legend(["First Year", "Second Year", "Third Year", "Fourth Year", "Fifth Year",
              "PhD + Employees"], loc= 'lower center', bbox_to_anchor=(0.5, -0.1), ncol=6, prop={'size': 16})
    #c1.set_title("PhD & Employees")



class Børsbar(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

#        tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "Børsbar 2022")
        tk.Tk.attributes(self, "-fullscreen",True)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage,  PageThree, Disaster1, Disaster2, Disaster3):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Børsbar 2022", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        button3 = ttk.Button(self, text="Aktieportefølje",
                             command=lambda: controller.show_frame(PageThree))
        button3.pack()

        def clear_text():
            file = open("FirstYear.txt", "w")
            file.close()
            file = open("SecondYear.txt", "w")
            file.close()
            file = open("ThirdYear.txt", "w")
            file.close()
            file = open("FourthYear.txt", "w")
            file.close()
            file = open("FifthYear.txt", "w")
            file.close()
            file = open("PhdAnsatte.txt", "w")
            file.close()
import sys
import time

firstbeer = []
firstbeer2 = []
firstbeer3 = []
firstbeer4 = []
firstbeer5 = []
firstbeer6 = []

firsttemp = 0
firsttemp2 = 0
firsttemp3 = 0
firsttemp4 = 0
firsttemp5 = 0
firsttemp6 = 0

import datetime
import numpy as np
import itertools
def NedtaelOel():
        global firsttemp
        firsttemp += 1
        firstbeer = firsttemp
        content = str(datetime.datetime.now())
        content3 = content[slice(11, 16)]
        content2 = str(firstbeer)
        content2 = content3 + ", " + content2
        textfile = open("FirstYear.txt","a")
        textfile.write(str(content2) + "\n")
        textfile.close()


def OptaelOel():
    global firsttemp
    firsttemp -= 1
    firstbeer = firsttemp
    content = str(datetime.datetime.now())
    content3 = content[slice(11, 16)]
    content2 = str(firstbeer)
    content2 = content3 + ", " + content2
    textfile = open("FirstYear.txt", "a")
    textfile.write(str(content2) + "\n")
    textfile.close()


def NedtaelOel2():
    global firsttemp2
    firsttemp2 += 1
    firstbeer2 = firsttemp2
    content = str(datetime.datetime.now())
    content3 = content[slice(11, 16)]
    content2 = str(firstbeer2)
    content2 = content3 + ", " + content2
    textfile = open("SecondYear.txt", "a")
    textfile.write(str(content2) + "\n")
    textfile.close()

def OptaelOel2():
    global firsttemp2
    firsttemp2 -= 1
    firstbeer2 = firsttemp2
    content = str(datetime.datetime.now())
    content3 = content[slice(11, 16)]
    content2 = str(firstbeer2)
    content2 = content3 + ", " + content2
    textfile = open("SecondYear.txt", "a")
    textfile.write(str(content2) + "\n")
    textfile.close()

def NedtaelOel3():
    global firsttemp3
    firsttemp3 += 1
    firstbeer3 = firsttemp3
    content = str(datetime.datetime.now())
    content3 = content[slice(11, 16)]
    content2 = str(firstbeer3)
    content2 = content3 + ", " + content2
    textfile = open("ThirdYear.txt", "a")
    textfile.write(str(content2) + "\n")
    textfile.close()

def OptaelOel3():
    global firsttemp3
    firsttemp3 -= 1
    firstbeer3 = firsttemp3
    content = str(datetime.datetime.now())
    content3 = content[slice(11, 16)]
    content2 = str(firstbeer3)
    content2 = content3 + ", " + content2
    textfile = open("ThirdYear.txt", "a")
    textfile.write(str(content2) + "\n")
    textfile.close()

def NedtaelOel4():
    global firsttemp4
    firsttemp4 += 1
    firstbeer4 = firsttemp4
    content = str(datetime.datetime.now())
    content3 = content[slice(11, 16)]
    content2 = str(firstbeer4)
    content2 = content3 + ", " + content2
    textfile = open("FourthYear.txt", "a")
    textfile.write(str(content2) + "\n")
    textfile.close()

def OptaelOel4():
    global firsttemp4
    firsttemp4 -= 1
    firstbeer4 = firsttemp4
    content = str(datetime.datetime.now())
    content3 = content[slice(11, 16)]
    content2 = str(firstbeer4)
    content2 = content3 + ", " + content2
    textfile = open("FourthYear.txt", "a")
    textfile.write(str(content2) + "\n")
    textfile.close()

def NedtaelOel5():
    global firsttemp5
    firsttemp5 += 1
    firstbeer5 = firsttemp5
    content = str(datetime.datetime.now())
    content3 = content[slice(11, 16)]
    content2 = str(firstbeer5)
    content2 = content3 + ", " + content2
    textfile = open("FifthYear.txt", "a")
    textfile.write(str(content2) + "\n")
    textfile.close()

def OptaelOel5():
    global firsttemp5
    firsttemp5 -= 1
    firstbeer5 = firsttemp5
    content = str(datetime.datetime.now())
    content3 = content[slice(11, 16)]
    content2 = str(firstbeer5)
    content2 = content3 + ", " + content2
    textfile = open("FifthYear.txt", "a")
    textfile.write(str(content2) + "\n")
    textfile.close()

def NedtaelOel6():
    global firsttemp6
    firsttemp6 += 1
    firstbeer6 = firsttemp6
    content = str(datetime.datetime.now())
    content3 = content[slice(11, 16)]
    content2 = str(firstbeer6)
    content2 = content3 + ", " + content2
    textfile = open("PhdAnsatte.txt", "a")
    textfile.write(str(content2) + "\n")
    textfile.close()

def OptaelOel6():
    global firsttemp6
    firsttemp6 -= 1
    firstbeer6 = firsttemp6
    content = str(datetime.datetime.now())
    content3 = content[slice(11, 16)]
    content2 = str(firstbeer6)
    content2 = content3 + ", " + content2
    textfile = open("PhdAnsatte.txt", "a")
    textfile.write(str(content2) + "\n")
    textfile.close()

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self) #text="Aktier", font=LARGE_FONT
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button1.place(x=100, y=15)

        buttonfirstyear = tk.Button(self,text="First Year", bg='green', command=NedtaelOel)
        buttonfirstyear.pack()
        buttonfirstyear.place(x= 800, y=0)

        buttonfirstyearned = tk.Button(self, text="First Year", bg='red', command=OptaelOel)
        buttonfirstyearned.pack()
        buttonfirstyearned.place(x=800, y=20)

        button2year = tk.Button(self, text="Second Year", bg='green', command=NedtaelOel2)
        button2year.pack()
        button2year.place(x=900, y=0)

        button2yearned = tk.Button(self, text="Second Year", bg='red', command=OptaelOel2)
        button2yearned.pack()
        button2yearned.place(x=900, y=20)

        button3year = tk.Button(self, text="Third Year",bg='green', command=NedtaelOel3)
        button3year.pack()
        button3year.place(x=1000, y=0)

        button3yearned = tk.Button(self, text="Third Year", bg='red', command=OptaelOel3)
        button3yearned.pack()
        button3yearned.place(x=1000, y=20)

        button4year = tk.Button(self, text="Fourth Year",bg='green', command=NedtaelOel4)
        button4year.pack()
        button4year.place(x=1100, y=0)

        button4yearned = tk.Button(self, text="Fourth Year", bg='red', command=OptaelOel4)
        button4yearned.pack()
        button4yearned.place(x=1100, y=20)

        button5year = tk.Button(self, text="Fifth Year",bg='green', command=NedtaelOel5)
        button5year.pack()
        button5year.place(x=1200, y=0)

        button5yearned = tk.Button(self, text="Fifth Year", bg='red', command=OptaelOel5)
        button5yearned.pack()
        button5yearned.place(x=1200, y=20)

        button6year = tk.Button(self, text="PhD+Employees", bg='green',command=NedtaelOel6)
        button6year.pack()
        button6year.place(x=1300, y=0)

        button6yearned = tk.Button(self, text="PhD+Employees", bg='red', command=OptaelOel6)
        button6yearned.pack()
        button6yearned.place(x=1300, y=20)

        #   button2 = ttk.Button(self, text="Restart", command=clear_text())
     #   button2.pack()
        button2 = tk.Button(self, text="Disaster",
                             command=lambda: controller.show_frame(Disaster1))
        button2.pack()
        button2.place(x=200, y=15)

        button3 = tk.Button(self, text="More disaster",
                             command=lambda: controller.show_frame(Disaster2))
        button3.pack()
        button3.place(x=300, y=15)

        button4 = tk.Button(self, text="Most disaster",
                             command=lambda: controller.show_frame(Disaster3))
        button4.pack()
        button4.place(x=400, y=15)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

       # toolbar = NavigationToolbar2Tk(canvas, self)
       # toolbar.update()
       # canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class Disaster1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Disaster!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button2 = ttk.Button(self, text="Back",
                             command=lambda: controller.show_frame(PageThree))
        button2.pack()
        button2.place(x=100, y=15)

        img = mpimg.imread('Volcano.png')
        imageplot = Figure(figsize=(8, 3), dpi=200)
        g = imageplot.add_subplot(111)
        g.imshow(img)
        g.axis("off")
        g.grid("off")
        imageplot.suptitle("Volcanic Eruption... Hot stuff all over... Brandbil for 8kr")

        canvas = FigureCanvasTkAgg(imageplot, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

class Disaster2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="More disaster!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button2 = ttk.Button(self, text="Back",
                             command=lambda: controller.show_frame(PageThree))
        button2.pack()
        button2.place(x=100, y=15)

        img = mpimg.imread('Earthquake.png')
        imageplot = Figure(figsize=(8, 3), dpi=200)
        g = imageplot.add_subplot(111)
        g.imshow(img)
        g.axis("off")
        g.grid("off")
        imageplot.suptitle("Earthquake... Move your feet... Best moves on the floor will be rewarded!")

        canvas = FigureCanvasTkAgg(imageplot, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

class Disaster3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Most disaster!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button2 = ttk.Button(self, text="Back",
                             command=lambda: controller.show_frame(PageThree))
        button2.pack()
        button2.place(x=100, y=15)

        img = mpimg.imread('Volcano.png')
        imageplot = Figure(figsize=(8, 3), dpi=200)
        g = imageplot.add_subplot(111)
        g.imshow(img)
        g.axis("off")
        g.grid("off")
        imageplot.suptitle("Volcanic Eruption... Hot stuff all over... Brandbil for 8kr")

        canvas = FigureCanvasTkAgg(imageplot, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

app = Børsbar()
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()