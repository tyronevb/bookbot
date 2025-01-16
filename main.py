# bookbot main.py

# main function
def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    print(f"The book: {book_path} contains {num_words} words.")

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        return f.read()
    
def count_words(book_text):
    return len(book_text.split())

main()