# -*- coding: utf-8 -*-

from io import open
import nltk
import pymorphy2

def load_data(text_file):
    sentences = []
    with open(text_file, 'r', encoding='utf-8-sig') as in_file:
        for line in in_file:
            sentences.append(line.strip().encode('utf-8'))
    return sentences

def load_dict(text_file):
    dictionary = {}
    with open(text_file, 'r', encoding='utf-8-sig') as in_file:
        for line in in_file:
            words = line.strip().encode('utf-8').split(':')
            dictionary.update({words[0]: [words[1], words[2]]})
    return dictionary

def improve_translation(eng_text, rus_text, dictionary):
    morph = pymorphy2.MorphAnalyzer()
    translation = rus_text
    for i in range(0, len(eng_text)):
##        eng_tokens = nltk.word_tokenize(eng_text[i])
##        eng_tagged = nltk.pos_tag(eng_tokens)
##        rus_tokens = nltk.word_tokenize(rus_text[i].decode('utf-8'))
        for items in dictionary.items():
            if eng_text[i].find(items[0]) >= 0:
                wrong_words = items[1][0].split(',')
                for word in wrong_words:
                    if translation[i].find(word) >= 0:
                        translation[i] = translation[i].replace(word, items[1][1])
##        for word in rus_tokens:
##            p = morph.parse(word)[0]
##            print p.normal_form
    return translation

def write_result(text):
    with open('russian', 'w', encoding='utf-8-sig') as out_file:
        for line in text[0:-1]:
            out_file.write(line.decode('utf-8-sig'))
            out_file.write('\n'.decode('utf-8-sig'))
        out_file.write(text[-1].decode('utf-8-sig'))
    
def main():
    dictionary = load_dict('dictionary')
    english = load_data('english')
    google = load_data('google')
    bing = load_data('bing')
    yandex = load_data('yandex')
    translation = improve_translation(english, yandex, dictionary)
    write_result(translation)

if __name__ == '__main__':
    main()
