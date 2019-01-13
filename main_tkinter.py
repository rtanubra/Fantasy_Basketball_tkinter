import tkinter as tk

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        #initiate tk functions you will use here.
        self.master = master
        #self.pack()
        self.grid()
        self.create_widgets()
    
    def submit(self):
        print("Initializing Trade Analysis. Please wait:")
        my_names = []
        if self.player1_inp.get():
            my_names.append(self.player1_inp.get())
        if self.player2_inp.get():
            my_names.append(self.player2_inp.get())
        if self.player3_inp.get():
            my_names.append(self.player3_inp.get())
        if len(my_names) < 2:
            print()
        print(my_names)
    
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

        self.player3_label= tk.Label(self,text="Player 3")
        self.player3_label.grid(row=3,column=0)
        self.player3_inp = tk.Entry(self)
        self.player3_inp.grid(row=3, column=2)

        self.status_label = tk.Label(self,text="Prepared to Analyze provide at least 2 players to compare")
        self.status_label.grid(row=4,columnspan=3)

        self.submit = tk.Button(
            self, text = "SUBMIT", fg= "green",command = self.submit
        )
        self.submit.grid(row=5,column=2)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=6)

    

root = tk.Tk()
app = Application(master=root)
app.mainloop()