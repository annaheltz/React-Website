import requests
from bs4 import BeautifulSoup


def get_verse():
    return_string = ''
    url = "https://www.biblestudytools.com/bible-verse-of-the-day/"
    response = requests.get(url)
    verse = ''
    verse_name = ''

    # If HTTP request is successful, response.status_code will be 200
    if response.status_code == 200:
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        div = soup.find('div', class_='bible-verses')
        if div:
            # Find the nested div inside the target div
            nested_div = div.find('span', class_='font-bold inline-block')

            # Check if the nested div was found
            if nested_div:
                # Modify the text content of the nested div
                # For example, remove the text
                nested_div.string = ''
                verse = div.text
                verse = verse.strip()
            else:
                print("could not find verse")

        div = soup.find('a', class_='text-blue-600 font-bold text-2xl')
        if div:
            verse_name = div.text
            verse_name = verse_name.strip()
        else:
            print("could not find verse name")
    else:
        print("Failed to retrieve the Bible Verse of the Day Webpage")

    return_string = verse_name + "<br>" + verse
    return return_string
