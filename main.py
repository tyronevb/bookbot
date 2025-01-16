# bookbot main.py

# main function
def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    char_count = count_character_occurence(book_text)
    sorted_char_count = sort_char_counts(char_count)
    print_report(book_path, num_words, sorted_char_count)

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

def print_report(book, num_words, sorted_char_occurences):
    print(f"\n--- Begin report for {book} ---")
    print(f"The book '{book}' contains {num_words} words.\n")

    for char in sorted_char_occurences:
        if char["character"].isalpha():
            print(f"The '{char['character']}' character occurs {char['occurrence']} times.")

    print("\n--- End Report ---")

def sort_char_counts(char_occurences):
    list_of_dicts = []
    for char in char_occurences:
        list_of_dicts.append({'character':char, "occurrence":char_occurences[char]})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def sort_on(dict):
    return dict["occurrence"]

main()