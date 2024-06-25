def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_words = num_words(text)
    number_letters = num_letters(text)
    final_list = nested_dicts(number_letters)
    final_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{number_words} words found in the document")
    print("")
    for letter in final_list:
        print(f"The '{letter['name']}' character was found {letter['num']} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

#function to get number of words in the text
def num_words(text_string):
    words = text_string.split()
    return len(words)

#get a dictionary with the number of times each letter shows up in the text
def num_letters(text_string):
    lowered_string = text_string.lower()
    non_dupe_letter = {}
    for letter in lowered_string:
        if (letter not in non_dupe_letter) and letter.isalpha():
            non_dupe_letter[letter] = 1
        elif letter.isalpha():
            non_dupe_letter[letter] += 1
    return non_dupe_letter

def nested_dicts(dict_of_letter_count):
    list_of_dicts = []
    for letter_dict in dict_of_letter_count:
        list_of_dicts.append({
            "name": letter_dict,
            "num": dict_of_letter_count[letter_dict]})
    return list_of_dicts

def sort_on(dict):
    return dict["num"]

'''
def dict_counts(list_of_letters):
    letter_counter = {}
    for letter in list_of_letters:
        if letter not in letter_counter:
            letter_counter[letter] = 1
        else:
            letter_counter[letter] += 1
    return letter_counter


#sort by number of occurences - not used right now
def sorting(dict):
    return dict["letter"]
'''

main()