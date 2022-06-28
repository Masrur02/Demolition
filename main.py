# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 23:39:25 2021

@author: almas
"""

from guiwin import Gui
from guisocket import Video

if __name__ == '__main__':
    video = Video()
    gui = Gui(video)
    video.set_gui(gui)
    gui.top.mainloop()




