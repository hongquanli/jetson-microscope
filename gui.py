import tkinter as tk
import datetime
from scipy import misc
from subprocess import call
from io import BytesIO
import numpy as np
import time
from tkinter import filedialog
# import matplotlib.pyplot as plt

# sudo apt-get install python3-tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        #self.pack()
        self.grid()
        self.create_widgets()

    ### create widgets ###
    def create_widgets(self):        

	# quit
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        # Exposure Time
        self.label_ss = tk.Label(self,text='Exposure Time (ms)')
        self.var_ss = tk.StringVar()
        #self.var_ss.trace("w", lambda name, index, mode, var_ss=self.var_ss:ss_update(var_ss))
        self.entry_ss = tk.Entry(self,width = 6,textvariable=self.var_ss)
        self.entry_ss.insert(0,"11")
        self.label_ss.grid(row=0,column=0,sticky=tk.W)
        self.entry_ss.grid(row=0,column=1,sticky=tk.W)

	# analog gain
        self.label_analoggain = tk.Label(self,text='analog gain (1-10.625)')
        self.var_analoggain = tk.StringVar()
        self.entry_analoggain = tk.Entry(self,width = 6,textvariable=self.var_analoggain)
        self.entry_analoggain.insert(0,"11")
        self.label_analoggain.grid(row=1,column=0,sticky=tk.W)
        self.entry_analoggain.grid(row=1,column=1,sticky=tk.W)

	# digital gain
        self.label_digitalgain = tk.Label(self,text='digital gain')
        self.var_digitalgain = tk.StringVar()
        self.entry_digitalgain = tk.Entry(self,width = 6,textvariable=self.var_digitalgain)
        self.entry_digitalgain.insert(0,"11")
        self.label_digitalgain.grid(row=2,column=0,sticky=tk.W)
        self.entry_digitalgain.grid(row=2,column=1,sticky=tk.W)

	# fps
        self.label_fps = tk.Label(self,text='fps')
        self.var_fps = tk.StringVar()
        self.entry_fps = tk.Entry(self,width = 6,textvariable=self.var_fps)
        self.entry_fps.insert(0,"21")
        self.label_fps.grid(row=3,column=0,sticky=tk.W)
        self.entry_fps.grid(row=3,column=1,sticky=tk.W)

	# Bit Rate
        self.label_bitrate = tk.Label(self,text='Bit Rate (Mbps)')
        self.var_bitrate = tk.StringVar()
        #self.var_bitrate.trace("w", lambda name, index, mode, var_ss=self.var_ss:ss_update(var_ss))
        self.entry_bitrate = tk.Entry(self,width = 6,textvariable=self.var_bitrate)
        self.entry_bitrate.insert(0,"10")
        self.label_bitrate.grid(row=4,column=0,sticky=tk.W)
        self.entry_bitrate.grid(row=4,column=1,sticky=tk.W)


        # # zoom
        # self.label_zoom = tk.Label(self,text='Zoom')
        # self.scale_zoom = tk.Scale(self,from_=1, to = 10,
        #                           resolution=1,
        #                           orient=tk.HORIZONTAL,
        #                           length = 275,
        #                           command=lambda value:setROI(float(value)))
        # self.scale_zoom.set(1)
        # self.label_zoom.grid(row=10,column=0,sticky=tk.W)
        # self.scale_zoom.grid(row=10,column=1,columnspan=4,sticky=tk.W)

        # seperation
        self.label_seperator = tk.Label(self,text='  ')
        self.label_seperator.grid(row=13,column=0)

        # filename
        self.label_filename = tk.Label(self,text='Prefix')
        self.entry_filename = tk.Entry(self,width = 20)
        
        self.label_filename.grid(row=14,column=0,sticky=tk.W)
        self.entry_filename.grid(row=14,column=1,columnspan=4,sticky=tk.W)

	# preview
        self.btn_preview = tk.Button(self, text="Preview", fg="black", bg = "yellow",
                                     width = 32, height = 2,
                                     command=lambda:preview(self.entry_filename.get(),self.entry_ss.get(),self.entry_analoggain.get(),self.entry_digitalgain.get(),self.entry_fps.get(),
                                                            self.entry_bitrate.get()))
        self.btn_preview.grid(row=15,column=0,columnspan=5,rowspan=2)

        # capture
        self.btn_record = tk.Button(self, text="Capture", fg="black", bg = "yellow",
                                     width = 32, height = 2,
                                     command=lambda:record(self.entry_filename.get(),
                                                            self.entry_ss.get(),
        self.btn_record.grid(row=15+2,column=0,columnspan=5,rowspan=2)

	# playback
        self.btn_record = tk.Button(self, text="Play (Click to Select File)", fg="black", bg = "yellow",
                                     width = 32, height = 2,
                                                            self.entry_bitrate.get()))
                                     command=lambda:play(self.entry_filename.get(),
                                                            self.entry_ss.get(),
                                                            self.entry_bitrate.get()))
        self.btn_record.grid(row=15+4,column=0,columnspan=5,rowspan=2)
    
