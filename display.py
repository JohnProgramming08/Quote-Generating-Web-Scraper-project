import tkinter as tk


class Display:
  #sets up initial window and its settings
  def __init__(self):
    self.root = tk.Tk()
    self.root.title("Quote Finder")
    self.root.geometry("600x300")
    self.root.resizable(False, False)
    self.root.configure(bg = "white")

  #creates the frames that are going to be used in the program
  def frames(self):
    self.search_frame = tk.LabelFrame(self.root, bg = "white")
    self.search_frame.grid(row = 1, column = 0, columnspan = 3)
    
    self.quote_frame = tk.LabelFrame(self.root, bg = "white", padx = 10, pady = 10)
    self.quote_frame.grid(row = 5, column = 1)

  def search_input(self):
    self.search_bar = tk.Entry(self.search_frame)
    self.search_bar.grid(row = 0, column = 0, ipadx = 30)
    self.search_bar.insert(0, "enter a tag that describes the quote")
  
  #creates the widgets used to generate/find quotes
  def heading(self, random, search):
    self.title = tk.Label(self.root, text = "Quote Finder", bg = "white")
    self.title.grid(row = 0, column = 0, columnspan = 3)

    self.search_button = tk.Button(self.search_frame, text = "Search", command = search)
    self.search_button.grid(row = 0, column = 1)

    self.empty_row1 = tk.Label(self.root, text = "", bg = "white")
    self.empty_row1.grid(row = 2, column = 0, columnspan = 3)
    
    self.random_button = tk.Button(self.root, text = "Generate Random Quote", command = random)
    self.random_button.grid(row = 3, column = 0, sticky = "w", columnspan = 3)

    self.empty_row2 = tk.Label(self.root, text = "", bg = "white")
    self.empty_row2.grid(row = 4, column = 0)

  #creates the widget for displaying the quotes and scrolling through them
  def quote_display(self, next, back):
    self.quote_label = tk.Label(self.quote_frame, text = "Quote", bg = "white")
    self.quote_label.grid(row = 0, column = 0)
    
    self.next_button = tk.Button(self.root, text = ">", command = next)
    self.next_button.grid(row = 6, column = 1, sticky = "e")

    self.back_button = tk.Button(self.root, text = "<", command = back)
    self.back_button.grid(row = 6, column = 1, sticky = "w")

  def update_quote_display(self, quote_text):
    self.quote_label.config(text = quote_text)
  

