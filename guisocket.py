from threading import Thread
from PIL import Image, ImageTk
import PIL
from tkinter import DISABLED, NORMAL
import cv2
import os
import time
import time
from datetime import datetime
from threading import Timer
from tkinter import *
import pandas as pd
from datetime import datetime
class Video:
    
    
    
    def __init__(self):
        self.__send_video = False
        self.__send_time = True
        

    def set_gui(self, gui):
        
        self.gui = gui
        
    
        
    def o_and_t(self):
        self.t=self.gui.time_entry.get() 
        self.t=int(self.t)
        self.t=self.t*3600
        self.f=int(self.gui.frame_entry.get())
        self.r=self.f*60
        self.prev=0
        self.onStartVideo()
        self.onWatch()
    def onStartVideo(self):
        thread = Thread(target=self.video)
        thread.start()
    
    def onWatch(self):
        thread = Thread(target=self.watch)
        thread.start()

    
        
        
    def onEndVideo(self):
        thread = Thread(target=self.video_off)
        thread.start()

    
    
    def video(self):
      
      self.__send_time=True
      self.gui.start_button.config(state=DISABLED)
      if self.__send_video:
            return  # ignore if already sending videos
      self.__send_video = True
      from pygrabber.dshow_graph import FilterGraph

      graph = FilterGraph()
      devices=graph.get_input_devices()
      print(devices)

      new=[index for (index, cam) in enumerate(devices) if cam == 'c922 Pro Stream Webcam']
      print(new)
      if (len(new)==0):
        print("Case issue")
        new2=[index for (index, cam) in enumerate(devices) if cam == 'C922 Pro Stream Webcam']
        camera=new2[0]
      else:

        camera=new[0]
      
      
      
      
      vid=cv2.VideoCapture(camera,cv2.CAP_DSHOW)
      
      while (vid.isOpened()):
            timer = time.time()
            file = str(timer)
            time_elapsed=timer-self.prev
            _, frame2 = vid.read()
            if time_elapsed>self.r:
                self.prev=time.time()
                cv2image = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGBA)
                frame = PIL.Image.fromarray(cv2image)
                imgtk = ImageTk.PhotoImage(image=frame)
                self.gui.lmain.imgtk = imgtk
                self.gui.lmain.configure(image=imgtk)
                self.gui.lmain.place(x=1, y=1)
            
                
                
                path1 = "Image"
                today = datetime.now()
                directory1 = today.strftime('%Y%m%d')
                folder1 = os.path.join(path1,directory1)
                if not os.path.exists(folder1):
                  os.makedirs(folder1)
                
                cv2.imwrite(folder1 +'/' + str(file) + '.jpg', frame2)
            
                self.gui.top.update()
            
            
            
            
            
            
            if not self.__send_video:
                vid.release()
            
            
        
    
    def video_off(self):
        self.__send_video = False
        self.__send_time = False
        
        
        
        self.gui.start_button.config(state=NORMAL)


    
      
        
        
        
    def watch(self):
        
        
        while self.t:
            
            if self.__send_time is True:
               
                   mins, secs = divmod(self.t, 60)
                   hour, mins = divmod(mins, 60)
                   self.timer = '{:02d}:{:02d}:{:02d}'.format(hour,mins, secs)
            
                   self.gui.stopwatch.config(text=self.timer)
                   time.sleep(1)
                   self.t -= 1
                   
            if self.__send_time is False:
                   return 
        def exitfunc():
            self.__send_video = False
            self.__send_time=False
            self.gui.start_button.config(state=NORMAL)
       
        exitfunc()
        #self.__send_time=True
		 
        
         
        
       
        
    
        
    
    

    