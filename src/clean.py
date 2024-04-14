import re
import os
# for each file in ../documents/chapters/ folder

directory = '../documents/chapters/'
for filename in os.listdir(directory):
    filepath = directory + filename
    print(f'processing {filepath}')

    with open(filepath, 'r') as file:
        content = file.read()

    # Find the index of the starting point
    start_index = content.find('<div id="page-container">')

    # Remove all text before the starting point
    content = content[start_index:]

    # Encode any formulas that were likely generated in latex originally and are now in html as pure text formatting
    content = re.sub(r'&lt;math&gt;(.*?)&lt;/math&gt;', r'\1', content)

    # Remove all span html elements but keep the text inside the brackets
    content = re.sub(r'<span.*?>(.*?)</span>', r'\1', content)

    # Add space at the beginning of each div text
    content = re.sub(r'<div.*?>(.*?)</div>', r' \1', content)

    # print(content[:1000])
    # Remove all div html elements but keep the text inside the brackets.  Should replace new divs with spaces.
    content = re.sub(r'<div.*?>(.*?)</div>', r'\1', content)

    #remove all html tags
    content = re.sub(r'<.*?>', '', content)

    # Remove all the extra spaces
    content = re.sub(r'\s+', ' ', content)

    # Remove all page numbers and chapter titles footer text there are formatted like "PageNum CHAPTER NUM. ALL CAPITAL WORDS" 
    content = re.sub(r'\d+ [A-Z]+ \d+\. [A-Z ]+', '', content)

    # Write to ../documents/cleaned/ folder
    with open('../documents/cleaned/' + f'{filename[:-5]}.txt', 'w') as file:
        file.write(content)
