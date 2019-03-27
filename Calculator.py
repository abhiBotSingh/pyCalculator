from tkinter import *
import tkinter.messagebox
import math


class Calculator:
    def __init__(self, rootfr):
        try:
            self.calVar = ""
            self.entryVar = StringVar()
            self.ans = ""
            self.rootfr = rootfr
            rootfr.configure(bg="light green")
            self.ent = Entry(rootfr, textvariable=self.entryVar, font=('arial', 10, 'bold'), bg="light blue", bd=15, width=40, justify=LEFT)
            self.ent.grid(row=0, column=0, columnspan=4, pady=1)
            self.ent.insert(0, "0")
            self.br1 = Button(rootfr, command=lambda: self.expression('('), bg="red", width=7, height=2, font=('arial', 10, 'bold'), text=' ( ', bd=5)
            self.br1.grid(row=1, column=0, pady=1)
            self.br2 = Button(rootfr, command=lambda: self.expression(')'), bg="red", width=7, height=2, font=('arial', 10, 'bold'), text=' ) ', bd=5)
            self.br2.grid(row=1, column=1, pady=1)
            self.c = Button(rootfr, command=self.clear, width=7, height=2, bg="red", font=('arial', 10, 'bold'), text=' C ', bd=5)
            self.c.grid(row=5, column=0, pady=1)
            self.c1 = Button(rootfr, command=self.clear_1, width=7, height=2, bg="red", font=('arial', 10, 'bold'), text=' \u232B ', bd=5)
            self.c1.grid(row=1, column=2, pady=1)
            self.eq = Button(rootfr, command=self.calculation, width=7, height=2, bg="red", font=('arial', 10, 'bold'), text=' = ', bd=5)
            self.eq.grid(row=1, column=3, pady=1)
            self.b7 = Button(rootfr, command=lambda: self.expression('7'), bg="red", width=7, height=2, font=('arial', 10, 'bold'), text=' 7 ', bd=5)
            self.b7.grid(row=2, column=0, pady=1)
            self.b8 = Button(rootfr, command=lambda: self.expression('8'), bg="red", width=7, height=2, font=('arial', 10, 'bold'), text=' 8 ', bd=5)
            self.b8.grid(row=2, column=1, pady=1)
            self.b9 = Button(rootfr, command=lambda: self.expression('9'),  bg="red", width=7, height=2, font=('arial', 10, 'bold'), text=' 9 ', bd=5)
            self.b9.grid(row=2, column=2, pady=1)
            self.div = Button(rootfr, command=lambda: self.expression('/'), bg="red", width=7, height=2, font=('arial', 10, 'bold'), text=" / ", bd=5)
            self.div.grid(row=2, column=3, pady=1)
            self.b4 = Button(rootfr, command=lambda: self.expression('4'), bg="red", width=7, height=2, font=('arial', 10, 'bold'), text=' 4 ', bd=5)
            self.b4.grid(row=3, column=0, pady=1)
            self.b5 = Button(rootfr, command=lambda: self.expression('5'), bg="red", width=7, height=2, font=('arial', 10, 'bold'), text=' 5 ', bd=5)
            self.b5.grid(row=3, column=1, pady=1)
            self.b6 = Button(rootfr, command=lambda: self.expression('6'), bg="red", width=7, height=2, font=('arial', 10, 'bold'), text=' 6 ', bd=5)
            self.b6.grid(row=3, column=2, pady=1)
            self.mul = Button(rootfr, command=lambda: self.expression('*'), bg="red", width=7, height=2, font=('arial', 10, 'bold'), text=" * ", bd=5)
            self.mul.grid(row=3, column=3, pady=1)
            self.b1 = Button(rootfr, command=lambda: self.expression('1'), bg="red", width=7, height=2, font=('arial', 10, 'bold'), text=' 1 ', bd=5)
            self.b1.grid(row=4, column=0, pady=1)
            self.b2 = Button(rootfr, command=lambda: self.expression('2'), bg="red", width=7, height=2, font=('arial', 10, 'bold'), text=' 2 ', bd=5)
            self.b2.grid(row=4, column=1, pady=1)
            self.b3 = Button(rootfr, command=lambda: self.expression('3'), bg="red", width=7, height=2, font=('arial', 10, 'bold'), text=' 3 ', bd=5)
            self.b3.grid(row=4, column=2, pady=1)
            self.add = Button(rootfr, command=lambda: self.expression('+'), bg="red", width=7, height=2, font=('arial', 10, 'bold'), text=" + ", bd=5)
            self.add.grid(row=4, column=3, pady=1)
            self.b0 = Button(rootfr, command=lambda: self.expression('0'), bg="red", width=7, height=2, font=('arial', 10, 'bold'), text=' 0 ', bd=5)
            self.b0.grid(row=5, column=1, pady=1)
            self.dot = Button(rootfr, command=lambda: self.expression('.'), bg="red", width=7, height=2, font=('arial', 10, 'bold'), text=' . ', bd=5)
            self.dot.grid(row=5, column=2, pady=1)
            self.sub = Button(rootfr, command=lambda: self.expression('-'), bg="red", width=7, height=2, font=('arial', 10, 'bold'), text=" - ", bd=5)
            self.sub.grid(row=5, column=3, pady=1)
            self.pm = Button(rootfr,command=self.plmi, bg="red", width=7, height=2, font=('arial', 10, 'bold'), text="\u2213", bd=5)
            self.pm.grid(row=6, column=0, pady=1)
            self.sq = Button(rootfr, command=self.squared, bg="red", width=7, height=2, font=('arial', 10, 'bold'), text="x\u00b2", bd=5)
            self.sq.grid(row=6, column=1, pady=1)
            self.xy = Button(rootfr, command=self.xpowery, bg="red", width=7, height=2, font=('arial', 10, 'bold'), text="x**y", bd=5)
            self.xy.grid(row=6, column=2, pady=1)
            self.sqrt = Button(rootfr, width=7, command=self.squ_rt, bg="red",  height=2, font=('arial', 10, 'bold'), text=" √ ", bd=5)
            self.sqrt.grid(row=6, column=3, pady=1)
            self.tenX = Button(rootfr, width=7, command=self.tenx, height=2, bg="red", font=('arial', 10, 'bold'), text=" 10ˣ ", bd=5)
            self.tenX.grid(row=7, column=0, pady=1)
            self.sin = Button(rootfr, width=7, command=self.sine, height=2, bg="red", font=('arial', 10, 'bold'), text=" sin ", bd=5)
            self.sin.grid(row=7, column=1, pady=1)
            self.cos = Button(rootfr, width=7, command=self.cosine, height=2, bg="red", font=('arial', 10, 'bold'), text=" cos ", bd=5)
            self.cos.grid(row=7, column=2, pady=1)
            self.tan = Button(rootfr, width=7, command=self.tangent, height=2, bg="red", font=('arial', 10, 'bold'), text=" tan ", bd=5)
            self.tan.grid(row=7, column=3, pady=1)
            self.log = Button(rootfr, width=7, command=self.log10, height=2, bg="red", font=('arial', 10, 'bold'), text=" log ", bd=5)
            self.log.grid(row=8, column=0, pady=1)
            self.md = Button(rootfr, width=7, command=self.modu, height=2, bg="red", font=('arial', 10, 'bold'), text=" mod ", bd=5)
            self.md.grid(row=8, column=1, pady=1)
            self.fact = Button(rootfr, width=7, command=self.fct, height=2, bg="red", font=('arial', 10, 'bold'), text=" n! ", bd=5)
            self.fact.grid(row=8, column=2, pady=1)
            self.pi = Button(rootfr, width=7, command=self.pie, height=2, bg="red", font=('arial', 10, 'bold'), text=" π ", bd=5)
            self.pi.grid(row=8, column=3, pady=1)
        except ZeroDivisionError as e:
            self.ent.insert(0, "Error")

    def expression(self, ch):
        str(self.calVar)
        self.calVar = self.calVar + str(ch)
        self.entryVar.set(self.calVar)

    def calculation(self):
        self.ans = eval(str(self.calVar))
        self.entryVar.set(self.ans)
        self.ans = str(self.ans)
        self.calVar = self.ans

    def clear(self):
        self.calVar = ""
        self.entryVar.set("")
        self.ent.insert(0, "0")

    def clear_1(self):
        self.calVar = self.calVar[:-1]
        self.entryVar.set(self.calVar)

    def squ_rt(self):
        self.calVar = float(self.calVar)
        self.ans = math.sqrt(self.calVar)
        self.entryVar.set(self.ans)
        self.ans = str(self.ans)
        self.calVar = self.ans

    def squared(self):
        a = float(self.calVar)
        self.ans = float(a**2)
        self.entryVar.set(self.ans)
        self.ans = str(self.ans)
        self.calVar = self.ans

    def xpowery(self):
        self.calVar = self.calVar+"**"
        self.entryVar.set(self.calVar)

    def plmi(self):
        a = -1.0*float(self.calVar)
        self.ans = a
        self.entryVar.set(self.ans)
        self.ans = str(self.ans)
        self.calVar = self.ans

    def tenx(self):
        self.calVar = self.calVar + "10**"
        self.entryVar.set(self.calVar)

    def sine(self):
        self.ans = float(self.calVar)
        self.ans = math.sin(self.ans)
        self.entryVar.set(self.ans)
        self.ans = str(self.ans)
        self.calVar = self.ans

    def cosine(self):
        self.ans = float(self.calVar)
        self.ans = math.cos(self.ans)
        self.entryVar.set(self.ans)
        self.ans = str(self.ans)
        self.calVar = self.ans

    def tangent(self):
        self.ans = float(self.calVar)
        self.ans = math.tan(self.ans)
        self.entryVar.set(self.ans)
        self.ans = str(self.ans)
        self.calVar = self.ans

    def log10(self):
        self.ans = float(self.calVar)
        self.ans = math.log10(self.ans)
        self.entryVar.set(self.ans)
        self.ans = str(self.ans)
        self.calVar = self.ans

    def modu(self):
        self.calVar = self.calVar + "%"
        self.entryVar.set(self.calVar)

    def fct(self):
        self.ans = int(self.calVar)
        self.ans = math.factorial(self.ans)
        self.entryVar.set(self.ans)
        self.ans = str(self.ans)
        self.calVar = self.ans

    def pie(self):
        a = math.pi
        self.ans = str(a)
        self.entryVar.set(self.ans)
        self.calVar = self.ans


def exitcalc():
    exitcalc = tkinter.messagebox.askyesno("Scientific Calculator", "Confirm if you want to exit?")
    if exitcalc > 0:
        root.destroy()
        return


def standard():
    root.geometry("315x310+400+150")


def scientific():
    root.geometry("315x468+400+150")


root = Tk()
root.geometry("315x310+400+150")
root.title("Scientific Calculator")
root.resizable(0, 0)
root.configure(bg="light pink")
rootfr = Frame(root)
rootfr.grid()
b = Calculator(rootfr)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Standard", command=standard)
filemenu.add_command(label="Scientific", command=scientific)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exitcalc)
root.configure(menu=menubar)
root.mainloop()
