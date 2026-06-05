from bs4 import BeautifulSoup
import requests

# Access and return the source from a web page
page_to_scrape = requests.get("https://www.scrapethissite.com/pages/")

# Use BeautifulSoup's HTML parser to convert it into an object
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

# Find elements on the web page based on HTML tag and CLASS
# Return them as tuples
countries = soup.find_all("h3", attrs={"class":"country-name"})



# Loop through the tuples in tandem using the zip function
# Present the data to the user
