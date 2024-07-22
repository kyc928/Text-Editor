import tkinter as tk
from tkinter import filedialog, messagebox

fileName = None

def newFile():
    global fileName
    fileName = "Untitled"
    text.delete(1.0, tk.END)

def saveFile():
    global fileName
    if fileName is None:
        saveAs()
    else:
        t = text.get(1.0, tk.END)
        with open(fileName, 'w') as f:
            f.write(t)

def saveAs():
    global fileName
    f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(1.0, tk.END)
    try:
        if f is not None:
            f.write(t.rstrip())
            fileName = f.name
    except Exception as e:
        messagebox.showerror(title="Oops!", message=f"Unable to save file...\n{e}")

def openFile():
    global fileName
    f = filedialog.askopenfile(mode='r')
    if f is not None:
        fileName = f.name
        t = f.read()
        text.delete(1.0, tk.END)
        text.insert(1.0, t)

root = tk.Tk()
root.title("Notepad")
root.minsize(width=500, height=500)
root.maxsize(width=500, height=500)

text = tk.Text(root, width=400, height=400)
text.pack()

menubar = tk.Menu(root)
fileMenu = tk.Menu(menubar)
fileMenu.add_command(label="New", command=newFile)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_command(label="Save As...", command=saveAs)
fileMenu.add_separator()
fileMenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=fileMenu)

root.config(menu=menubar)
root.mainloop()
