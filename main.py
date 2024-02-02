from display import Display
from back_end import BackEnd


def main():
    #initiate Display and BackEnd
    display = Display()
    back_end = BackEnd()
    display.frames()
    display.search_input()

    #generate a random quote
    def random_quote():
      quote_text = back_end.random_quote()
      display.update_quote_display(quote_text)
      
    #search for a quote
    def search_quote():
      quote_text = back_end.search(display.search_bar.get())
      display.update_quote_display(quote_text)
      
    #display the next quote
    def next_quote():
      quote_text = back_end.next()
      display.update_quote_display(quote_text)
      
    #display the previous quote
    def back_quote():
      quote_text = back_end.back()
      display.update_quote_display(quote_text)

    #edit the quote display
    quote_display = display.quote_display(next_quote, back_quote)
    display.heading(random_quote, search_quote)
    display.root.mainloop()
  
#execute the main function
if __name__ == "__main__":
    main()