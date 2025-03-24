from typing import Any

from stats import number_of_words
from stats import number_of_characters
from stats import sort_by_greatest_to_least

def get_book_text(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file at {filepath} was not found.")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""


def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    if book_text:
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        word_count = number_of_words(book_text)
        print("--------- Character Count -------")
        char_counts: Any = number_of_characters(book_text)
        sorted_items = sort_by_greatest_to_least(char_counts)
        for item in sorted_items:
            print(f"{item['char']}: {item['count']}")

        print("============= END ===============")

if __name__ == '__main__':
    main()