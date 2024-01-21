import requests
from bs4 import BeautifulSoup



#selects the page to scrape
page_to_scrape = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

#makes a dictionay of all the quotes, authors and tags in the code
quote_elements = soup.find_all(attrs = {"itemprop":"text"})
quote_authors = soup.find_all(attrs = {"itemprop":"author"})
meta_tags = soup.find_all("meta", attrs = {"itemprop":"keywords"})

#outputs all the quotes, authors and keywords/tags
for quote in quote_elements:
  #formats it in a readable way  
  quote_text = quote.get_text(strip = True)
  
  index = quote_elements.index(quote)
  author_text = quote_authors[index].get_text(strip = True)
  
  tags = meta_tags[index]
  tag_text = tags.get("content")
  tag_list = tag_text.split(",")

  print(f"quote:\n  {quote_text}\n- {tag_list}")
  print(f"author:\n  {author_text}")
  print("--------------------")

desired_tag = input("Enter a tag/keyword to search for: ")
print("--------------------")

#searches for the quote with that tag only on that page
index = 0
found_quotes = 0
for tags in meta_tags:
  tag_text = tags.get("content")
  tag_list = tag_text.split(",")

  for tag in tag_list:
    if desired_tag == tag:
      found_quotes += 1
      
      quote_text = quote_elements[index].get_text(strip = True)
      author_text = quote_authors[index].get_text(strip = True)
  
      print(f"quote:\n  {quote_text}\n- {tag_list}")
      print(f"author:\n  {author_text}")
      print("--------------------")

  index += 1

#selects a new page to scrape
page_number = 2
url = f"https://quotes.toscrape.com/page/{page_number}/"
page_to_scrape = requests.get(url)
page_to_scrape.raise_for_status()
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

#makes dictionaries of all the quotes, tags and authors on the page
quote_elements = soup.find_all(attrs = {"itemprop":"text"})
quote_authors = soup.find_all(attrs = {"itemprop":"author"})
meta_tags = soup.find_all("meta", attrs = {"itemprop":"keywords"})

#outputs all the quotes, authors and keywords on the page
for quote in quote_elements:
  #formats it in a readable way  
  quote_text = quote.get_text(strip = True)

  
  index = quote_elements.index(quote)
  author_text = quote_authors[index].get_text(strip = True)
  
  tags = meta_tags[index]
  tag_text = tags.get("content")
  tag_list = tag_text.split(",")
  
  print(f"quote:\n  {quote_text}\n- {tag_list}")
  print(f"author:\n  {author_text}")
  print("--------------------")

desired_tag = input("Enter a tag/keyword to search for: ")
print("--------------------")
print("--------------------")

page_number = 2
found_quotes = 0
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
      if desired_tag == tag:
        found_quotes += 1

        print(f"quote:\n  {quote_text}\n- {tag_list}")
        print(f"author:\n  {author_text}")
        print(f"page: {page_number}")
        print("--------------------")
        print("--------------------")
  
  page_number += 1


