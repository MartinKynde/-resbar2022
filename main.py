import matplotlib

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
style.use("ggplot")
from matplotlib import *
f = Figure(figsize=(12, 6), dpi=100)
f.suptitle("Børsbar 2022",fontsize=35)
gs = matplotlib.gridspec.GridSpec(2, 3)
a = f.add_subplot(gs[0,0])
b = f.add_subplot(gs[0,1])
c = f.add_subplot(gs[0,-1])
a1 = f.add_subplot(gs[1,0])
b1 = f.add_subplot(gs[1,1])
c1 = f.add_subplot(gs[1,-1])
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
    si=(p*r*t)/100
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
            xs.append(float(x))
            ys.append(float(y))
    a.clear()
    a.plot(xs, ys, color="blue")
    a.set_title("First Year")

    #  if file_stat.st_size >= startingsizeFirstYear:


    secondyear = open('SecondYear.txt', 'r').read()
    lines1 = secondyear.split('\n')
    xs1 = []
    ys1 = []
    for line in lines1:
        if len(line) > 1:
            x1, y1 = line.split(',')
            y1 = float(y1)
            y1 = simple_interest(p, 1 * y1, 1)
            xs1.append(float(x1))
            ys1.append(float(y1))
    b.clear()
    b.plot(xs1, ys1, color="green")
    b.set_title("Second Year")


    thirdyear = open('ThirdYear.txt', 'r').read()
    lines2 = thirdyear.split('\n')
    xs2 = []
    ys2 = []
    for line in lines2:
        if len(line) > 1:
            x2, y2 = line.split(',')
            y2 = float(y2)
            y2 = simple_interest(p, 1 * y2, 1)
            xs2.append(float(x2))
            ys2.append(float(y2))
    c.clear()
    c.plot(xs2, ys2, color="purple")
    c.set_title("Third Year")


    fourthyear = open('FourthYear.txt', 'r').read()
    lines3 = fourthyear.split('\n')
    xs3 = []
    ys3 = []
    for line in lines3:
        if len(line) > 1:
            x3, y3 = line.split(',')
            y3 = float(y3)
            y3 = simple_interest(p, 1 * y3, 1)
            xs3.append(float(x3))
            ys3.append(float(y3))
    a1.clear()
    a1.plot(xs3, ys3,  color="orange")
    a1.set_title("Fourth Year")


    fifthyear = open('FifthYear.txt', 'r').read()
    lines4 = fifthyear.split('\n')
    xs4 = []
    ys4 = []
    for line in lines4:
        if len(line) > 1:
            x4, y4 = line.split(',')
            y4 = float(y4)
            y4 = simple_interest(p, 1 * y4, 1)
            xs4.append(float(x4))
            ys4.append(float(y4))
    b1.clear()
    b1.plot(xs4, ys4)
    b1.set_title("Fifth Year")

    phdansatte = open('PhdAnsatte.txt', 'r').read()
    lines5 = phdansatte.split('\n')
    xs5 = []
    ys5 = []
    for line in lines5:
        if len(line) > 1:
            x5, y5 = line.split(',')
            y5 = float(y5)
            y5 = simple_interest(p, 1 * y5, 1)
            xs5.append(float(x5))
            ys5.append(float(y5))
    c1.clear()
    c1.plot(xs5, ys5, color="pink")
    c1.set_title("PhD & Employees")



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


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self) #text="Aktier", font=LARGE_FONT
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

     #   button2 = ttk.Button(self, text="Restart", command=clear_text())
     #   button2.pack()
        button2 = ttk.Button(self, text="Disaster",
                             command=lambda: controller.show_frame(Disaster1))
        button2.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class Disaster1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Disaster!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button2 = ttk.Button(self, text="Back",
                             command=lambda: controller.show_frame(PageThree))
        button2.pack()

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

        label = tk.Label(self, text="Disaster!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button2 = ttk.Button(self, text="Back",
                             command=lambda: controller.show_frame(PageThree))
        button2.pack()

        img = mpimg.imread('Earthquake.png')
        imageplot = Figure(figsize=(8, 3), dpi=200)
        g = imageplot.add_subplot(111)
        g.imshow(img)
        g.axis("off")
        g.grid("off")
        imageplot.suptitle("Earthquake... Move ")

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