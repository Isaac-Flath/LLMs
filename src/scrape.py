import requests
from bs4 import BeautifulSoup
import os

# URL of the book website
url = "https://www.deeplearningbook.org/"

# Folder to save the downloaded content
save_folder = "../documents/chapters/"

# Create the save folder if it doesn't exist
os.makedirs(save_folder, exist_ok=True)

# Send a GET request to the book website
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the hyperlinks that start with "contents/"
links = soup.find_all('a',href=lambda x: x and x.startswith('contents'))

ignore_files = ('TOC.html', 'acknowledgements.html', 'notation.html', 
                   'bib.html', 'index-.html','part_basics.html',
                   'part_practical.html','part_research.html',)
# Download and save the content of each link
for link in links:
    content_url = url + link["href"]
    filename = content_url.split("/")[-1]
    if filename in ignore_files: 
        continue 
    filepath = os.path.join(save_folder, filename)

    response = requests.get(content_url)
    print(f"URL: {content_url} | filename: {filepath}")
    with open(filepath, "wb") as file:
        file.write(response.content)
        print(f"Downloaded {filepath}")

print("Download completed!")