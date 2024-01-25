from bs4 import BeautifulSoup
import requests
import random


class BackEnd:
  def __init__(self):
    self.page_to_scrape = requests.get("https://quotes.toscrape.com/")
    self.soup = BeautifulSoup(self.page_to_scrape.text, "html.parser")

  def random_quote(self, quote_display):
    page_number = random.randint(1, 10)
    quote_number = random.randint(1, 9)

    page_to_scrape = requests.get(f"https://quotes.toscrape.com/page/{page_number}/")
    page_to_scrape.raise_for_status()
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")

    quote_list = soup.find_all(attrs = {"itemprop":"text"})
    quote_text = quote_list[quote_number].text

    author_list = soup.find_all(attrs = {"itemprop":"author"})
    author_text = author_list[quote_number].text

    meta_tags = soup.find_all("meta", attrs = {"itemprop":"keywords"})
    tags = meta_tags[quote_number].get("content")
    tag_list = tags.split(",")
    tag_text = *tag_list, sep = ", "

    #quote_display.configure(text = f" quote:\n{quote_text}\n\n author:\n{author_text}\n\n keywords:\n{tag_text}")

  def tags(self, tag_display):
    key_tag_list = self.soup.find_all(attrs = {"class":"tag-item"})
    key_tags = []
    
    for key_tag in key_tag_list:
      key_tag_text = key_tag.text.replace("\n", "")
      key_tags.append(key_tag_text)
      
    

    
back_end = BackEnd()
back_end.random_quote("quote_display")
back_end.tags("tag display")
