from tkinter import *
from tkinter.ttk import Combobox
from tkinter.messagebox import showinfo
from math import sqrt, pi
from webbrowser import open as openw
import json
import subprocess
import sys

try:
    from PIL import Image, ImageTk
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pillow'])
finally:
    from PIL import Image, ImageTk
from zipfile import ZipFile
from os import remove


class Areas:
    def __init__(self):
        self.lst = ['Parallelogram', 'Square', 'Rectangle', 'Circle',
                    'Triangle', 'Trapezoid', 'Rhombus']
        self.cb = Combobox(frame2, value=self.lst, width=16, state="readonly")
        self.cb.current(0)
        self.cb.bind('<<ComboboxSelected>>', updateShapes)

    def value(self):
        return self.cb.get()

    def put(self):
        self.cb.grid(row=0, column=1, pady=5, padx=12, sticky=W)

    def delete(self):
        self.cb.grid_forget()


class Volumes(Areas):
    def __init__(self):
        self.lst = ['Cube', 'Rectangular Prism', 'Triangular Prism', 'Sphere', 'Cylinder', 'Cone',
                    'Pyramid']
        self.cb = Combobox(frame2, value=self.lst, width=16, state="readonly")
        self.cb.current(0)
        self.cb.bind('<<ComboboxSelected>>', updateShapes)


class Shapes:
    def __init__(self):
        self.input1 = Entry(frame2, width=8, textvariable=iv1)
        self.input2 = Entry(frame2, width=8, textvariable=iv2)
        self.input3 = Entry(frame2, width=8, textvariable=iv3)
        self.input4 = Entry(frame2, width=8, textvariable=iv4)

        self.lbl1 = Label(frame2, text='b =')
        self.lbl2 = Label(frame2, text='h =')
        self.lbl3 = Label(frame2, text='A =')
        self.lbl4 = Label(frame2, text='u')
        self.lbl5 = Label(frame2, text='u')
        self.lbl6 = Label(frame2, text='u')
        self.lbl7 = Label(frame2, text='u²')
        self.lbl8 = Label(frame2, text='u')

    def forgetSome(self):
        self.lbl2.grid_forget()
        self.input2.grid_forget()
        self.lbl6.grid_forget()
        self.lbl4.grid_forget()
        self.input4.grid_forget()
        self.lbl8.grid_forget()

    def put(self):
        if cb.get() == 'Area':
            ar = areas.value()
            self.lbl1.grid(row=0, column=2, padx=3)
            self.input1.grid(row=0, column=3, padx=3)
            self.lbl5.grid(row=0, column=4, padx=3)
            self.lbl2.grid(row=0, column=5, padx=5)
            self.input2.grid(row=0, column=6, padx=3)
            self.lbl6.grid(row=0, column=7, padx=3)
            self.lbl3.grid(row=0, column=8, padx=5)
            self.input3.grid(row=0, column=9, padx=3)
            self.lbl7.grid(row=0, column=10, padx=3)

            self.lbl4.grid_forget()
            self.input4.grid_forget()
            self.lbl8.grid_forget()
            if ar == 'Square':
                self.lbl2.grid_forget()
                self.input2.grid_forget()
                self.lbl6.grid_forget()

                self.lbl1.config(text='a =')
            elif ar == 'Circle':
                self.lbl2.grid_forget()
                self.input2.grid_forget()
                self.lbl6.grid_forget()

                self.lbl1.config(text='r =')
            elif ar == 'Trapezoid':
                self.lbl4.grid(row=0, column=8, padx=3)
                self.input4.grid(row=0, column=9, padx=5)
                self.lbl7.grid(row=0, column=13, padx=3)
                self.lbl3.grid(row=0, column=11, padx=5)
                self.input3.grid(row=0, column=12, padx=3)
                self.lbl8.grid(row=0, column=10, padx=3)

                self.lbl1.config(text='b =')
                self.lbl4.config(text='h =')
                self.lbl2.config(text='a =')

            else:
                self.lbl1.config(text='b =')
                self.lbl2.config(text='h =')

        else:
            vs = volumes.value()
            self.lbl1.grid(row=0, column=2, padx=3)
            self.input1.grid(row=0, column=3, padx=3)
            self.lbl5.grid(row=0, column=4, padx=3)
            self.lbl3.grid(row=0, column=5, padx=3)
            self.input3.grid(row=0, column=6, padx=3)
            self.lbl7.grid(row=0, column=7, padx=3)
            self.forgetSome()

            if vs == 'Cube':
                self.lbl1.config(text='a =')
                self.forgetSome()

            elif vs == 'Sphere':
                self.lbl1.config(text='r =')
                self.forgetSome()

            else:
                self.lbl2.grid(row=0, column=5, padx=3)
                self.input2.grid(row=0, column=6, padx=3)
                self.lbl6.grid(row=0, column=7, padx=3)
                self.lbl3.grid(row=0, column=8, padx=3)
                self.input3.grid(row=0, column=9, padx=3)
                self.lbl7.grid(row=0, column=10, padx=3)

                self.lbl2.config(text='h =')
                if vs == 'Cone' or vs == 'Cylinder':
                    self.lbl1.config(text='r =')
                elif vs == 'Pyramid':
                    self.lbl1.config(text='a =')
                else:
                    self.lbl4.grid(row=0, column=8, padx=3)
                    self.input4.grid(row=0, column=9, padx=3)
                    self.lbl8.grid(row=0, column=10, padx=3)
                    self.lbl3.grid(row=0, column=11, padx=3)
                    self.input3.grid(row=0, column=12, padx=3)
                    self.lbl7.grid(row=0, column=13, padx=3)
                    if vs == 'Triangular Prism':
                        self.lbl1.config(text='b =')
                        self.lbl4.config(text='l =')
                    elif vs == 'Rectangular Prism':
                        self.lbl1.config(text='l =')
                        self.lbl2.config(text='w =')
                        self.lbl4.config(text='h =')


