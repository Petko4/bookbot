def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    word_count = get_num_words(text)
    character_dict = get_character_count(text)
    character_list = convert_character_dict_to_sorted_list(character_dict)
    print_report(path, word_count, character_list)
    
def convert_character_dict_to_sorted_list(dict):
    character_list = []
    for character in dict:
        character_list.append({"character": character, "num": dict[character]})
    character_list.sort(reverse=True, key=sort_on)
    return character_list


def print_report(path, word_count, character_list):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    for character_dict in character_list:
        char = character_dict["character"]
        num = character_dict["num"]
        if not char.isalpha():
            continue
        print(f"The '{char}' character was found {num} times")
    print("--- End report ---")
    

def sort_on(dict):
    return dict["num"]
    
def get_character_count(text):
    chars = {}
    for character in text.lower():
        if character not in chars:
            chars[character] = 1
        else:
            chars[character] += 1
    return chars    

def get_num_words(text):
    words = text.split()
    return len(words)

def get_text(path):
    with open(path) as f:
        return f.read()

main()