import tkinter as tk


class Display:
  #sets up initial window and its settings
  def __init__(self):
    self.root = tk.Tk()
    self.root.title("Quote Generator")
    self.root.geometry("300x300")
    self.root.resizable(False, False)
    self.root.configure(bg = "white")

  #creates the frames that are going to be used in the program
  def frames(self):
    self.quote_frame = tk.LabelFrame(self.root, padx = 10, pady = 10)
    self.quote_frame.grid(row = 4, column = 0)

  #creates the widgets used to generate/find quotes
  def heading(self):
    self.title = tk.Label(self.root, text = "Quote Generator")
    self.title.grid(row = 0, column = 0)
    
    self.search_bar = tk.Entry(self.root)
    self.search_bar.grid(row = 1, column = 0)

    self.search_button = tk.Button(self.root, text = "Search")
    self.search_button.grid(row = 1, column = 1)

    self.random_button = tk.Button(self.root, text = "Generate Random Quote")
    self.random_button.grid(row = 2, column = 0)

    self.empty_row1 = tk.Label(self.root, text = "", bg = "white")
    self.empty_row1.grid(row = 3, column = 0)

  #creates the widget for displaying the quotes and scrolling through them
  def quote_display(self, next, back):
    self.quote_label = tk.Label(self.quote_frame, text = "Quote", bg = "white")
    self.quote_label.grid(row = 0, column = 0)

    self.next_button = tk.Button(self.root, text = ">", command = next)
    self.next_button.grid(row = 5, column = 0, sticky = "e")

    self.back_button = tk.Button(self.root, text = "<", command = back)
    self.back_button.grid(row = 5, column = 0, sticky = "w")

#testing purposes
display = Display()
display.frames()
display.heading()
display.quote_display("next", "back")
display.root.mainloop()