# ----- Config -----

root = Tk()
w = 730         # Global width
root.geometry(str(w)+'x470')
root.title('Shapes Calculator')
root.resizable(False, False)

# Setting the icon

with ZipFile('./res.dat') as z:
    z.extract('icon.ico')
root.iconbitmap('./icon.ico')
remove('./icon.ico')


# ----- Images Frame -----


frame1 = Frame(root, width=w, height=340, bg='white')
frame1.pack()
img = Label(frame1)


# ----- Functions -----

def reset():
    iv1.set('')
    iv2.set('')
    iv3.set('')
    iv4.set('')


def countX(lstc, x):
    count = 0
    for ele in lstc:
        if ele == x:
            count += 1
    return count


def curt(x):
    return x ** (1. / 3)


def negative(x):
    if x < 0:
        return True
    else:
        return False


def checc(a=False):
    global err
    if cb.get() == 'Area':
        sh = areas.value()

    else:
        sh = volumes.value()

    v1, v2, v3, v4 = [iv1.get(), iv2.get(), iv3.get(), iv4.get()]
    vlst = [v1, v2, v3, v4]
    par1 = ['Cube', 'Sphere', 'Square', 'Circle']
    par2 = ['Cylinder', 'Cone', 'Pyramid', 'Parallelogram', 'Rectangle', 'Triangle', 'Rhombus']

    if sh in par1 and not a and countX(vlst, '') < 4:
        iv3.set('')

    elif sh in par2 and not a and countX(vlst, '') < 2:
        iv3.set('')

    elif sh not in par2 and sh not in par1 and not a and countX(vlst, '') < 1:
        iv3.set('')

    if sh in par1:

        if v1 == '':
            try:
                float(v3)
                err = False
                butt.config(state=NORMAL)
                statusUpdate(0)
                if negative(float(v3)):
                    err = True
                    butt.config(state=DISABLED)
                    status.config(text='Please use valid numbers (Values can not be negative)')

            except ValueError:
                err = True
                butt.config(state=DISABLED)
                status.config(text='Please use valid numbers')
        if v3 == '':
            try:
                float(v1)
                err = False
                butt.config(state=NORMAL)
                statusUpdate(0)
                if negative(float(v1)):
                    err = True
                    butt.config(state=DISABLED)
                    status.config(text='Please use valid numbers (Values can not be negative)')
            except ValueError:
                err = True
                butt.config(state=DISABLED)
                status.config(text='Please enter valid numbers')
    elif sh in par2 and countX(vlst, '') < 3:
        if v1 == '':
            try:
                float(v2)
                float(v3)
                if negative(float(v3)) or negative(float(v2)):
                    err = True
                    butt.config(state=DISABLED)
                    status.config(text='Please use valid numbers (Values can not be negative)')
                err = False
                butt.config(state=NORMAL)
                statusUpdate(0)
            except ValueError:
                err = True
                butt.config(state=DISABLED)
                status.config(text='Please use valid numbers')
        if v2 == '':
            try:
                float(v1)
                float(v3)
                err = False
                butt.config(state=NORMAL)
                statusUpdate(0)
                if negative(float(v3)) or negative(float(v1)):
                    err = True
                    butt.config(state=DISABLED)
                    status.config(text='Please use valid numbers (Values can not be negative)')
            except ValueError:
                err = True
                butt.config(state=DISABLED)
                status.config(text='Please enter valid numbers')
        if v3 == '':
            try:
                float(v1)
                float(v2)
                err = False
                butt.config(state=NORMAL)
                statusUpdate(0)
                if negative(float(v2)) or negative(float(v1)):
                    err = True
                    butt.config(state=DISABLED)
                    status.config(text='Please use valid numbers (Values can not be negative)')
            except ValueError:
                err = True
                butt.config(state=DISABLED)
                status.config(text='Please enter valid numbers')
    elif sh not in par2 and sh not in par1 and countX(vlst, '') <= 1:
        if v1 == '':
            try:
                float(v2)
                float(v3)
                float(v4)
                err = False
                butt.config(state=NORMAL)
                statusUpdate(0)
                if negative(float(v2)) or negative(float(v3)) or negative(float(v4)):
                    err = True
                    butt.config(state=DISABLED)
                    status.config(text='Please use valid numbers (Values can not be negative)')
            except ValueError:
                err = True
                butt.config(state=DISABLED)
                status.config(text='Please use valid numbers')
        if v2 == '':
            try:
                float(v1)
                float(v3)
                float(v4)
                err = False
                butt.config(state=NORMAL)
                statusUpdate(0)
                if negative(float(v1)) or negative(float(v3)) or negative(float(v4)):
                    err = True
                    butt.config(state=DISABLED)
                    status.config(text='Please use valid numbers (Values can not be negative)')
            except ValueError:
                err = True
                butt.config(state=DISABLED)
                status.config(text='Please enter valid numbers')
        if v3 == '':
            try:
                float(v1)
                float(v2)
                float(v4)
                err = False
                butt.config(state=NORMAL)
                statusUpdate(0)
                if negative(float(v1)) or negative(float(v2)) or negative(float(v4)):
                    err = True
                    butt.config(state=DISABLED)
                    status.config(text='Please use valid numbers (Values can not be negative)')
            except ValueError:
                err = True
                butt.config(state=DISABLED)
                status.config(text='Please enter valid numbers')
        if v4 == '':
            try:
                float(v1)
                float(v2)
                float(v3)
                err = False
                butt.config(state=NORMAL)
                statusUpdate(0)
                if negative(float(v2)) or negative(float(v3)) or negative(float(v1)):
                    err = True
                    butt.config(state=DISABLED)
                    status.config(text='Please use valid numbers (Values can not be negative)')
            except ValueError:
                err = True
                butt.config(state=DISABLED)
                status.config(text='Please enter valid numbers')


