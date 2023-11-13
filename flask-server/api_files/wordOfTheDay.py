import requests
from bs4 import BeautifulSoup


def get_word():
    return_string = ''
    url = "https://www.merriam-webster.com/word-of-the-day"
    response = requests.get(url)
    word = ''
    syllables = ''
    word_type = ''

    # If HTTP request is successful, response.status_code will be 200
    if response.status_code == 200:
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        div = soup.find('h2', class_='word-header-txt')
        if div:
            word = div.text
            word = word.strip()
        else:
            print("word not found")

        div = soup.find('span', class_='word-syllables')
        if div:
            syllables = div.text
            syllables = syllables.strip()
        else:
            print("syllables not found")

        div = soup.find('span', class_='main-attr')
        if div:
            word_type = div.text
            word_type = word_type.strip()
        else:
            print("word type not found")

        div = soup.find('div', class_='wod-definition-container')
        if div:
            # Find the first <p> element within the <div>
            first_p = div.find('p')

            if first_p:
                # Get the text content of the first <p> element
                first_p_text = first_p.get_text()
                definition = first_p_text
            else:
                print("definition not found")
    else:
        print("Failed to retrieve the Word of the Day Webpage")

    return_string = word + ", " + syllables + ", " + word_type + "<br><br>" + \
        definition + "<br>"
    return return_string
