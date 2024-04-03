def main():
    book_filepath = "books/frankenstein.txt"
    print_book_summary(book_filepath)

def read_file(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents

def get_word_count(text):
    words = text.split()
    count = len(words)
    return count

def get_char_counts(text):
    lowercase_text = text.lower()
    char_dict = {}
    for char in lowercase_text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_dict_by_value(dict_to_sort, reverse=False):
    return dict(sorted(dict_to_sort.items(), key=lambda item: item[1], reverse=reverse))

def print_book_summary(filepath):
    book_text = read_file(filepath)
    word_count = get_word_count(book_text)
    book_char_counts = get_char_counts(book_text)
    book_char_counts = sort_dict_by_value(book_char_counts, reverse=True)

    print(f"--- Begin report of {filepath} ---")
    print(f"{word_count:,} word{'s' if word_count > 1 else ''} found in the document")
    print("")
    for key, value in book_char_counts.items():
        if not key.isalpha(): # only include letters in this report
            continue
        print(f"The '{key}' character was found {value:,} time{'s' if value > 1 else ''}")
    print("--- End report ---")

main()
