from tkinter import *
from matplotlib.figure import Figure
from PIL import Image,ImageTk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib
import PIL
import cv2
from multiprocessing import Process
import sys
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import socket
import cv2, pickle, struct
import time
from threading import *



class Gui:
    def __init__(self, connection):
        top = Tk()
        self.top = top
        self.top.title("Demolition")
        self.top.geometry("810x410")
        self.top.resizable(width=0,height=0)
        self.top.config(bg="skyblue")
        self.connection = connection
        
        self.left_frame = Frame(self.top, width=200, height=400, bg='grey')
        self.left_frame.grid(row=0, column=0, padx=10, pady=5)
        self.right_frame = Frame(self.top, width=570, height=400, bg='grey')
        self.right_frame.grid(row=0, column=1, padx=10, pady=5)
        self.lmain = Label(self.right_frame)
        
        self.start_button = Button(self.left_frame, text="Video_On", fg="blue", command=self.connection.o_and_t)
        self.start_button.place(x=60, y=80)
        
        
        self.off_button = Button(self.left_frame, text="Video_0ff", fg="blue", command=self.connection.onEndVideo)
        self.off_button.place(x=60, y=130)
        
        self.Quit_button = Button(self.left_frame, text="Quit", fg="blue", command=top.destroy).place(x=70, y=180)
        
        self.time_label = Label(self.left_frame, text="Time(h)",fg='blue',font="Times 10")
        self.time_label.place(x=5, y=20)
        self.time_entry = Entry(self.left_frame)
        self.time_entry.place(x=60, y=20, width=50)
        self.frame_label = Label(self.left_frame, text="Intv.(m)",fg='blue',font="Times 10")
        self.frame_label.place(x=5, y=50)
        self.frame_entry = Entry(self.left_frame)
        self.frame_entry.place(x=60, y=50, width=50)
        
        self.stopwatch = Label(self.left_frame,font=("Arial", 25),foreground="red")
        self.stopwatch.place(x=40, y=250)

        
        
       
        
        
        
        
        
        
       
        #self.Quit_button = Button(self.Network, text="Quit", fg="blue", command=sys.exit).place(x=100, y=100)

    