#!/usr/bin/env python
#-*-coding:utf-8-*-



from tkinter import *

class Uygulama(object):
    def __init__(self):
        self.guiPenAr()
        self.gV()

    def gV(self):
        self.depo = ""

    def guiPenAr(self):
        
        self.ekrano = Text(width=20,height=5)
        self.ekran = Entry(width=20)
        self.ekrano.grid(row=0, column=0, columnspan=3,ipady=4)
        self.ekran.grid(row=1, column=0, columnspan=3,ipady=4)

        self.liste = [\
                    "7", "8", "9",
                    "4", "5", "6",
                    "1", "2", "3",
                    "+", "0", "-",
                    "/", "*", "=",
                    "C"
                    ]

        self.sira = 2
        self.sutun = 0

        
        for i in self.liste:
            self.komut = lambda x=i: self.hesapla(x)
            Button(text=i,
                   width=5,
                   relief=GROOVE,
                   command=self.komut).grid(row=self.sira,
                                            column=self.sutun)
            self.sutun += 1

            if self.sutun > 2: # sütun sayısı -1
                self.sutun = 0
                self.sira += 1
    
    def key_handler(self, event):
        print(event) # () ağırlık hesaplama ilave 
        if event.char in '0123456789':
            self.depo = self.depo+event.char

        if event.char in '+-/*':
            self.depo = self.depo+event.char

        if event.char in '\r':
            self.ekran.delete(0,END)
            ans = self.hp(self.depo)
            self.ekran.insert(END,ans)

        if event.char in 'cC':
            self.ekran.delete(0,END)
            self.depo = ""

    def hp(self, gelen):
        self.gelen = gelen
        self.hep = eval(self.gelen,{"__builtins__":None},{})
        return self.hep

    def hesapla(self, tus):
        self.tus = tus
        if self.tus in "0123456789":
            self.ekran.insert(END,self.tus)
            self.depo = self.depo + self.tus

        if self.tus in "+-/*":
            self.depo = self.depo + self.tus
            self.ekran.delete(0,END)

        if self.tus == "=":
            self.ekran.delete(0,END)
            self.hesap = eval(self.depo,{"__builtins__":None},{})
            self.depo = str(self.hesap)
            self.ekran.insert(END,self.depo)

        if self.tus == "C":
            self.ekran.delete(0,END)
            self.depo = ""

pencere = Tk()
uyg = Uygulama()

pencere.bind("<Key>", uyg.key_handler)
pencere.resizable(width=FALSE,height=FALSE)


mainloop()
