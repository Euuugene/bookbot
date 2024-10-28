def main():
    # get_book_text("books/frankenstein.txt")
    # count_words("books/frankenstein.txt")
    charc_dict = count_characters("books/frankenstein.txt")
    print(charc_dict)

def get_book_text(path):
    with open(path) as f:
        print(f.read())

def count_words(path):
        with open(path) as f:
            content = f.read().split()
        print(len(content))

def count_characters(path):
    characters_set = {chr(i+96):0 for i in range(1,27)}

    with open(path) as f:
        content = f.read()

    for c in content:
        if c.isalpha():
            characters_set[c.lower()] += 1

    return characters_set

                
main()