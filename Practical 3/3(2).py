from bs4 import BeautifulSoup

def search_word_in_html(filename="Demo.html"):
    try:

        with open(filename, 'r', encoding='utf-8') as file:
            html_content = file.read()
            

        soup = BeautifulSoup(html_content, 'html.parser')
        visible_text = soup.get_text().lower()
        

        search_word = input("Enter the word to search in the HTML text: ").strip().lower()
        

        if search_word in visible_text:
            print(f"Success: The word '{search_word}' was found in the HTML text!")
        else:
            print(f"Not Found: The word '{search_word}' was not found in the HTML text.")
            
    except FileNotFoundError:
        print(f"Error: The file '{filename}' could not be found.")

search_word_in_html()
