import tkinter as tk
from tkinter.filedialog import *
import re
import json
root = tk.Tk()
root.option_add('*font',['TsukuARdGothic-Regular',20])
root.attributes("-fullscreen", True)
root.resizable(0,0)

def capture():
    Data = right.get(1.0, tk.END)
    string = re.findall(r"u'.*'", Data)
    json.dump(string, open('data.json', 'w'), ensure_ascii=False)
    Data = re.sub(r"u'.*'", "ǽ", Data)
    root.clipboard_clear()
    root.clipboard_append(Data)
    right.delete(1.0, tk.END)
    right.insert(1.0, 'クリップボードへコピーされました')
def takeout():
    Data = right.get(1.0, tk.END)
    string = json.load(open('data.json', 'r'))
    for i in range(len(string)):
        Data = Data.replace("ǽ", string[i], 1)
    with open('pyfile/name.py', mode='w') as f:
        f.write(Data)
    right.delete(1.0, tk.END)
    right.insert(1.0, 'pyfile/name.pyに生成されました')
def clear():
    json.dump([], open('data.json', 'w'))
    right.delete(1.0, tk.END)

def file_open():
    f = open(askopenfilename(filetypes=[('*.py','*.py')]))
    right.delete(0.0, tk.END)
    right.insert(1.0, f.read())
    f.close()

def select():
    if commands.selection_includes(0)==1:
        file_open()
    elif commands.selection_includes(1)==1:
        capture()
    elif commands.selection_includes(2)==1:
        takeout()
    elif commands.selection_includes(3)==1:
        clear()
    else:
        return

left = tk.Frame(root)
left.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))

commands = tk.Listbox(left, listvariable=tk.StringVar(value=('FILE_OPEN', 'CAPTURE', 'TAKEOUT', 'CLEAR')))
commands.grid(column=0, row=0)

runbtn = tk.Button(left, text="RUN", command=select)
runbtn.grid(column=0, row=1, sticky=(tk.N, tk.S, tk.W, tk.E))

right = tk.Text()
right.insert(1.0, 'Copy&Paste')
right.grid(column=1, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))

root.mainloop()