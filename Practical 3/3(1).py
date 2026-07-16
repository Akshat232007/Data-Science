def search_word_in_file(filename):
    try:
        search_word = input("Enter the word to search for: ").strip().lower()
        
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().lower()
            

        if search_word in content:
            print(f"Success: The word '{search_word}' was found in the file!")
        else:
            print(f"Not Found: The word '{search_word}' was not found in the file.")
            
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")


search_word_in_file("data.txt")
