import matplotlib
import numpy
from numpy import ndarray
import re
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


def animate(r):
    a.clear()

    firstyear = open('FirstYear.txt', 'r').read()
    lines = firstyear.split('\n')
    xs = []
    ys = []
    h = 0
    m = 0
    y = 0
    for line in lines:
        if len(line) > 1:
            ##y5 = float(y5)
            h, m, y = re.split(':|, ', line)

            y = float(y)
            h = float(h)
            m = float(m)
            y = simple_interest(p, 1 * y, 1)
            xs.append(datetime.datetime(2022, 4, 22, int(h), int(m)))
            ys.append(float(y))

    if int(h)==0 & int(m)==0 & int(y)==0:
        pass
    else:
        a.plot(xs,ys, marker='o', color='#d53e4f', lw=3, alpha=0.7)

    #  a.set_title("First Year")

    secondyear = open('SecondYear.txt', 'r').read()
    lines1 = secondyear.split('\n')
    xs1 = []
    ys1 = []
    h1 = 0
    m1 = 0
    y1 = 0
    for line in lines1:
        if len(line) > 1:
            ##y5 = float(y5)
            h1, m1, y1 = re.split(':|, ', line)

            y1 = float(y1)
            h1 = float(h1)
            m1 = float(m1)
            y1 = simple_interest(p, 1 * y1, 1)
            xs1.append(datetime.datetime(2022, 4, 22, int(h1), int(m1)))
            ys1.append(float(y1))

    #    a.clear(
    if int(h1)==0 & int(m1)==0 & int(y1)==0:
        pass
    else:
        a.plot(xs1, ys1, marker='+', color='#fc8d59', lw=3, alpha=0.7)
    # a.set_title("Second Year")

    thirdyear = open('ThirdYear.txt', 'r').read()
    lines2 = thirdyear.split('\n')
    xs2 = []
    ys2 = []
    h2 = 0
    m2 = 0
    y2 = 0
    for line in lines2:
        if len(line) > 1:
            ##y5 = float(y5)
            h2, m2, y2 = re.split(':|, ', line)

            y2 = float(y2)
            h2 = float(h2)
            m2 = float(m2)
            y2 = simple_interest(p, 1 * y2, 1)
            xs2.append(datetime.datetime(2022, 4, 22, int(h2), int(m2)))
            ys2.append(float(y2))

    #    a.clear(
    if int(h2)==0 & int(m2)==0 & int(y2)==0:
        pass
    else:
        a.plot(xs2, ys2, marker='v', color='#fee08b', lw=3, alpha=0.7)
    # c.set_title("Third Year")

    fourthyear = open('FourthYear.txt', 'r').read()
    lines3 = fourthyear.split('\n')
    xs3 = []
    ys3 = []
    h3 = 0
    m3 = 0
    y3 = 0
    for line in lines3:
        if len(line) > 1:
            ##y5 = float(y5)
            h3, m3, y3 = re.split(':|, ', line)

            y3 = float(y3)
            h3 = float(h3)
            m3 = float(m3)
            y3 = simple_interest(p, 1 * y3, 1)
            xs3.append(datetime.datetime(2022, 4, 22, int(h3), int(m3)))
            ys3.append(float(y3))

    #    a.clear(
    if int(h3)==0 & int(m3)==0 & int(y3)==0:
        pass
    else:
        a.plot(xs3, ys3, marker='D', color='#8b008b', lw=3, alpha=0.7)
    # a1.set_title("Fourth Year")

    fifthyear = open('FifthYear.txt', 'r').read()
    lines4 = fifthyear.split('\n')
    xs4 = []
    ys4 = []
    h4 = 0
    m4 = 0
    y4 = 0
    for line in lines4:
        if len(line) > 1:
            ##y5 = float(y5)
            h4, m4, y4 = re.split(':|, ', line)

            y4 = float(y4)
            h4 = float(h4)
            m4 = float(m4)
            y4 = simple_interest(p, 1 * y4, 1)
            xs4.append(datetime.datetime(2022, 4, 22, int(h4), int(m4)))
            ys4.append(float(y4))

    #    a.clear(
    if int(h4)==0 & int(m4)==0 & int(y4)==0:
        pass
    else:
        a.plot(xs4, ys4, marker='h', color='#006400', lw=3, alpha=0.7)
    # b1.set_title("Fifth Year")


    phdansatte = open('PhdAnsatte.txt', 'r').read()
    lines5 = phdansatte.split('\n')
    xs5 = []
    ys5 = []
    h5 = 0
    m5 = 0
    y5 = 0
    for line in lines5:
        if len(line) > 1:
           ##y5 = float(y5)
            h5, m5, y5 = re.split(':|, ', line)
            y5 = float(y5)
            h5 = float(h5)
            m5 = float(m5)
            y5 = simple_interest(p, 1 * y5, 1)
            xs5.append(datetime.datetime(2022, 4, 22, int(h5), int(m5)))
            ys5.append(float(y5))

    if int(h5)==0 & int(m5)==0 & int(y5)==0:
        pass
    else:
        a.plot(xs5, ys5, marker='*', color='#3288bd', lw=3, alpha=0.7)
    import matplotlib.dates as mdates
    import matplotlib.ticker
  #  myFmt = mdates.DateFormatter('%d')
  #  a.xaxis.set_major_formatter(myFmt)
    xfmt = mdates.DateFormatter("%H:%M")
    a.xaxis.set_major_formatter(xfmt)
    a.legend(["First Year", "Second Year", "Third Year", "Fourth Year", "Fifth Year",
              "PhD + Employees"], loc= 'lower center', bbox_to_anchor=(0.5, -0.1), ncol=6, prop={'size': 16})
    #c1.set_title("PhD & Employees")


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
    content4 = content3 + ", " + content2
    textfile = open("PhdAnsatte.txt", "a")
    textfile.write(str(content4) + "\n")
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


