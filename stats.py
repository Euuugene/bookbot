def get_num_words(file_contents):
    return len(file_contents.split())

def count_characters(file_contents):
    characters_dict = dict()
    for ch in file_contents.lower():
        if ch.isalpha() and ch not in characters_dict:
            characters_dict[ch] = 1
        elif ch.isalpha() and ch in characters_dict:
            characters_dict[ch] += 1

    return characters_dict

def sort_on(items):
    return items["num"]

def sort_characters_dict(characters_dict):
    ls = []
    for k,v in characters_dict.items():
        ls.append({"char":k, "num":v})
    ls.sort(reverse=True, key=sort_on)
    return ls

