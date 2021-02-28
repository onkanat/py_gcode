#!<UTF-8>
# Importing Required libraries & Modules
import subprocess as sb
from tkinter import *
from tkinter import messagebox, filedialog

# Defining TextEditor Class
class TextEditor:

	# Defining Constructor
	def __init__(self,root):
		self.root = root
		self.root.title("TEXT EDITOR")
		self.root.geometry("1200x700+200+150")
		# Initializing filename
		self.filename = None
		# Declaring Title variable
		self.title = StringVar()
		# Declaring Status variable
		self.status = StringVar()

		# Creating Titlebar
		self.titlebar = Label(self.root,textvariable=self.title,
		font=("times new roman",15,"bold"),bd=2,relief=GROOVE)
		self.titlebar.pack(side=TOP,fill=BOTH)
		self.settitle()

		# Creating Statusbar
		self.statusbar = Label(self.root,textvariable=self.status,
		font=("times new roman",15,"bold"),bd=2,relief=GROOVE)
		self.statusbar.pack(side=BOTTOM,fill=BOTH)
		self.status.set("Welcome To Text Editor")

		# Creating Menubar
		self.menubar = Menu(self.root,font=("times new roman",15,"bold"),
		activebackground="skyblue")
		self.root.config(menu=self.menubar)

		# Creating File Menu
		self.filemenu = Menu(self.menubar,font=("times new roman",12,"bold"),
		activebackground="skyblue",tearoff=0)
		# Adding New file Command
		self.filemenu.add_command(label="New",accelerator="Ctrl+N",command=self.newfile)
		# Adding Open file Command
		self.filemenu.add_command(label="Open",accelerator="Ctrl+O",command=self.openfile)
		# Adding Save File Command
		self.filemenu.add_command(label="Save",accelerator="Ctrl+S",command=self.savefile)
		# Adding Save As file Command
		self.filemenu.add_command(label="Save As",accelerator="Ctrl+A",command=self.saveasfile)
		# Adding Seprator
		self.filemenu.add_separator()
		# Adding Exit window Command
		self.filemenu.add_command(label="Exit",accelerator="Ctrl+E",command=self.exit)
		# Cascading filemenu to menubar
		self.menubar.add_cascade(label="File", menu=self.filemenu)

		# Creating Edit Menu
		self.editmenu = Menu(self.menubar,font=("times new roman",12,"bold"),
		activebackground="skyblue",tearoff=0)
		# Adding Cut text Command
		self.editmenu.add_command(label="Cut",accelerator="Ctrl+X",command=self.cut)
		# Adding Copy text Command
		self.editmenu.add_command(label="Copy",accelerator="Ctrl+C",command=self.copy)
		# Adding Paste text command
		self.editmenu.add_command(label="Paste",accelerator="Ctrl+V",command=self.paste)
		# Adding Seprator
		self.editmenu.add_separator()
		
		# düzelt iki tane copyalıyor ????
		self.editmenu.add_command(label="Select All",accelerator="Ctlr+Shift+S",command=self.SelectAllText)
		# Adding Undo text Command
		self.editmenu.add_command(label="Undo",accelerator="Ctrl+U",command=self.undo)
		# Cascading editmenu to menubar
		self.menubar.add_cascade(label="Edit", menu=self.editmenu)

		# Creating Uygulama Menu
		self.uygulama = Menu(self.menubar,font=("times new roman",12,"bold"),
		activebackground="skyblue",tearoff=0)
		# Adding Arc
		self.uygulama.add_command(label="Arc",accelerator="Ctrl+Shift+A",command=self.arcgen)
		# Adding Bezel
		self.uygulama.add_command(label="Bezel",accelerator="Ctrl+Shift+B",command=self.bezel)
		# Adding Boltcircle
		self.uygulama.add_command(label="BoLtCircle",accelerator="Ctrl+Shift+L",
		command=self.boltcircle)
		# Adding Counterbore
		self.uygulama.add_command(label="CounterBore",accelerator="Ctrl+Shift+C",
		command=self.counterbore)
		# Adding Face
		self.uygulama.add_command(label="Face",accelerator="Ctrl+Shift+F",command=self.face)
		# Adding Grig
		self.uygulama.add_command(label="Grid",accelerator="Ctrl+Shift+G",command=self.Grid)
		# Adding Grill
		self.uygulama.add_command(label="GriLl",accelerator="Ctrl+Shift+R",command=self.grill)
		# Cascadin Uygulama Menu to menubar
		self.menubar.add_cascade(label="Uygulama", menu=self.uygulama)

		# Creating Help Menu
		self.helpmenu = Menu(self.menubar,font=("times new roman",12,"bold"),
		activebackground="skyblue",tearoff=0)
		# Adding About Command
		self.helpmenu.add_command(label="About",command=self.infoabout)
		# Cascading helpmenu to menubar
		self.menubar.add_cascade(label="Help", menu=self.helpmenu)

		# Creating Scrollbar
		scrol_y = Scrollbar(self.root,orient=VERTICAL)
		# Creating Text Area
		self.txtarea = Text(self.root,yscrollcommand=scrol_y.set,
		font=("times new roman",15,"bold"),state="normal",relief=GROOVE)
		# Packing scrollbar to root window
		scrol_y.pack(side=RIGHT,fill=Y)
		# Adding Scrollbar to text area
		scrol_y.config(command=self.txtarea.yview)
		# Packing Text Area to root window
		self.txtarea.pack(fill=BOTH,expand=1)
		# Calling shortcuts funtion
		self.shortcuts()

	# Defining settitle function
	def settitle(self):
		# Checking if Filename is not None
		if self.filename:
			# Updating Title as filename
			self.title.set(self.filename)
		else:
			# Updating Title as Untitled
			self.title.set("Untitled")

	# Defining New file Function
	def newfile(self,*args):
		# Clearing the Text Area
		self.txtarea.delete("1.0",END)
		# Updating filename as None
		self.filename = None
		# Calling settitle funtion
		self.settitle()
		# updating status
		self.status.set("New File Created")

	# Defining Open File Funtion
	def openfile(self,*args):
		# Exception handling
		try:
			# Asking for file to open
			self.filename = filedialog.askopenfilename(title = "Select file",
			filetypes = [("All Files","*.*"),
						("Text Files","*.txt"),
						("Python Files","*.py"),
						("Markdown Documents", "*.md"),
						("JavaScript Files", "*.js"),
						("HTML Documents", "*.html"),
						("CSS Documents", "*.css"),
						("G Code Files", "*.gcn")])
			# checking if filename not none
			if self.filename:
				# opening file in readmode
				infile = open(self.filename,"r")
				# Clearing text area
				self.txtarea.delete("1.0",END)
				# Inserting data Line by line into text area
				for line in infile:
    					if line != '\n':
    							self.txtarea.insert(END,str(line))
				# Closing the file  
				infile.close()
				# Calling Set title
				self.settitle()
				# Updating Status
				self.status.set("Opened Successfully")
		except Exception as e:
			messagebox.showerror("Exception",e)

	# Defining Save File Funtion
	def savefile(self,*args):
		# Exception handling
		try:
			# checking if filename not none
			if self.filename:
				# Reading the data from text area
				data = self.txtarea.get("1.0",END)
				# opening File in write mode
				outfile = open(self.filename,"w")
				# Writing Data into file
				outfile.write(data)
				# Closing File
				outfile.close()
				# Calling Set title
				self.settitle()
				# Updating Status
				self.status.set("Saved Successfully")
			else:
				self.saveasfile()
		except Exception as e:
			messagebox.showerror("Exception",e)

	# Defining Save As File Funtion
	def saveasfile(self,*args):
		# Exception handling
		try:
			# Asking for file name and type to save
			untitledfile = filedialog.asksaveasfilename(title = "Save file As",
			defaultextension=".txt",initialfile = "Untitled.txt",
			filetypes=[("All Files", "*.*"),
                        ("Text Files", "*.txt"),
                        ("Python Scripts", "*.py"),
                        ("Markdown Documents", "*.md"),
                        ("JavaScript Files", "*.js"),
                        ("HTML Documents", "*.html"),
                        ("CSS Documents", "*.css"),
						("G Code Files", "*.gcn")])
			# Reading the data from text area
			data = self.txtarea.get("1.0",END)
			# opening File in write mode
			outfile = open(untitledfile,"w")
			# Writing Data into file
			outfile.write(data)
			# Closing File
			outfile.close()
			# Updating filename as Untitled
			self.filename = untitledfile
			# Calling Set title
			self.settitle()
			# Updating Status
			self.status.set("Saved Successfully")
		except Exception as e:
			messagebox.showerror("Exception",e)

	# Defining Exit Funtion
	def exit(self,*args):
		op = messagebox.askyesno("WARNING","Your Unsaved Data May be Lost!!")
		if op>0:
			self.root.destroy()
		else:
			return

	def SelectAllText(self,*args):
		self.txtarea.tag_add(SEL, '1.0', END)

	# Defining Cut Funtion
	def cut(self,*args):
		self.txtarea.event_generate("<<Cut>>")

	# Defining Copy Funtion
	def copy(self,*args):
		self.txtarea.event_generate("<<Copy>>")

	# Defining Paste Funtion
	def paste(self,*args):
		self.txtarea.event_generate("<<Paste>>")

	# Defining Undo Funtion
	def undo(self,*args):
		# Exception handling
		try:
			# checking if filename not none
			if self.filename:
				# Clearing Text Area
				self.txtarea.delete("1.0",END)
				# opening File in read mode
				infile = open(self.filename,"r")
				# Inserting data Line by line into text area
				for line in infile:
					self.txtarea.insert(END,line)
				# Closing File
				infile.close()
				# Calling Set title
				self.settitle()
				# Updating Status
				self.status.set("Undone Successfully")
			else:
				# Clearing Text Area
				self.txtarea.delete("1.0",END)
				# Updating filename as None
				self.filename = None
				# Calling Set title
				self.settitle()
				# Updating Status
				self.status.set("Undone Successfully")
		except Exception as e:
			messagebox.showerror("Exception",e)

	# Defining About Funtion
	def infoabout(self):
		messagebox.showinfo("About Text Editor","A Simple Text Editor\nCreated using Python.")

	# Defining shortcuts Funtion
	def shortcuts(self):
		# Binding Ctrl+n to newfile funtion
		self.txtarea.bind("<Control-n>",self.newfile)
		# Binding Ctrl+o to openfile funtion
		self.txtarea.bind("<Control-o>",self.openfile)
		# Binding Ctrl+s to savefile funtion
		self.txtarea.bind("<Control-s>",self.savefile)
		# Binding Ctrl+a to saveasfile funtion
		self.txtarea.bind("<Control-a>",self.saveasfile)
		# Binding Ctrl+e to exit funtion
		self.txtarea.bind("<Control-e>",self.exit)
		# Binding Ctrl+x to cut funtion
		self.txtarea.bind("<Control-x>",self.cut)
		# Binding Ctrl+c to copy funtion
		self.txtarea.bind("<Control-c>",self.copy)
		# Binding Ctrl+v to paste funtion
		self.txtarea.bind("<Control-v>",self.paste)
		# Binding Ctrl+u to undo funtion
		self.txtarea.bind("<Control-u>",self.undo)

		self.txtarea.bind("<Control-Shift-S>",self.SelectAllText)
		self.txtarea.bind("<Control-Shift-A>",self.arcgen)
		self.txtarea.bind("<Control-Shift-B>",self.bezel)
		self.txtarea.bind("<Control-Shift-L>",self.boltcircle)
		self.txtarea.bind("<Control-Shift-C>",self.counterbore)
		self.txtarea.bind("<Control-Shift-F>",self.face)
		self.txtarea.bind("<Control-Shift-G>",self.Grid)
		self.txtarea.bind("<Control-Shift-R>",self.grill)
		
	# Uygulamalar
	def Grid(self,*args):
		a = sb.run('python.exe py3w_grid.py',capture_output=True)
		self.txtarea.insert(END,a.stdout)
				
	def grill(self,*args):
		a = sb.run('python.exe py3w_grill.py',capture_output=True)
		self.txtarea.insert(END,a.stdout)

	def boltcircle(self,*args):
		a = sb.run('python.exe py3w_boltcircle.py',capture_output=True)
		self.txtarea.insert(END,a.stdout)
				
	def counterbore(self,*args):
		a = sb.run('python.exe py3w_counterbore.py',capture_output=True)
		self.txtarea.insert(END,a.stdout)
				
	def bezel(self,*args):    
		a = sb.run('python.exe py3w_bezel.py',capture_output=True)
		self.txtarea.insert(END,a.stdout)
						
	def arcgen(self,*args):    
		a = sb.run('python.exe py3w_arcgen-mill.py',capture_output=True)
		self.txtarea.insert(END,a.stdout)

	def face(self,*args):    
		a = sb.run('python.exe py3w_face.py',capture_output=True)
		self.txtarea.insert(END,a.stdout)





# Creating TK Container
root = Tk()
# Passing Root to TextEditor Class
TextEditor(root)
# Root Window Looping
root.mainloop()