def calculate():
    global err
    if cb.get() == 'Area':
        sh = areas.value()
    else:
        sh = volumes.value()
    try:
        v1, v2, v3, v4 = [iv1.get(), iv2.get(), iv3.get(), iv4.get()]
        vlst = [v1, v2, v3, v4]
        par1 = ['Cube', 'Sphere', 'Square', 'Circle']
        par2 = ['Cylinder', 'Cone', 'Pyramid', 'Parallelogram', 'Rectangle', 'Triangle', 'Rhombus']
        par3 = ['Trapezoid', 'Rectangular Prism', 'Triangular Prism']

        if sh in par1:
            if countX(vlst, '') == 3:
                butt.config(state=DISABLED)
                err = True
            else:
                butt.config(state=NORMAL)
                err = False
        elif sh in par2:
            if countX(vlst, '') > 2:
                butt.config(state=DISABLED)
                err = True
            else:
                butt.config(state=NORMAL)
                err = False
        else:
            if countX(vlst, '') > 1:
                butt.config(state=DISABLED)
                err = True
            else:
                butt.config(state=NORMAL)
                err = False

        if sh in par1 and countX(vlst, '') == 2:
            iv3.set('')

        elif sh in par2 and countX(vlst, '') == 1:
            iv3.set('')

        elif sh not in par2 and sh not in par1 and countX(vlst, '') == 0:
            iv3.set('')

        if sh in par1:
            if v1 == '':
                if sh == 'Square':
                    iv1.set(str(round(sqrt(float(v3)), 3)))
                elif sh == 'Circle':
                    iv1.set(str(round(sqrt(float(v3) / pi), 3)))
                elif sh == 'Cube':
                    iv1.set(str(round(curt(float(v3)), 3)))
                elif sh == 'Sphere':
                    iv1.set(str(round(curt((float(v3) * 3) / (pi * 4)), 3)))
            elif v3 == '':
                if sh == 'Square':
                    iv3.set(str(round((float(v1) ** 2), 3)))
                elif sh == 'Circle':
                    iv3.set(str(round((pi * float(v1)) ** 2, 3)))
                elif sh == 'Cube':
                    iv3.set(str(round(float(v1) ** 3, 3)))
                elif sh == 'Sphere':
                    iv3.set(str(round((4. / 3) * (pi * (float(v1) ** 3)), 3)))

        elif sh in par2:
            if v1 == '':    # Calculating 1st value, setting it to iv1
                n2, n3 = [float(v2), float(v3)]
                if sh == 'Cylinder':
                    val = sqrt(n3 / pi * n2)
                    iv1.set(str(round(val, 3)))
                if sh == 'Cone':
                    val = sqrt(3 * (n3 / (pi * n2)))
                    iv1.set(str(round(val, 3)))
                if sh == 'Pyramid':
                    val = sqrt(3 * (n3 / n2))
                    iv1.set(str(round(val, 3)))
                if sh == 'Parallelogram' or sh == 'Rectangle':
                    val = n3 / n2
                    iv1.set(str(round(val, 3)))
                if sh == 'Triangle' or sh == 'Rhombus':
                    val = ((2 * n3) / n2)
                    iv1.set(str(round(val, 3)))
            elif v2 == '':  # Calculating 2nd value, setting it to iv2
                n1, n3 = [float(v1), float(v3)]
                if sh == 'Cylinder':
                    val = n3 / (pi * n1 ** 2)
                    iv2.set(str(round(val, 3)))
                if sh == 'Cone':
                    val = (3 * n3) / (pi * n1 ** 2)
                    iv2.set(str(round(val, 3)))
                if sh == 'Pyramid':
                    val = (3 * n3) / n1 ** 2
                    iv2.set(str(round(val, 3)))
                if sh == 'Parallelogram' or sh == 'Rectangle':
                    val = n3 / n1
                    iv2.set(str(round(val, 3)))
                if sh == 'Triangle' or sh == 'Rhombus':
                    val = ((2 * n3) / n1)
                    iv2.set(str(round(val, 3)))
            elif v3 == '':  # Calculating result (area / volume) , setting it to iv3
                n1, n2 = [float(v1), float(v2)]
                if sh == 'Cylinder':
                    val = (pi * v1 ** 2 * n2)
                    iv3.set(str(round(val, 3)))
                if sh == 'Cone':
                    val = (pi * n1 ** 2 * n2) / 3
                    iv3.set(str(round(val, 3)))
                if sh == 'Pyramid':
                    val = (n1 ** 2 * n2) / 3
                    iv3.set(str(round(val, 3)))
                if sh == 'Parallelogram' or sh == 'Rectangle':
                    val = n1 * n2
                    iv3.set(str(round(val, 3)))
                if sh == 'Triangle' or sh == 'Rhombus':
                    val = (n1 * n2) / 2
                    iv3.set(str(round(val, 3)))

        elif sh in par3:
            if v1 == '':    # Calculating 1st value and setting it to iv1
                n2, n3, n4 = [float(v2), float(v4), float(v3)]
                if sh == 'Trapezoid':
                    val = (2 * n4 / n3) - n2
                    if negative(val):
                        status.config(text='There is no solution for b (violates b > 0). Please change input values.')
                    else:
                        iv1.set(str(round(val, 2)))
                elif sh == 'Rectangular Prism':
                    val = n4 / (n3 * n2)
                    iv1.set(str(round(val, 2)))
                elif sh == 'Triangular Prism':
                    val = 2 * n4 / n2 * n3
                    iv1.set(str(round(val, 2)))
            if v2 == '':    # Calculating 2nd value and setting it to iv2
                n1, n3, n4 = [float(v1), float(v4), float(v3)]
                if sh == 'Trapezoid':
                    val = (2 * n4 / n3) - n1
                    if negative(val):
                        status.config(text='There is no solution for a (violates a > 0). Please change input values.')
                    else:
                        iv2.set(str(round(val, 2)))
                elif sh == 'Rectangular Prism':
                    val = n4 / (n1 * n3)
                    iv2.set(str(round(val, 2)))
                elif sh == 'Triangular Prism':
                    val = 2 * n4 / n1 * n3
                    iv2.set(str(round(val, 2)))
            if v4 == '':    # Calculating 3rd value and setting it to iv4
                n1, n2, n4 = [float(v1), float(v2), float(v3)]
                if sh == 'Trapezoid':
                    val = 2 * n4 / (n1 + n2)
                    iv4.set(str(round(val, 2)))
                elif sh == 'Rectangular Prism':
                    val = n4 / (n1 * n2)
                    iv4.set(str(round(val, 2)))
                elif sh == 'Triangular Prism':
                    val = 2 * n4 / n1 * n2
                    iv4.set(str(round(val, 2)))
            if v3 == '':    # Calculating result (area / volume) and setting it to iv3
                n1, n2, n3 = [float(v1), float(v2), float(v4)]
                if sh == 'Trapezoid':
                    val = (n1 + n2) * n3 / 2
                    iv3.set(str(round(val, 2)))
                elif sh == 'Rectangular Prism':
                    val = n1 * n2 * n3
                    iv3.set(str(round(val, 2)))
                elif sh == 'Triangular Prism':
                    val = n1 * n2 * n3 / 2
                    iv3.set(str(round(val, 2)))
    except ZeroDivisionError:
        status.config(text='Please use valid numbers (Can not divide by Zero)')


