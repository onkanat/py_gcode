#https://www.golinuxcloud.com/python-subprocess/
#https://www.pythontutorial.net/tkinter/
version = '0.01.0'

import subprocess as sb
import tkinter as tk
import os
import sys
import configparser
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog,Frame,Menu
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import asksaveasfile,askdirectory

class App(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createmenu()
        self.butonlar()
        self.edit()


    def createmenu(self):
        
        #Create the Menu base
        self.menu = Menu(self)
        #Add the Menu
        self.master.config(menu=self.menu)
        #Create our File menu
        self.FileMenu = Menu(self.menu)
        #Add our Menu to the Base Menu
        self.menu.add_cascade(label='File', menu=self.FileMenu)
        #Add items to the menu
        self.FileMenu.add_command(label='New', command=self.ClearTextBox)
        self.FileMenu.add_command(label='Open', command=self.Simple)
        self.FileMenu.add_separator()
        self.FileMenu.add_command(label='Save', command=self.WriteToFile)
        self.FileMenu.add_separator()
        self.FileMenu.add_command(label='Quit', command=self.quit)
        
        self.EditMenu = Menu(self.menu)
        self.menu.add_cascade(label='Edit', menu=self.EditMenu)
        self.EditMenu.add_command(label='Copy       ctrl+c', command=self.CopyClpBd)
        self.EditMenu.add_command(label='Paste       ctrl+p',command=self.Paste)
        self.EditMenu.add_command(label='Select All', command=self.SelectAllText)
        self.EditMenu.add_command(label='Delete All', command=self.ClearTextBox)
        self.EditMenu.add_separator()
        #self.EditMenu.add_command(label='Save Preferences', command=self.SavePrefs)
        #self.EditMenu.add_command(label='Load Preferences', command=self.LoadPrefs)
        
        self.HelpMenu = Menu(self.menu)
        self.menu.add_cascade(label='Help', menu=self.HelpMenu)
        self.HelpMenu.add_command(label='Help Info', command=self.HelpInfo)
        self.HelpMenu.add_command(label='About', command=self.HelpAbout)

    def butonlar(self): # BUTONLARIN ÜZERİNE .PNG KONACAK !!!!!
        self.EntryFrame = Frame(self,bd=5)
        self.EntryFrame.grid(row=1, column=6)
        tk.Button(self.EntryFrame,text="face",command=self.face).grid(row=1,column=0)
        tk.Button(self.EntryFrame,text="grid",command=self.Grid).grid(row=1,column=1)
        tk.Button(self.EntryFrame,text="grill",command=self.grill).grid(row=1,column=2)
        tk.Button(self.EntryFrame,text="boltcircle",command=self.boltcircle).grid(row=1,column=3)
        tk.Button(self.EntryFrame,text="counterbore",command=self.counterbore).grid(row=1,column=4)
        tk.Button(self.EntryFrame,text="bezel",command=self.bezel).grid(row=1,column=5)
        tk.Button(self.EntryFrame,text="arcgen",command=self.arcgen).grid(row=1,column=6)

    def edit(self):# SAVE OPEN SELECT VS... İLAVE
        self.TextFrame = Frame(self,bd=5)
        self.TextFrame.grid(row=2,column=6)
        self.g_code = ScrolledText(self.TextFrame)
        self.g_code.grid(row=2,column=0)
    
    def CopyClpBd(self):
        self.g_code.clipboard_clear()
        self.g_code.clipboard_append(self.g_code.get(0.0, tk.END))

    def Paste(self):
        self.g_code.insert(tk.END,self.g_code.clipboard_get())

    def WriteToFile(self):
        self.NewFileName = asksaveasfile(initialdir=self.GetIniData('face.ini','Directories','NcFiles',os.path.expanduser("~")),mode='w', \
		master=self.master,title='Create NC File',defaultextension='.ngc')
        self.NcDir=os.path.dirname(self.NewFileName.name)
        self.NewFileName.write(self.g_code.get(0.0, tk.END))
        self.NewFileName.close()

    def GetIniData(self,FileName,SectionName,OptionName,default=''):
        """
        Returns the data in the file, section, option if it exists
        of an .ini type file created with ConfigParser.write()
        If the file is not found or a section or an option is not found
        returns an exception
        """
        self.cp =  configparser.ConfigParser()
        try:
            self.cp.read_file(open(FileName,'r'))
            try:
                self.cp.has_section(SectionName)
                try:
                    IniData=self.cp.get(SectionName,OptionName)
                except:
                    IniData=default
            except:
                IniData=default
        except:
            IniData=default
        return IniData


    def WriteIniData(self,FileName,SectionName,OptionName,OptionData):
        """
        Pass the file name, section name, option name and option data
        When complete returns 'sucess'
        """
        self.cp = configparser.ConfigParser()
        try:
            self.fn=open(FileName,'a')
        except IOError:
            self.fn=open(FileName,'w')
        if not self.cp.has_section(SectionName):
            self.cp.add_section(SectionName)
        self.cp.set(SectionName,OptionName,OptionData)
        self.cp.write(self.fn)
        self.fn.close()

    '''
    def LoadPrefs(self):
        self.NcDir=self.GetIniData('face.ini','Directories','NcFiles',os.path.expanduser("~"))
        self.FeedrateVar.set(self.GetIniData('face.ini','MillingPara','Feedrate','1000'))
        self.DepthOfCutVar.set(self.GetIniData('face.ini','MillingPara','DepthOfCut','3'))
        self.ToolDiameterVar.set(self.GetIniData('face.ini','MillingPara','ToolDiameter','10'))
        self.SpindleRPMVar.set(self.GetIniData('face.ini','MillingPara','SpindleRPM','9000'))
        self.StepOverVar.set(self.GetIniData('face.ini','MillingPara','StepOver','50'))
        self.LeadinVar.set(self.GetIniData('face.ini','MillingPara','Leadin'))
        self.UnitVar.set(int(self.GetIniData('face.ini','MillingPara','UnitVar','2')))
        self.HomeVar.set(int(self.GetIniData('face.ini','MillingPara','HomeVar','4')))
        self.SafeZVar.set(self.GetIniData('face.ini','MillingPara','SafeZ','10.0'))
        self.PartLengthVar.set(self.GetIniData('face.ini','Part','X'))
        self.PartWidthVar.set(self.GetIniData('face.ini','Part','Y'))
        self.TotalToRemoveVar.set(self.GetIniData('face.ini','Part','TotalToRemove'))


    def SavePrefs(self):
        def set_pref(SectionName,OptionName,OptionData):
            if not self.cp.has_section(SectionName):
                self.cp.add_section(SectionName)
            self.cp.set(SectionName,OptionName,OptionData)
        self.cp=configparser.ConfigParser()
        self.fn=open('face.ini','w')
        set_pref('Directories','NcFiles',self.NcDir)
        set_pref('MillingPara','Feedrate',self.FeedrateVar.get())
        set_pref('MillingPara','DepthOfCut',self.DepthOfCutVar.get())
        set_pref('MillingPara','ToolDiameter',self.ToolDiameterVar.get())
        set_pref('MillingPara','SpindleRPM',self.SpindleRPMVar.get())
        set_pref('MillingPara','StepOver',self.StepOverVar.get())
        set_pref('MillingPara','Leadin',self.LeadinVar.get())
        set_pref('MillingPara','UnitVar',self.UnitVar.get())
        set_pref('MillingPara','HomeVar',self.HomeVar.get())
        set_pref('MillingPara','SafeZ',self.SafeZVar.get())
        set_pref('Part','X',self.PartLengthVar.get())
        set_pref('Part','Y',self.PartWidthVar.get())
        set_pref('Part','TotalToRemove',self.TotalToRemoveVar.get())
        self.cp.write(self.fn)
        self.fn.close()
        '''

    def Simple(self):
        messagebox.showinfo('Feature', 'Sorry this Feature has\nnot been programmed yet.')

    def ClearTextBox(self):
        self.g_code.delete(1.0,tk.END)

    def SelectAllText(self):
        self.g_code.tag_add(tk.SEL, '1.0', tk.END)

    def SelectCopy(self):
        self.SelectAllText()
        self.CopyClpBd()

    def HelpInfo(self):
        simpledialog.SimpleDialog(self,
            text='Required fields are:\n'
            'Part Width & Length,\n'
            'Amount to Remove,\n'
            'and Feedrate\n'
            'Fractions can be entered in most fields',
            title='Yüzey silmek için gerekenler',
            buttons=['OK'],
            default='none').go()

    def HelpAbout(self):
        messagebox.showinfo('Help About', 'Programmed by\n'
            'Big John T (AKA John Thornton)\n'
            'Rick Calder\n'
            'Brad Hanken\n'
            'Aglef Kaiser\n'
            'Version ' + version)

### TÜM BUTONLARIN YERLERİ GÜNCELLENECEK ###
    def Grid(self):
        a = sb.run('python3 py3w_grid.py',capture_output=True)
        self.g_code.insert(tk.END,a.stdout)
        
    def grill(self):
        a = sb.run('python.exe py3w_grill.py',capture_output=True)
        self.g_code.insert(tk.END,a.stdout)
        
    def boltcircle(self):
        a = sb.run('python.exe py3w_boltcircle.py',capture_output=True)
        self.g_code.insert(tk.END,a.stdout)
        
    def counterbore(self):
        a = sb.run('python.exe py3w_counterbore.py',capture_output=True)
        self.g_code.insert(tk.END,a.stdout)
        
    def bezel(self):    
        a = sb.run('python.exe py3w_bezel.py',capture_output=True)
        self.g_code.insert(tk.END,a.stdout)
            
    def arcgen(self):    
        a = sb.run('python.exe py3w_arcgen-mill.py',capture_output=True)
        self.g_code.insert(tk.END,a.stdout)

    def face(self):    
        a = sb.run('python.exe py3w_face.py',capture_output=True)
        self.g_code.insert(tk.END,a.stdout)
        
ap = App()
ap.master.title("programlar")
ap.mainloop()
