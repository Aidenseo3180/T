
from os import system
from tkinter import *
import tkinter as tk

root = tk.Tk() #master

root.title("Twitch Downloader")
root.geometry("540x400+500+100")
root.resizable(True,True)
root.configure(bg = 'white')    #background color = white

def retrieve_input():
    input = text.get("1.0","end") #gets input from text
    #first string to the end of the string (first character in text widget is 1.0)
    print(input)




label = Label(root,text="Python",width = 10, height = 1, fg = "blue", relief = "solid")
text = tk.Text(root, height = 20, width = 40)

btn1 = tk.Button(root, text = "Proceed")
btn2 = tk.Button(root, text = "How to Use")
btn3 = tk.Button(root, text = "About")

#btn_file = tk.Button(root, height = 1, width = 10, text = "Read", command = retrieve_input)

#packs
label.pack()
text.pack()
btn1.pack()
btn2.pack()
btn3.pack()

#btn.pack()

#root.clear("all")

root.mainloop()

#https://076923.github.io/posts/Python-tkinter-3/


#file_directory = input("Enter the file directory where you have ffmpeg.exe (copy&paste recommended) : ")
#twitch_image_link = input("Enter the image link of the twitch video that you want to download (copy&paste recommended) :")

#print(file_directory)
#os.system(f"start cmd /k cd {file_directory}")  #opens the cmd from ffpmeg exe location





