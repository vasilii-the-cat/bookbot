import sys

from stats import get_num_words
from stats import get_character_count
from stats import get_sorted_character_data

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    contents = get_book_text(path_to_file)
    character_count = get_character_count(contents)
    sorted_character_data = get_sorted_character_data(character_count)

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path_to_file}...')
    print('----------- Word Count ----------')
    print(f'Found {get_num_words(contents)} total words')
    print('--------- Character Count -------')
    for cd in sorted_character_data:
        if cd["char"].isalpha():
            print(f'{cd["char"]}: {cd["num"]}')
    print('============= END ===============')

main()