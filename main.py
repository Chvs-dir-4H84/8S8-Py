#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import tkinter
import tkinter.messagebox
import sys
 
root = tkinter.Tk()
 
def exi():
    sys.exit()

def helloCallBack():
   tkinter.messagebox.showinfo("main.py","缺失Nsdallop.dll文件")

def dll_cho():
   tkinter.messagebox.showinfo("Dfck.cpp","正在修复dll文件")

def dll_chos():
   tkinter.messagebox.showinfo("dos.cs","正在修复dll文件,稍后再试")
 
B = tkinter.Button(root, text ="开始菜单", command = helloCallBack)
Z = tkinter.Button(root, text ="开始菜单2", command = helloCallBack)
X = tkinter.Button(root, text ="修复dll文件", command = dll_cho)
F = tkinter.Button(root, text ="退出", command = dll_chos)



B.pack()
Z.pack()
X.pack()
F.pack()

root.geometry("500x500")

root.mainloop()