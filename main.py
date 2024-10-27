def main():
    get_book_text("books/frankenstein.txt")

def get_book_text(path):
    with open(path) as f:
        print(f.read())

main()
