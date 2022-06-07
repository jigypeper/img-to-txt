from fileinput import filename
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\hagi-1\AppData\Local\Programs\Tesseract-OCR\tesseract' 

img_file = ''
file_dir = ''
string = ''
#text = pytesseract.image_to_string(img_file)
#direc = fd.askdirectory(initialdir = "C:/",title = "choose save directory")

def write_file():
    global img_file, file_name, file_dir, string
    text = pytesseract.image_to_string(img_file)
    if str(string) != '' and file_dir != '':
        with open(file_dir + '/' + str(string) + '.txt', 'w') as f:
            f.write(text)
    else:
        with open('text-in-file.txt', 'w') as f:
            f.write(text)
    label1['text'] = '"' + file_dir + '/' + str(string) + '.txt' + '"' + ' Created!'

def run_help():
    helproot = tk.Tk()
    help_text = tk.Text(helproot, height=20, width=100)
    helproot.title('Instructions')
    help_text.pack()
    help_text.insert(tk.END, "1. Select the image file\n2. Press the 'Run' button\n3. Find your file\nNote: It will overwrite the file when you run again unless you rename it\n")
    helproot.mainloop()


root = tk.Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label='Help', menu=subMenu)
subMenu.add_command(label='How to use', command= run_help)

root.title('Write Image to TXT file')
root.geometry('800x216')#('800x92')  #root.geometry('400x140')

def open_file():
    global img_file
    root.filename = fd.askopenfilename(initialdir = "C:/",title = "choose your file",filetypes = (("png files","*.png"),("bitmap", "*.bmp"),("jpeg files", "*.jpeg, *.jpg"),))
    img_file = root.filename
    c = "Selected file: " + img_file
    label2['text'] = c

def save_dir():
    global file_dir
    file_dir = fd.askdirectory()



def write_to_txt(imgfile):
    global img_file
    text = pytesseract.image_to_string(imgfile)
    return text

file_name = Entry(root)

def set_name():
    global file_name, string
    string = file_name.get()
    label3['text'] = "File Name: " + string
    #return string

#string = set_name()

button1 = tk.Button(root, text= 'Open Image File', width= 800, command= open_file)
button2 = tk.Button(root, text= 'Set Save Directory', width= 800, command= save_dir)
button3 = tk.Button(root, text= 'Run', width= 800, command= write_file)
button4 = tk.Button(root, text= 'Set File Name', width= 800, command= set_name)
label4 = tk.Label(root, text= 'File Name: ', width=800)
button1.pack()
button2.pack()
label4.pack()
file_name.pack(padx=5, pady=5)
button4.pack(padx=1, pady=1)
button3.pack()
label1 = tk.Label(root, text= '', bd=1, relief=SUNKEN, anchor=W)
#label1 = tk.Label(root, text= file_csv, bg="black", fg="white", width=400)
label2 = tk.Label(root, text= img_file, bg="black", fg="white", width=800)
label3 = tk.Label(root, text= '', bg="black", fg="white", width=800)
label2.pack()
label3.pack()
label1.pack(side=BOTTOM, fill=X)
root.mainloop()
