import tkinter as tk
from tkinter import *

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

import collatzConjecture as ccs

class mainApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.minsize(800,600)
        self.wdt = 800
        self.hgt = 600
        self.createWidgets()
    
    def createWidgets(self):
        # --- Frames ---
        self.mainFrame = tk.Frame(self.master)
        self.mainFrame.config(width=self.wdt, height=self.hgt)
        self.mainFrame.grid(row=1, column=1)
        self.mainFrame.place(anchor="c", relx=0.5, rely=0.5)

        # --- Ploting Section ---
        self.plotingFrame = tk.Frame(self.mainFrame, relief=tk.SOLID)
        self.plotingFrame.config(width=int(self.wdt/2), height=int(self.hgt/2))
        self.plotingFrame.grid(row=1, column=1)

        # --- Inputs Section ---
        self.inputFrame = tk.Frame(self.mainFrame, relief=tk.SOLID)
        self.inputFrame.config(width=int(self.wdt/2), height=int(self.hgt/2))
        self.inputFrame.grid(row=1,column=2, sticky="nsew")

        # - Ini Entry Def -
        self.iniSeqLabel = tk.Label(self.inputFrame, text="Num. Ini. de la Serie: ", anchor="w")
        self.iniSeqLabel.grid(row=1, column=1, sticky="nsew")

        self.iniSeqEntry = tk.Entry(self.inputFrame)
        self.iniSeqEntry.insert(0,"9")
        self.iniSeqEntry.grid(row=1, column=2, sticky="nsew")

        self.subIniButton = tk.Button(self.inputFrame, text="-",command=lambda: self.operateIniSeqEntry(-1))
        self.subIniButton.grid(row=2,column=1,sticky="nsew")

        self.plusIniButton = tk.Button(self.inputFrame, text="+",command=lambda: self.operateIniSeqEntry(1))
        self.plusIniButton.grid(row=2,column=2,sticky="nsew")

        self.advIniLabel = tk.Label(self.inputFrame, text="", fg="#ff0000", anchor="w")
        self.advIniLabel.grid(row=3, column=1, columnspan=2, sticky="nsew")

        # - Max Entry Def -
        self.maxSeqLabel = tk.Label(self.inputFrame, text="Max. Terms. de la Serie: ", anchor="w")
        self.maxSeqLabel.grid(row=4, column=1, sticky="nsew")

        self.maxSeqEntry = tk.Entry(self.inputFrame)
        self.maxSeqEntry.insert(0,"20")
        self.maxSeqEntry.grid(row=4, column=2, sticky="nsew")

        self.advMaxLabel = tk.Label(self.inputFrame, text="", fg="#ff0000", anchor="w")
        self.advMaxLabel.grid(row=5, column=1, columnspan=2,sticky="nsew")

        # - Run Button -
        self.runBttn = tk.Button(self.inputFrame,text="Graficar",command=lambda: self.plotSequence())
        self.runBttn.grid(row=6,column=1,columnspan=2)

    def operateIniSeqEntry(self, nChange):
        try:
            nIniSeq = int(self.iniSeqEntry.get())
        except:
            self.advIniLabel.config(text="Entrada no valida.")
        else:
            self.advIniLabel.config(text="")
            n = nIniSeq + int(nChange)
            self.iniSeqEntry.delete(0,tk.END)
            self.iniSeqEntry.insert(0,str(n))
            self.plotSequence()

    def plotSequence(self):
        # - Validar Ini Entry -
        try:
            nIniSeq = int(self.iniSeqEntry.get())
        except:            
            self.advIniLabel.config(text="Entrada no valida.")
            return
        else:
            self.advIniLabel.config(text="")

        # - Validar Max Entry -
        try:
            nMaxSeq = int(self.maxSeqEntry.get())
        except:
            self.advMaxLabel.config(text="Entrada no valida.")
            return
        else:
            self.advMaxLabel.config(text="")

        # - Generar Seq y Plot -
        yArr = ccs.collatzSequence(nIniSeq,nMaxSeq)
        xArr = list(range(0,len(yArr)))

        fig = plt.figure(figsize=(4, 4),dpi=100)
        plt.plot(xArr, yArr)

        canvas = FigureCanvasTkAgg(fig, self.plotingFrame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=1, ipadx=40, ipady=20)

        plt.close(fig)

if __name__ == "__main__":
    root = tk.Tk()
    app = mainApp(master=root)
    app.mainloop()
