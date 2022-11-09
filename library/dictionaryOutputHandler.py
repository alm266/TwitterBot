import random

from PyDictionary import PyDictionary
dictionary = PyDictionary()

from pathlib import Path

f_path = Path(r"words.txt")
with open(f_path, 'r') as f_object:
    word_list = f_object.readlines()
    words = []
    for w in word_list:
        words.append(w.replace('\n', ''))


def get_random_type_with_definition(word):
    word_type_definition_dict = dictionary.meaning(word)
    parts_of_speech = list(word_type_definition_dict.keys())

    index = random.randint(0, len(parts_of_speech) - 1)
    part_of_speech = parts_of_speech[index]
    definitions = word_type_definition_dict.get(part_of_speech)

    index = random.randint(0, len(definitions) - 1)
    definition = definitions[index]

    return [part_of_speech, definition]


def generate_tweet_text():
    word = get_random_word()
    print("WORD: " + word)

    type_def_pair = get_random_type_with_definition(word)
    part_of_speech = type_def_pair[0]
    definition = type_def_pair[1]

    text = word.upper() + ' the ' + part_of_speech.upper()

    if part_of_speech == 'Verb':
        text = text + ' can mean to '
    else:
        text = text + ' can mean '

    text = text + definition;

    return text


def get_random_word():
    random_index = random.randint(0, len(words) - 1)
    return words[random_index]

