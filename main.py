#https://www.golinuxcloud.com/python-subprocess/
import subprocess as sb
import tkinter as tk
import os
import sys
from tkinter import filedialog,Frame

class App(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.butonlar()
        self.edit()
        
    
    def butonlar(self): # BUTONLARIN ÜZERİNE .PNG KONACAK !!!!!
        self.EntryFrame = Frame(self,bd=5)
        self.EntryFrame.grid(row=0, column=6)
        tk.Button(self.EntryFrame,text="grid",command=self.py3w_grid).grid(row=1,column=1)
        tk.Button(self.EntryFrame,text="grill",command=self.grill).grid(row=1,column=2)
        tk.Button(self.EntryFrame,text="boltcircle",command=self.boltcircle).grid(row=1,column=3)
        tk.Button(self.EntryFrame,text="counterbore",command=self.counterbore).grid(row=1,column=4)
        tk.Button(self.EntryFrame,text="bezel",command=self.bezel).grid(row=1,column=5)
        tk.Button(self.EntryFrame,text="arcgen",command=self.arcgen).grid(row=1,column=6)

    def edit(self):# SAVE OPEN SELECT VS... İLAVE 
        self.TextFrame = Frame(self,bd=5)
        self.TextFrame.grid(row=1,column=6)
        self.gc = tk.Text(self.TextFrame)
        self.gc.grid(row=2,column=0)

### TÜM BUTONLARIN YERLERİ GÜNCELLENECEK ###         
    def py3w_grid(self):
        a = sb.run('python.exe py3w_grid.py',capture_output=True)
        self.gc.insert(tk.END,a.stdout)
        print(a.stdout)

    def grill(self):
        a = sb.run('python.exe py3w_grill.py',capture_output=True)
        self.gc.insert(tk.END,a.stdout)
        print(a.stdout) 

    def boltcircle(self):
        a = sb.run('python.exe py3w_boltcircle.py',capture_output=True)
        self.gc.insert(tk.END,a.stdout)
        print(a.stdout)               

    def counterbore(self):
        a = sb.run('python.exe py3w_counterbore.py',capture_output=True)
        self.gc.insert(tk.END,a.stdout)
        print(a.stdout)  

    def bezel(self):    
        a = sb.run('python.exe py3w_bezel.py',capture_output=True)
        self.gc.insert(tk.END,a.stdout)
        print(a.stdout)  
    
    def arcgen(self):    
        a = sb.run('python.exe py3w_arcgen-mill.py',capture_output=True)
        self.gc.insert(tk.END,a.stdout)
        print(a.stdout)

ap = App()
ap.master.title("programlar")
ap.mainloop()