def Update():
    global firsttemp, firsttemp2, firsttemp3, firsttemp4, firsttemp5, firsttemp6
    content = str(datetime.datetime.now())
    date = content[slice(11, 16)]


    firstbeer = firsttemp
    firstbeer5 = firsttemp5
    firstbeer2 = firsttemp2
    firstbeer3 = firsttemp3
    firstbeer4 = firsttemp4
    firstbeer6 = firsttemp6

    update1 = str(firstbeer)
    update2 = str(firstbeer2)
    update3 = str(firstbeer3)
    update4 = str(firstbeer4)
    update5 = str(firstbeer5)
    update6 = str(firstbeer6)

    content1 = date + ", " + update1
    content2 = date + ", " + update2
    content3 = date + ", " + update3
    content4 = date + ", " + update4
    content5 = date + ", " + update5
    content6 = date + ", " + update6

    textfile = open("FirstYear.txt", "a")
    textfile.write(str(content1) + "\n")
    textfile.close()

    textfile = open("SecondYear.txt", "a")
    textfile.write(str(content2) + "\n")
    textfile.close()

    textfile = open("ThirdYear.txt", "a")
    textfile.write(str(content3) + "\n")
    textfile.close()

    textfile = open("FourthYear.txt", "a")
    textfile.write(str(content4) + "\n")
    textfile.close()

    textfile = open("FifthYear.txt", "a")
    textfile.write(str(content5) + "\n")
    textfile.close()
    textfile = open("PhdAnsatte.txt", "a")
    textfile.write(str(content6) + "\n")
    textfile.close()


