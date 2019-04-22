from tkinter import Tk, Label, Button
from compute_stats import hist_stats

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Create Histograms", command=self.greet)
        self.greet_button.pack()

    def greet(self):
        print("Greetings!")
        hist = hist_stats("results_with_data.csv")
        hist.execute()
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()