def updatePic():
    global img
    img.config(image='')
    if cb.get() == 'Area':
        sh = areas.value()
    else:
        sh = volumes.value()

    with ZipFile('./res.dat') as z:
        z.extract('pics.json')
        with open('./pics.json', 'r') as f:
            dirs = json.load(f)
        remove('./pics.json')
        i = dirs[sh]
        z.extract(i)
    i = './' + i
    # print(i)
    load = Image.open(i)
    render = ImageTk.PhotoImage(load)
    remove(i)
    img.config(image=render)
    img.image = render
    img.grid(row=0)


def statusUpdateR(e):
    statusUpdate(0)
    updatePic()
    reset()


def statusUpdate(e):

    shapes.put()
    if cb.get() == 'Area':
        areas.put()
        sh = areas.value()
        volumes.delete()
        shapes.lbl3.config(text='A =')
        shapes.lbl7.config(text='u²')
    else:
        volumes.put()
        sh = volumes.value()
        areas.delete()
        shapes.lbl3.config(text='V =')
        shapes.lbl7.config(text='u³')

    status.config(text='Calculating for: ' + sh + '\'s ' + cb.get() + '...')


def updateShapes(e):
    statusUpdateR(0)
    shapes.put()


def google():
    if cb.get() == 'Area':
        sh = areas.value()
    else:
        sh = volumes.value()
    with ZipFile('./res.dat') as z:
        z.extract('google.json')
        with open('./google.json', 'r') as f:
            dic = json.load(f)
    openw(dic[sh])
    remove('./google.json')