def Inflation():
    global firsttemp, firsttemp2, firsttemp3, firsttemp4, firsttemp5, firsttemp6

    content = str(datetime.datetime.now())
    date = content[slice(11, 16)]

    if firsttemp >=0:
        firsttemp -= firsttemp*0.2
    else:
        firsttemp += firsttemp * 0.2

    if firsttemp2 >=0:
        firsttemp2 -= firsttemp2*0.2
    else:
        firsttemp2 += firsttemp2 * 0.2

    if firsttemp3 >=0:
        firsttemp3 -= firsttemp3*0.2
    else:
        firsttemp3 += firsttemp3 * 0.2

    if firsttemp4 >=0:
        firsttemp4 -= firsttemp4*0.2
    else:
        firsttemp4 += firsttemp4 * 0.2

    if firsttemp5 >=0:
        firsttemp5 -= firsttemp5*0.2
    else:
        firsttemp5 += firsttemp5 * 0.2

    if firsttemp6 >=0:
        firsttemp6 -= firsttemp6*0.2
    else:
        firsttemp6 += firsttemp6 * 0.2


    firstbeer = firsttemp
    firstbeer5 = firsttemp5
    firstbeer2 = firsttemp2
    firstbeer3 = firsttemp3
    firstbeer4 = firsttemp4
    firstbeer6 = firsttemp6


    update1 = str(firstbeer)
    update2 = str(firstbeer2)
    update3 = str(firstbeer3)
    update4 = str(firstbeer4)
    update5 = str(firstbeer5)
    update6 = str(firstbeer6)

    content1 = date + ", " + update1
    content2 = date + ", " + update2
    content3 = date + ", " + update3
    content4 = date + ", " + update4
    content5 = date + ", " + update5
    content6 = date + ", " + update6

    textfile = open("FirstYear.txt", "a")
    textfile.write(str(content1) + "\n")
    textfile.close()

    textfile = open("SecondYear.txt", "a")
    textfile.write(str(content2) + "\n")
    textfile.close()

    textfile = open("ThirdYear.txt", "a")
    textfile.write(str(content3) + "\n")
    textfile.close()

    textfile = open("FourthYear.txt", "a")
    textfile.write(str(content4) + "\n")
    textfile.close()

    textfile = open("FifthYear.txt", "a")
    textfile.write(str(content5) + "\n")
    textfile.close()
    textfile = open("PhdAnsatte.txt", "a")
    textfile.write(str(content6) + "\n")
    textfile.close()


