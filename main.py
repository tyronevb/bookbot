# bookbot main.py

# main function
def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print(book_text)
    

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        return f.read()
main()