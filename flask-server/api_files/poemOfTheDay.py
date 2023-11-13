import requests
from bs4 import BeautifulSoup


def get_poem():
    return_String = ''
    url = "https://www.poetryfoundation.org/poems/poem-of-the-day"
    response = requests.get(url)
    poem = ''
    author = ''
    title = ''

    # If HTTP request is successful, response.status_code will be 200
    if response.status_code == 200:
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        div = soup.find('div', class_='c-feature-hd')
        if div:
            title = div.text
            title = title.strip()
        else:
            print("title not found")

        div = soup.find('span', class_='c-txt c-txt_attribution')
        if div:
            author = div.text
            author = author.strip()
        else:
            print("author not found")

        div = soup.find('div', class_='o-poem')
        if div:

            # Find all child <div> elements within the parent <div>
            child_divs = div.find_all('div')

            # Extract and print the text from each child <div>
            for child_div in child_divs:
                child_text = child_div.get_text()
                poem = poem + child_text + "<br>"
        else:
            print("poem not found")
    else:
        print("Failed to retrieve the Poem of the Day Webpage")

    return_String = title + " " + author + "<br><br>" + poem
    return return_String
