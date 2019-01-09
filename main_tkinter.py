import tkinter as tk

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        #initiate tk functions you will use here.
        self.master = master
        self.pack()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(self)
        self.title["text"] = "Fantasy NBA Analyst\nLet's Begin"
        self.title.grid(columnspan=4)
        
        self.player1_label =tk.Label(self,text="Player 1")
        self.player1_label.grid(row=1,column=0)
        self.player1_inp = tk.Entry(self)
        self.player1_inp.grid(row=1,column=2)
       
        self.player2_label =tk.Label(self,text="Player 2")
        self.player2_label.grid(row=2,column=0)
        self.player2_inp = tk.Entry(self)
        self.player2_inp.grid(row=2,column=2)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=3)



root = tk.Tk()
app = Application(master=root)
app.mainloop()