# camera control

def preview(prefix,ss,analog_gain,digital_gain,fps,bitrate):
   filename = (prefix +
        '_' + str(ss) + ' ms' +
	'_' + str(bitrate) + ' Mbps'
        '_' + '{:%Y-%m-%d %H-%M-%S-%f}'.format(datetime.datetime.now())[:-3]
              )
   print(filename)
   cmd = "gst-launch-1.0 -e nvarguscamerasrc sensor-id=0 aelock=true exposuretimerange=\"" + str(float(ss)*1000000) + " " + str(float(ss)*1000000) + "\" ! \'video/x-raw(memory:NVMM), width=(int)4032, height=(int)3040, format=(string)NV12, framerate=(fraction)" + fps + "/1\' ! nvvidconv flip-method=2 ! nvoverlaysink -e"
   # cmd = "gst-launch-1.0 -e nvarguscamerasrc sensor-id=0 aelock=true exposuretimerange=\'10000 10000\' ispdigitalgainrange=\"" + digital_gain + " " + digital_gain + "\" gainrange=\"" + analog_gain + " " + analog_gain + "\" exposuretimerange=\"" + str(float(ss)*1000000) + " " + str(float(ss)*1000000) + "\" ! \'video/x-raw(memory:NVMM), width=(int)3280, height=(int)2464, format=(string)NV12, framerate=(fraction)" + fps + "/1\' ! nvoverlaysink -e"
   call(cmd,shell=True)

# 

def record(prefix,ss,bitrate):
   filename = (prefix +
        '_' + str(ss) + ' ms' +
        '_' + str(bitrate) + ' Mbps' +
        '_' + '{:%Y-%m-%d %H-%M-%S-%f}'.format(datetime.datetime.now())[:-3] +
        '.mp4')
   print(filename)
   cmd = "gst-launch-1.0 -e nvarguscamerasrc sensor-id=0 aelock=true exposuretimerange=\"" + str(float(ss)*1000000) + " " + str(float(ss)*1000000) + "\" ! \'video/x-raw(memory:NVMM), width=(int)4032, height=(int)3040, format=(string)NV12, framerate=(fraction)" + fps + "/1\' ! nvv4l2h264enc ! h264parse ! mp4mux ! filesink location=" + filename
   call(cmd,shell=True)

def play(prefix,ss,bitrate):

   filename = filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("Video Files","*.mp4"),("all files","*.*")))
   print(filename)
   cmd = "git --version"
   call(cmd,shell=True)


#======================================================================#
#======================================================================#
#======================================================================#

# init.

# set up camera

# create GUI
root = tk.Tk()
app = Application(master=root)
app.mainloop()

# exit routine




#======================================================================#
#======================================================================#
#======================================================================#

# def setROI(zoom):
#   x_start = 0.5 - 1/(2*zoom)
#   y_start = 0.5 - 1/(2*zoom)
#   width = 1/zoom
#   height = 1/zoom
#   print(1/zoom)

# def ss_update(var_ss):
#   tmp = var_ss.get()
#   if tmp == '':
#     print(0)
#   else:
#     ss = int(float(tmp)*1000)
