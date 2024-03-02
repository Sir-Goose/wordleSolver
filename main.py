import json


def create_dictionary_from_json(json_file_path):
    with open(json_file_path) as file:
        data = json.load(file)
    return data


def add_five_letter_words_to_list(word_dict):
    for word in word_dict:
        if len(word) == 5:
            word_list.append(word)


def letters_not_included(grey_letter_list):
    bad_words = []
    for char in grey_letter_list:
        for word in word_list:
            if char in word:
                if word not in bad_words:
                    bad_words.append(word)
    for word in bad_words:
        if word in word_list:
            word_list.remove(word)



def letters_included_yellow(yello_letters):
    bad_words = []
    for key in yello_letters:
        position = yello_letters[key]
        for word in word_list:
            if word[position] == key:
                if word not in bad_words:
                    bad_words.append(word)
    for key in yello_letters:
        for word in word_list:
            if key not in word:
                if word not in bad_words:
                    bad_words.append(word)

    for word in bad_words:
        if word in word_list:
            word_list.remove(word)




def green_letter_words(green_letters):
    bad_words = []
    for key in green_letters:
        position = green_letters[key]
        for word in word_list:
            if word[position] != key:
                if word not in bad_words:
                    bad_words.append(word)
    for word in bad_words:
        if word in word_list:
            word_list.remove(word)


word_list = []
five_letter_list = []
grey_letter_list = []
yello_letter_list = []

json_file_path = "words_dictionary.json"
word_dict = create_dictionary_from_json(json_file_path)
print(word_dict)

add_five_letter_words_to_list(word_dict)
print(word_list)
print(len(word_list))

while True:

    grey_letters = input("Enter grey letters: ")
    for char in grey_letters:
        grey_letter_list.append(char)

    letters_not_included(grey_letter_list)
    print(word_list)
    print(len(word_list))

    yellow_letters = {}
    temp = input("Enter Yellow Letters with position eg ___a_: ")
    count = 0
    for char in temp:
        if char != '_':
            yellow_letters[char] = count
        count += 1

    print(yellow_letters)
    letters_included_yellow(yellow_letters)
    print(word_list)
    print(len(word_list))

    green_letters = {}
    temp = input("Enter Green Letters with position eg ___a_: ")
    count = 0
    for char in temp:
        if char != '_':
            green_letters[char] = count
        count += 1

    print(green_letters)
    green_letter_words(green_letters)
    print(word_list)
    print(len(word_list))

