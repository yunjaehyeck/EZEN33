from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Frame, Label, Entry


class App(Frame):
    def __init__(self,parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("계산기")
        self.pack(fill=BOTH, expand=True)
        global value
        value = 0
        global num1
        num1 = StringVar()
        global num2
        num2 = StringVar()
        global res
        res = StringVar()

        frame1 = Frame(self)
        frame1.pack(fill=X) #X 대문자
        lbl1 = Label(frame1, text="INPUT NUMBER 1: ", width=15)
        lbl1.pack(side=LEFT, padx=5, pady=5)
        entry1 = Entry(frame1, textvariable=num1)
        entry1.pack(fill=X, padx=5, expand=True)

        frame2 = Frame(self)
        frame2.pack(fill=X)  # X 대문자
        lbl2 = Label(frame2, text="INPUT NUMBER 2: ", width=15)
        lbl2.pack(side=LEFT, padx=5, pady=5)
        entry2 = Entry(frame2, textvariable=num1)
        entry2.pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=X)

        btn_plus = Button(frame3, text="+", width=8, command=self.plus)
        btn_plus.pack(side=LEFT, anchor=N, padx=5, pady=5)

        btn_minus = Button(frame3, text="-", width=8, command=self.minus)
        btn_minus.pack(side=LEFT, anchor=N, padx=5, pady=5)

        btn_mul = Button(frame3, text="*", width=8, command=self.mul)
        btn_mul.pack(side=LEFT, anchor=N, padx=5, pady=5)

        btn_div = Button(frame3, text="/", width=8, command=self.div)
        btn_div.pack(side=LEFT, anchor=N, padx=5, pady=5)

        frame4 = Frame(self)
        frame4.pack(fill=X)

        lbl3 = Label(frame4, text="RESULT: ", width=10)
        lbl3.pack(side=LEFT, padx=5, pady=5)

        entry3 = Entry(frame4, textvariable=num1)
        entry3.pack(fill=X, padx=5, expand=True)

    def errorMsg(self,msg):
        pass

    def plus(self):
        try:
            value=float(num1.get())+float(num2.get())
            res.set(self.makeResult(value))
        except:
            self.errorMsg('잘못된 연산')


    def mul(self):
        try:
            value = float(num1.get()) * float(num2.get())
            res.set(self.makeResult(value))
        except:
            self.errorMsg('잘못된 연산')

    def minus(self):
        try:
            value = float(num1.get()) - float(num2.get())
            res.set(self.makeResult(value))
        except:
            self.errorMsg('잘못된 연산')

    def div(self):
        try:
            value = float(num1.get()) / float(num2.get())
            res.set(self.makeResult(value))
        except:
            self.errorMsg('잘못된 연산')
    def makeResult(self,value):
        if (value==int(value)):
            value=int(value)
        return value

class CalUI:
    def __init__(self):
        pass

    @staticmethod
    def main():
        root = Tk()
        root.title("계산기")
        w = 300
        h = 200
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        root.geometry("%dx%d+%d+%d" % (w, h, x, y))
        root.resizable(FALSE, FALSE)
        root.geometry("380x200")  # 소문자 x
        app = App(root)
        root.mainloop()
