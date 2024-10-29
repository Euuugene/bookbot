def main():
    print_report("books/frankenstein.txt")

def get_book_text(path):
    with open(path) as f:
        print(f.read())

def count_words(path):
    with open(path) as f:
        content = f.read().split()
    return len(content)

def count_characters(path):
    characters_counts_dict = {chr(i+96):0 for i in range(1,27)}

    with open(path) as f:
        content = f.read()

    for c in content:
        if c.isalpha():
            characters_counts_dict[c.lower()] += 1

    return characters_counts_dict

def print_report(path):
    characters_counts_dict = count_characters(path) 
    report_list = [{"characters":key, "num":value} for key,value in characters_counts_dict.items()]
    report_list.sort(reverse=True,key=sort_on)
    
    # Display Report
    print(f'--- {path} ---')
    print(f'{count_words(path)} words found in the document')

    for item in report_list:
        print(f'The {item["characters"]} character was found {item["num"]} items')
    print('--- End report ---')

def sort_on(dict):
    return dict['num']
       
main()