def Deflation():
    global firsttemp, firsttemp2, firsttemp3, firsttemp4, firsttemp5, firsttemp6


    if firsttemp >= 0:
        firsttemp += firsttemp * 0.015
    else:
        firsttemp -= firsttemp * 0.015

    if firsttemp2 >= 0:
        firsttemp2 += firsttemp2 * 0.015
    else:
        firsttemp2 -= firsttemp2 * 0.015

    if firsttemp3 >= 0:
        firsttemp3 += firsttemp3 * 0.015
    else:
        firsttemp3 -= firsttemp3 * 0.015

    if firsttemp4 >= 0:
        firsttemp4 += firsttemp4 * 0.015
    else:
        firsttemp4 -= firsttemp4 * 0.015

    if firsttemp5 >= 0:
        firsttemp5 += firsttemp5 * 0.015
    else:
        firsttemp5 -= firsttemp5 * 0.015

    if firsttemp6 >= 0:
        firsttemp6 += firsttemp6 * 0.015
    else:
        firsttemp6 -= firsttemp6 * 0.015

    firstbeer = firsttemp
    firstbeer5 = firsttemp5
    firstbeer2 = firsttemp2
    firstbeer3 = firsttemp3
    firstbeer4 = firsttemp4
    firstbeer6 = firsttemp6

    content = str(datetime.datetime.now())
    date = content[slice(11, 16)]

    update1 = str(firstbeer)
    update2 = str(firstbeer2)
    update3 = str(firstbeer3)
    update4 = str(firstbeer4)
    update5 = str(firstbeer5)
    update6 = str(firstbeer6)

    content1 = date + ", " + update1
    content2 = date + ", " + update2
    content3 = date + ", " + update3
    content4 = date + ", " + update4
    content5 = date + ", " + update5
    content6 = date + ", " + update6

    textfile = open("FirstYear.txt", "a")
    textfile.write(str(content1) + "\n")
    textfile.close()

    textfile = open("SecondYear.txt", "a")
    textfile.write(str(content2) + "\n")
    textfile.close()

    textfile = open("ThirdYear.txt", "a")
    textfile.write(str(content3) + "\n")
    textfile.close()

    textfile = open("FourthYear.txt", "a")
    textfile.write(str(content4) + "\n")
    textfile.close()

    textfile = open("FifthYear.txt", "a")
    textfile.write(str(content5) + "\n")
    textfile.close()
    textfile = open("PhdAnsatte.txt", "a")
    textfile.write(str(content6) + "\n")
    textfile.close()



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

        for F in (StartPage,  PageThree, Disaster1, Disaster2, Disaster3, Disaster4, Disaster5):
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

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self) #text="Aktier", font=LARGE_FONT
        label.pack(pady=10, padx=10)
        Update()

        button1 = tk.Button(self, text="Back",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button1.place(x=100, y=15)

        buttonfirstyear = tk.Button(self,text="First Year", bg='green', command=lambda:[NedtaelOel()]) #, Update()]
        buttonfirstyear.pack()
        buttonfirstyear.place(x= 800, y=0)

        buttonfirstyearned = tk.Button(self, text="First Year", bg='red', command=lambda:[OptaelOel()]) #
        buttonfirstyearned.pack()
        buttonfirstyearned.place(x=800, y=20)

        button2year = tk.Button(self, text="Second Year", bg='green', command=lambda:[NedtaelOel2()])
        button2year.pack()
        button2year.place(x=900, y=0)

        button2yearned = tk.Button(self, text="Second Year", bg='red', command=lambda:[OptaelOel2()])
        button2yearned.pack()
        button2yearned.place(x=900, y=20)

        button3year = tk.Button(self, text="Third Year",bg='green', command=lambda:[NedtaelOel3()])
        button3year.pack()
        button3year.place(x=1000, y=0)

        button3yearned = tk.Button(self, text="Third Year", bg='red', command=lambda:[OptaelOel3()])
        button3yearned.pack()
        button3yearned.place(x=1000, y=20)

        button4year = tk.Button(self, text="Fourth Year",bg='green', command=lambda:[NedtaelOel4()])
        button4year.pack()
        button4year.place(x=1100, y=0)

        button4yearned = tk.Button(self, text="Fourth Year", bg='red', command=lambda:[OptaelOel4()])
        button4yearned.pack()
        button4yearned.place(x=1100, y=20)

        button5year = tk.Button(self, text="Fifth Year",bg='green', command=lambda:[NedtaelOel5()])
        button5year.pack()
        button5year.place(x=1200, y=0)

        button5yearned = tk.Button(self, text="Fifth Year", bg='red', command=lambda:[OptaelOel5()])
        button5yearned.pack()
        button5yearned.place(x=1200, y=20)

        button6year = tk.Button(self, text="PhD+Employees", bg='green',command=lambda:[NedtaelOel6()])
        button6year.pack()
        button6year.place(x=1300, y=0)

        button6yearned = tk.Button(self, text="PhD+Employees", bg='red', command=lambda:[OptaelOel6()])
        button6yearned.pack()
        button6yearned.place(x=1300, y=20)

        button6yearned22 = tk.Button(self, text="Update", command=Update)
        button6yearned22.pack()
        button6yearned22.place(x=1700, y=10)


        button7 = tk.Button(self, text="Inflation", bg='red',command=lambda:[Inflation(), Update()])
        button7.pack()
        button7.place(x=1800, y=10)

      #  button8 = tk.Button(self, text="Stonks!", bg='green', command=lambda:[Deflation(), Update()])
      #  button8.pack()
      #  button8.place(x=1600, y=10)

        button2 = tk.Button(self, text="Event 1",
                             command=lambda: controller.show_frame(Disaster1))
        button2.pack()
        button2.place(x=200, y=15)

        button3 = tk.Button(self, text="Event 2",
                             command=lambda: controller.show_frame(Disaster2))
        button3.pack()
        button3.place(x=300, y=15)

        button4 = tk.Button(self, text="Event 3",
                             command=lambda: controller.show_frame(Disaster3))
        button4.pack()
        button4.place(x=400, y=15)

        button44 = tk.Button(self, text="Event 4",
                            command=lambda: controller.show_frame(Disaster4))
        button44.pack()
        button44.place(x=500, y=15)

        button444 = tk.Button(self, text="Event 5",
                            command=lambda: controller.show_frame(Disaster5))
        button444.pack()
        button444.place(x=600, y=15)

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
        imageplot.suptitle("Vulkanudbrud... It's getting hot in here... \n Brandbil giver dobbelt point")

        canvas = FigureCanvasTkAgg(imageplot, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

class Disaster2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Disaster!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button2 = ttk.Button(self, text="Back",
                             command=lambda: controller.show_frame(PageThree))
        button2.pack()
        button2.place(x=100, y=15)

        img = mpimg.imread('Earthquake.jpg')
        imageplot = Figure(figsize=(8, 3), dpi=200)
        g = imageplot.add_subplot(111)
        g.imshow(img)
        g.axis("off")
        g.grid("off")
        imageplot.suptitle("Jordskælv... Store ødelæggelser og aktiemarkedet lider... \n De kraftige rystelser gør Shakers (og pink) mere værd (1,5 point)")

        canvas = FigureCanvasTkAgg(imageplot, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

class Disaster3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Disaster!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button2 = ttk.Button(self, text="Back",
                             command=lambda: controller.show_frame(PageThree))
        button2.pack()
        button2.place(x=100, y=15)

        img = mpimg.imread('Landslide.jpg')
        imageplot = Figure(figsize=(8, 3), dpi=200)
        g = imageplot.add_subplot(111)
        g.imshow(img)
        g.axis("off")
        g.grid("off")
        imageplot.suptitle("Jordskred... Endnu en nedgang for aktiemarkedet... \n Alt det overflødige jord gør Søren Munchs Jordprøver billigere (10Kr)")

        canvas = FigureCanvasTkAgg(imageplot, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


class Disaster4(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Noice!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button2 = ttk.Button(self, text="Back",
                             command=lambda: controller.show_frame(PageThree))
        button2.pack()
        button2.place(x=100, y=15)

        img = mpimg.imread('Olie.jpg')
        imageplot = Figure(figsize=(8, 3), dpi=200)
        g = imageplot.add_subplot(111)
        g.imshow(img)
        g.axis("off")
        g.grid("off")
        imageplot.suptitle("Et kæmpe fund af Nordsøolie giver favorable tider for aktiemarkedet... \n Råolie er på tilbud - 3 stk. for 10kr")

        canvas = FigureCanvasTkAgg(imageplot, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


class Disaster5(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Disaster!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button2 = ttk.Button(self, text="Back",
                             command=lambda: controller.show_frame(PageThree))
        button2.pack()
        button2.place(x=100, y=15)

        img = mpimg.imread('Global.jpg')
        imageplot = Figure(figsize=(8, 3), dpi=200)
        g = imageplot.add_subplot(111)
        g.imshow(img)
        g.axis("off")
        g.grid("off")
        imageplot.suptitle("Global opvarmning er på det højeste nogensinde... \n Isbjørne er i høj kurs og giver dobbelt point!")

        canvas = FigureCanvasTkAgg(imageplot, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

app = Børsbar()
ani = animation.FuncAnimation(f, animate, frames=t, interval=1000)

import schedule

schedule.every(5).minutes.do(Deflation)
schedule.every(1).minutes.do(Update)

while True:
    schedule.run_pending()
    app.update_idletasks()
    app.update()
#app.mainloop()
