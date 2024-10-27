def main():
    get_book_text("books/frankenstein.txt")
    count_words("books/frankenstein.txt")

def get_book_text(path):
    with open(path) as f:
        print(f.read())

def count_words(path):
        with open(path) as f:
            content = f.read().split()
        print(len(content))

main()
