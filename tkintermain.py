import tkinter as tk
import tkinter.font as tkFont

import infer
import time

from tkinter import *
from PIL import ImageTk,Image  
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import os
import shutil

from tkHyperLinkManager import HyperlinkManager
import webbrowser
from functools import partial


class App:

    def __init__(self, root):
        #setting title
        root.title("AI Image")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_727=tk.Label(root)
        GLabel_727["bg"] = "#F2F0EC"
        ft = tkFont.Font(family='Times',size=17)
        GLabel_727["font"] = ft
        GLabel_727["fg"] = "#333333"
        GLabel_727["justify"] = "center"
        GLabel_727["text"] = "AI Image"
        GLabel_727.place(x=270,y=70,width=71,height=30)

        GLabel_150=tk.Label(root)
        GLabel_150["bg"] = "#F2F0EC"
        GLabel_150["disabledforeground"] = "#000000"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_150["font"] = ft
        GLabel_150["fg"] = "#333333"
        GLabel_150["justify"] = "center"
        GLabel_150["text"] = "Convert your current images to an aged version in seconds for free."
        GLabel_150.place(x=110,y=120,width=410,height=30)

        GButton_84=tk.Button(root)
        GButton_84["activebackground"] = "#ff0000"
        GButton_84["activeforeground"] = "#ff0000"
        GButton_84["anchor"] = "center"
        GButton_84["bg"] = "#ff0000"
        GButton_84["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=21)
        GButton_84["font"] = ft
        GButton_84["fg"] = "#ff0000"
        GButton_84["justify"] = "center"
        GButton_84["text"] = "Select\nJPG/PNG\nImages"
        GButton_84["relief"] = "flat"
        GButton_84.place(x=220,y=190,width=158,height=163)
        GButton_84["command"] = self.GButton_84_command

        GLabel_577=tk.Label(root)
        GLabel_577["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_577["font"] = ft
        GLabel_577["fg"] = "#333333"
        GLabel_577["justify"] = "center"
        GLabel_577["text"] = ""
        GLabel_577.place(x=0,y=0,width=597,height=47)

        GLabel_661=tk.Label(root)
        GLabel_661["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_661["font"] = ft
        GLabel_661["fg"] = "#333333"
        GLabel_661["justify"] = "center"
        GLabel_661["text"] = ""
        GLabel_661.place(x=0,y=470,width=598,height=30)

        GLabel_776=tk.Label(root)
        ft = tkFont.Font(family='Times',size=7)
        GLabel_776["font"] = ft
        GLabel_776["bg"] = "#ffffff"
        GLabel_776["fg"] = "#333333"
        GLabel_776["justify"] = "center"
        GLabel_776["text"] = "© AI image 2022® - Image Aging using AI"
        GLabel_776.place(x=0,y=470,width=154,height=30)

        # GLabel_842=tk.Label(root)
        # ft = tkFont.Font(family='Times',size=10)
        # GLabel_842["font"] = ft
        # GLabel_842["bg"] = "#ffffff"
        # GLabel_842["fg"] = "#d34238"
        # GLabel_842["justify"] = "center"
        # GLabel_842["text"] = "About Us"
        # GLabel_842.place(x=510,y=10,width=70,height=25)

        GLabel_190=tk.Label(root)
        ft = tkFont.Font(family='Times',size=19)
        GLabel_190["font"] = ft
        GLabel_190["bg"] = "#ffffff"
        GLabel_190["fg"] = "#333333"
        GLabel_190["justify"] = "center"
        GLabel_190["text"] = "AI Image"
        GLabel_190.place(x=10,y=10,width=100,height=30)

         # Create a Label to display the link
        text1 = Text(root)
        text1.place(x=510,y=10,width=70,height=25)
        text1["bg"] = "#ffffff"
        text1["fg"] = "#333333"
        hyperlink= HyperlinkManager(text1)
        text1.insert(END,"About Us",hyperlink.add(partial(webbrowser.open,"https://github.com/SubhajitMishra04/Ai-Image")))




    def GButton_84_command(self):
        # print("command")

        file = filedialog.askopenfilename(filetypes=[("JPG files",".jpg"),("PNG files",".png")])
        
        if(file):
            root.update()
            shutil.copy(file,"image/")

            infer.main()
            print("command3")
            # time.sleep(5)
            # image1 = Image.open("/Users/subhajitmishra/Desktop/CGAN/Fast-AgingGAN-master/Fast-AgingGAN-master/mygraph.png")
            # image.show()

            # test = ImageTk.PhotoImage(image1)

            # label1 = tk.Label(image=test)
            # label1.image = test

            # label1.place(x=1, y=1)  #Position image
    

    def callback(url):
        webbrowser.open_new_tab(url)


if __name__ == "__main__":
    root = tk.Tk()
    root['background']="#F2F0EC"
    app = App(root)
    root.mainloop()
