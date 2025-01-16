# bookbot main.py

# main function
def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    char_count = count_character_occurence(book_text)
    
    print_report(book_path, num_words, char_count)

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

def print_report(book, num_words, char_occurence):
    print(f"--- Begin report for {book} ---")
    print(f"The book '{book}' contains {num_words} words.\n")

    for char in char_occurence:
        if char.isalpha():
            print(f"The '{char}' character occurs {char_occurence[char]} times.")

main()