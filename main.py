from stats import get_num_words, count_characters, sort_characters_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_contents = get_book_text(sys.argv[1])
    num_words = get_num_words(file_contents)
    # print(f"{num_words} words found in the document")

    characters_dict = count_characters(file_contents)
    # print(characters_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sort_characters_dict(characters_dict):
        print(dict["char"] + ": " + str(dict["num"]))
    print("============= END ===============")
    sys.exit(0)
    
main()
