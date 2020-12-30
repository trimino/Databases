import tkinter as tk

class Example(tk.Frame):
    def __init__(self):

        tk.Frame.__init__(self)

        self.canvas = tk.Canvas(self, borderwidth=0, width = 50, height = 100)
        self.lframe = tk.Frame(self.canvas, width=10)
        self.sbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.sbar.set)

        self.sbar.grid(row=0, column=0, rowspan=2, sticky="nsw")
        self.canvas.grid(row=0, column=1, rowspan=2, sticky="nsew")
        self.canvas.create_window((2,2), window=self.lframe, anchor="ne", 
                                  tags="self.lframe")

        self.lframe.bind("<Configure>", self.onFrameConfigure)
        self.rframe = tk.Frame(self)
        self.rframe.grid(row=0, column=2, sticky="n")

        self.bframe = tk.Frame(self)
        self.bframe.grid(row=1, column=2)

        llbl = tk.Label(self.lframe, text='this \nis \nthe \nLEFT \nframe')
        llbl.grid(row = 0, column = 0)

        rlbl = tk.Label(self.rframe, text='this is the RIGHT frame')
        rlbl.grid(row = 0, column = 0)
        btn = tk.Button(self.rframe, text='click me', command=self.addmore)
        btn.grid(row=1, column=0, sticky="n")
        blbl = tk.Label(self.bframe, text='this is the BOTTOM frame', bg="yellow")
        blbl.grid(row = 2, column = 0, sticky = "s")

        self.bframe.rowconfigure(1, weight = 1)
        self.bframe.rowconfigure(2, weight = 0)
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 1)
        self.columnconfigure(0, weight = 0)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 0)

        self.cnt = 1

    def addmore(self):
        test = tk.Label(self.lframe, text='this \nis \nthe \nLEFT \nframe\nthis \nis \nthe \nLEFT \nframe\nthis \nis \nthe \nLEFT \nframe\nthis \nis \nthe \nLEFT \nframe\nthis \nis \nthe \nLEFT \nframe\n')
        test.grid(row=self.cnt, column=0)
        self.cnt += 1

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    root=tk.Tk()
    Example().grid(row=0, column=0)
    root.mainloop()