def credits():
    # Shows credit msg
    showinfo('Credits', '\tDeveloped by:\n\n\tig: @ashraf0016\n\n\ton: 23/08/2020\t    \n\n')

# ----- Menu -----


menu = Menu(root)
root.config(menu=menu)
subMenu1 = Menu(menu, tearoff=0)
menu.add_cascade(label='More', menu=subMenu1)
subMenu1.add_command(label='Shape\'s Google Calculator', command=google)
subMenu1.add_command(label='Credits', command=credits)
subMenu1.add_separator()
subMenu1.add_command(label='Exit', command=root.quit)

# ----- Variables -----

err = False

iv1 = StringVar()
iv2 = StringVar()
iv3 = StringVar()
iv4 = StringVar()

reset()

iv1.trace("w", lambda name, index, mode: checc())
iv2.trace("w", lambda name, index, mode: checc())
iv3.trace("w", lambda name, index, mode: checc(True))
iv4.trace("w", lambda name, index, mode: checc())

# ------ Status Bar ------


status = Label(root, text='Please select desired calculation', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

frame2 = Frame(root, width=w, height=109)
frame2.pack(side=BOTTOM)

# ----- Combo Boxes -----

lst = ['Area', 'Volume']
cb = Combobox(frame2, value=lst, width=8, state="readonly")
cb.current(0)
cb.bind('<<ComboboxSelected>>', statusUpdateR)
cb.grid(row=0, pady=10, padx=15, sticky=W)

# ----- Buttons -----

areas = Areas()
areas.put()
volumes = Volumes()
shapes = Shapes()

butt = Button(frame2, text='Calculate', command=calculate)
butt.grid(row=1, columnspan=7, padx=15, pady=6)

butt2 = Button(frame2, text='Reset', command=reset)
butt2.grid(row=1, column=8, padx=3, pady=6)

root.mainloop()
