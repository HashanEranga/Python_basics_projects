from tkinter import *
from tkinter import ttk
from tkinter import font
import time 
import datetime

global endTime

def quit(*args):
    root.destroy()

def cant__wait():
    timeLeft = endTime - datetime.datetime.now()
    timeLeft = timeLeft - datetime.timedelta(microseconds=timeLeft.microseconds)

    txt.set(timeLeft)
    root.after(1000, cant__wait)