from bs4 import BeautifulSoup
import requests
import random


#creates a class for the back end of the app
class BackEnd:
  #sets up the home page url for parsing
  def __init__(self):
    self.page_to_scrape = requests.get("https://quotes.toscrape.com/")
    self.soup_home = BeautifulSoup(self.page_to_scrape.text, "html.parser")
    self.random = "unassigned_value"
    self.start_message = False
    self.end_message = False
    
  #wraps quote text
  def text_wrap(self, quote_text):
    character_number = 0
    quote_lined_text = ""
    
    for character in quote_text:
      character_number += 1
      quote_lined_text += character
      if character_number == 50:
        quote_lined_text += ("\n")
        character_number = 0
        
    return quote_lined_text
  
  #searches for a random quote
  def random_quote(self):
    self.random = True
    self.page_number = random.randint(1, 10)
    self.quote_number = random.randint(1, 9)
    self.tag_number = 0

    page_to_scrape = requests.get(f"https://quotes.toscrape.com/page/{self.page_number}/")
    page_to_scrape.raise_for_status()
    self.soup_random = BeautifulSoup(page_to_scrape.text, "html.parser")

    quote_list = self.soup_random.find_all(attrs = {"itemprop":"text"})
    quote_text = quote_list[self.quote_number].text
    quote_lined_text = self.text_wrap(quote_text)

    author_list = self.soup_random.find_all(attrs = {"itemprop":"author"})
    author_text = author_list[self.quote_number].text

    meta_tags = self.soup_random.find_all("meta", attrs = {"itemprop":"keywords"})
    tags = meta_tags[self.quote_number].get("content")
    tag_list = tags.split(",")
    
    tag_text = ""
    for tag in tag_list:
      if self.tag_number < 5:
        tag_text += f"{tag}, "
        self.tag_number += 1
    tag_text = tag_text[:-2]

    quote_display = f" quote:\n{quote_lined_text}\n\n author:\n{author_text}\n\n keywords:\n{tag_text}"
    return quote_display
  
  #displays the most popular tags
  def popular_tags(self, tag_display):
    soup = BeautifulSoup(self.page_to_scrape.text, "html.parser")
    key_tag_list = soup.find_all(attrs = {"class":"tag-item"})
    
    for key_tag in key_tag_list:
      key_tag_text = key_tag.text.replace("\n", "")
      tag_display_text = tag_display.cget("text")
      tag_display_text += f"{key_tag_text}\n"
      tag_display.config(text = tag_display_text)

  #searches multiple pages until it finds 10 quotes with the right tags
  def search(self, search_input):
    self.random = False
    self.page_number = 1
    page_number = 2
    self.found_quotes = 0
    self.quote_list = []
    self.quote_index = 0
    self.tag_number = 0
    
    while self.found_quotes < 10:
      if page_number == 102:
        break
      
      #selects a page to scrape
      url = f"https://quotes.toscrape.com/page/{page_number}/"
      page_to_scrape = requests.get(url)
      page_to_scrape.raise_for_status()
      soup = BeautifulSoup(page_to_scrape.text, "html.parser")

      quote_elements = soup.find_all(attrs = {"itemprop":"text"})
      quote_authors = soup.find_all(attrs = {"itemprop":"author"})
      meta_tags = soup.find_all("meta", attrs = {"itemprop":"keywords"})

      #iterates through all the quotes on that page and checks if their tags have the desired tag
      for quote in quote_elements:
        quote_text = quote.get_text(strip = True)
    
        index = quote_elements.index(quote)
        author_text = quote_authors[index].get_text(strip = True)

        tags = meta_tags[index]
        tag_text = tags.get("content")
        tag_list = tag_text.split(",")
        
        tag_text = ""
        for tag in tag_list:
          if self.tag_number < 5:
            tag_text += f"{tag}, "
            self.tag_number += 1
        tag_text = tag_text[:-2]
        
        for tag in tag_list:
          if search_input == tag:
            self.found_quotes += 1
            quote_lined_text = self.text_wrap(quote_text)
            self.quote_list.append([quote_lined_text, author_text, tag_text])

      page_number += 1
    if self.found_quotes >= 1:
      quote_display_text = ""
      quote = self.quote_list[0][0]
      author = self.quote_list[0][1]
      tags = self.quote_list[0][2]
  
      quote_display_text = f" quote:\n{quote}\n\n author:\n{author}\n\n keywords:\n{tags}"
      return quote_display_text

    else:
      return "No quotes found with that tag"
  
  #displays the next quote
  def next(self):
    self.tag_number = 0
    #if the quote is a random one then it will just show the next one
    if self.random == True:
      if self.quote_number == 9:
        self.quote_number = 1
        self.page_number += 1

        try:
          if self.page_number >= 0:
            url = f"https://quotes.toscrape.com/page/{self.page_number}/"
            page_to_scrape = requests.get(url)
            page_to_scrape.raise_for_status()
            self.soup_random = BeautifulSoup(page_to_scrape.text, "html.parser")

        except:
          return "An error occured please try again"
  
      else:
        self.quote_number += 1

      try:
        quote_list = self.soup_random.find_all(attrs = {"itemprop":"text"})
        quote_text = quote_list[self.quote_number].text
        quote_lined_text = self.text_wrap(quote_text)
  
        author_list = self.soup_random.find_all(attrs = {"itemprop":"author"})
        author_text = author_list[self.quote_number].text
  
        meta_tags = self.soup_random.find_all("meta", attrs = {"itemprop":"keywords"})
        tags = meta_tags[self.quote_number].get("content")
        tag_list = tags.split(",")
        
        tag_text = ""
        for tag in tag_list:
          if self.tag_number < 5:
            tag_text += f"{tag}, "
            self.tag_number += 1
        tag_text = tag_text[:-2]
  
        quote_display_text = f" quote:\n{quote_lined_text}\n\n author:\n{author_text}\n\n keywords:\n{tag_text}"
        return quote_display_text

      except:
        return "Please try again"
      
    #if the quote is not a random one then it will show the next one
    elif self.random == False:
      if self.quote_index < self.found_quotes - 1:
        if self.start_message == False:
          self.quote_index += 1

        elif self.start_message == True:
          self.start_message = False
        
        quote_text = self.quote_list[self.quote_index][0]
        author_text = self.quote_list[self.quote_index][1]
        tags = self.quote_list[self.quote_index][2]
        
        quote_display_text = f" quote:\n{quote_text}\n\n author:\n{author_text}\n\n keywords:\n{tags}"
        return quote_display_text

      else:
        self.end_message = True
        return "No more quotes with that tag!"

    else:
      return "No quotes searched for yet!"

  #displays the previous quote
  def back(self):
    self.tag_number = 0
    #if the quote is a random one then it will just show the previous one
    if self.random == True:
      if self.quote_number == 1 and self.page_number > 0:
        self.quote_number = 9
        self.page_number -= 1
        
        try:
          url = f"https://quotes.toscrape.com/page/{self.page_number}/"
          page_to_scrape = requests.get(url)
          page_to_scrape.raise_for_status()
          self.soup_random = BeautifulSoup(page_to_scrape.text, "html.parser")

        except:
          return "An error occured please try again"

      else:
        self.quote_number -= 1

      try:
        quote_list = self.soup_random.find_all(attrs = {"itemprop":"text"})
        quote_text = quote_list[self.quote_number].text
        quote_lined_text = self.text_wrap(quote_text)
  
        author_list = self.soup_random.find_all(attrs = {"itemprop":"author"})
        author_text = author_list[self.quote_number].text
  
        meta_tags = self.soup_random.find_all("meta", attrs = {"itemprop":"keywords"})
        tags = meta_tags[self.quote_number].get("content")
        tag_list = tags.split(",")
        
        tag_text = ""
        for tag in tag_list:
          if self.tag_number < 5:
            tag_text += f"{tag}, "
            self.tag_number += 1
        tag_text = tag_text[:-2]
  
        quote_display_text = f" quote:\n{quote_lined_text}\n\n author:\n{author_text}\n\n keywords:\n{tag_text}"
        return quote_display_text

      except:
        return "Please try again"

    elif self.random == False:
      if self.quote_index > 0:
        if self.end_message == False:
          self.quote_index -= 1

        elif self.end_message == True:
          self.end_message = False
          
        quote_text = self.quote_list[self.quote_index][0]
        author_text = self.quote_list[self.quote_index][1]
        tags = self.quote_list[self.quote_index][2]

        quote_display_text = f" quote:\n{quote_text}\n\n author:\n{author_text}\n\n keywords:\n{tags}"
        return quote_display_text

      else:
        self.start_message = True
        return "This is as far back as you can go!"

    else:
      return "No quotes searched for yet!"