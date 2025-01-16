# bookbot main.py

# main function
def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    print(f"The book: {book_path} contains {num_words} words.")
    char_count = count_character_occurence(book_text)
    print(char_count)

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        return f.read()
    
def count_words(book_text):
    return len(book_text.split())

def count_character_occurence(book_text):
    character_count = {}
    for char in book_text.lower():
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    
    return character_count

main()