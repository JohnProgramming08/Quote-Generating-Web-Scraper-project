from display import Display
from back_end import BackEnd

def main():
    display = Display()
    back_end = BackEnd()
    display.frames()
    display.search_input()
    
    def random_quote():
      quote_text = back_end.random_quote()
      display.update_quote_display(quote_text)

    def search_quote():
      quote_text = back_end.search(display.search_bar.get())
      display.update_quote_display(quote_text)

    def next_quote():
      quote_text = back_end.next()
      display.update_quote_display(quote_text)

    def back_quote():
      quote_text = back_end.back()
      display.update_quote_display(quote_text)
  
    quote_display = display.quote_display(next_quote, back_quote)
    display.heading(random_quote, search_quote)
    display.root.mainloop()

if __name__ == "__main__":
    main()