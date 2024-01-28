from bs4 import BeautifulSoup
import requests
import random

#creates a class for the back end of the app
class BackEnd:
  #sets up the home page url for parsing
  def __init__(self):
    self.page_to_scrape = requests.get("https://quotes.toscrape.com/")
    self.soup_home = BeautifulSoup(self.page_to_scrape.text, "html.parser")

  #searches for a random quote
  def random_quote(self, quote_display):
    self.random = True
    self.page_number = random.randint(1, 10)
    self.quote_number = random.randint(1, 9)

    page_to_scrape = requests.get(f"https://quotes.toscrape.com/page/{self.page_number}/")
    page_to_scrape.raise_for_status()
    self.soup_random = BeautifulSoup(page_to_scrape.text, "html.parser")

    quote_list = self.soup_random.find_all(attrs = {"itemprop":"text"})
    quote_text = quote_list[self.quote_number].text

    author_list = self.soup_random.find_all(attrs = {"itemprop":"author"})
    author_text = author_list[self.quote_number].text

    meta_tags = self.soup_random.find_all("meta", attrs = {"itemprop":"keywords"})
    tags = meta_tags[self.quote_number].get("content")
    tag_list = tags.split(",")
    tag_text = ""
    for tag in tag_list:
      tag_text += f"{tag}, "


    #quote_display.configure(text = f" quote:\n{quote_text}\n\n author:\n{author_text}\n\n keywords:\n{tag_text}")

  #displays the most popular tags
  def popular_tags(self, tag_display):
    soup = BeautifulSoup(self.page_to_scrape.text, "html.parser")
    key_tag_list = soup.find_all(attrs = {"class":"tag-item"})
    
    for key_tag in key_tag_list:
      key_tag_text = key_tag.text.replace("\n", "")
      #tag_display_text = tag_display.cget("text")
      #tag_display_text += f"{key_tag_text}\n"
      #tag_display.configure(text = tag_display_text)

  #searches multiple pages until it finds 10 quotes with the right tags
  def search(self, quote_display, search_input):
    self.random = False
    self.page_number = 1
    page_number = 2
    found_quotes = 0
    self.quote_list = []
    self.quote_index = 0
    
    while found_quotes < 10:
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

        for tag in tag_list:
          if search_input == tag:
            found_quotes += 1
            self.quote_list.append([quote_text, author_text, tag_text])

      page_number += 1

    quote_display_text = ""
    quote = self.quote_list[0][0]
    author = self.quote_list[0][1]
    tags = self.quote_list[0][2]

    quote_display_text = f" quote:\n{quote}\n\n author:\n{author}\n\n keywords:\n{tags}"
    #quote_display.configure(text = quote_display_text)
  
  #displays the next quote
  def next(self, quote_display):
    #if the quote is a random one then it will just show the next one
    if self.random == True:
      if self.quote_number == 9:
        self.quote_number = 1
        self.page_number += 1
  
        page_to_scrape = requests.get(f"https://quotes.toscrape.com/page{self.page_number}/")
        page_to_scrape.raise_for_status()
        self.soup_random = BeautifulSoup(page_to_scrape.text, "html.parser")
  
      else:
        self.quote_number += 1

      quote_list = self.soup_random.find_all(attrs = {"itemprop":"text"})
      quote_text = quote_list[self.quote_number].text

      author_list = self.soup_random.find_all(attrs = {"itemprop":"author"})
      author_text = author_list[self.quote_number].text

      meta_tags = self.soup_random.find_all("meta", attrs = {"itemprop":"keywords"})
      tags = meta_tags[self.quote_number].get("content")
      tag_list = tags.split(",")
      tag_text = ""
      for tag in tag_list:
        tag_text += f"{tag}, "      
    
    else:
      self.quote_index += 1
      quote_text = self.quote_list[self.quote_index][0]
      author_text = self.quote_list[self.quote_index][1]
      tags = self.quote_list[self.quote_index][2]

      quote_display_text = f" quote:\n{quote_text}\n\n author:\n{author_text}\n\n keywords:\n{tags}"
      #quote_display.configure(text = quote_display_text)

  #displays the previous quote
  def back(self, quote_diaplay):
    #if the quote is a random one then it will just show the previous one
    if self.random == True:
      if self.quote_number == 1:
        self.quote_number = 9
        self.page_number -= 1

        page_to_scrape = requests.get(f"https://quotes.toscrape.com/page{self.page_number}/")
        page_to_scrape.raise_for_status()
        self.soup_random = BeautifulSoup(page_to_scrape.text, "html.parser")

      else:
        self.quote_number -= 1

      quote_list = self.soup_random.find_all(attrs = {"itemprop":"text"})
      quote_text = quote_list[self.quote_number].text

      author_list = self.soup_random.find_all(attrs = {"itemprop":"author"})
      author_text = author_list[self.quote_number].text

      meta_tags = self.soup_random.find_all("meta", attrs = {"itemprop":"keywords"})
      tags = meta_tags[self.quote_number].get("content")
      tag_list = tags.split(",")
      tag_text = ""
      for tag in tag_list:
        tag_text += f"{tag}, "      

    else:
      self.quote_index -= 1
      quote_text = self.quote_list[self.quote_index][0]
      author_text = self.quote_list[self.quote_index][1]
      tags = self.quote_list[self.quote_index][2]

      quote_display_text = f" quote:\n{quote_text}\n\n author:\n{author_text}\n\n keywords:\n{tags}"
      #quote_display.configure(text = quote_display_text)



