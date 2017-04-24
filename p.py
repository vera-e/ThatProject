import random

def word_list():
    file = open("out_word_eng.txt", "r")
    file = file.readlines()
    word = []
    for i in file:
        i = i.strip("\n")
        word += [i]
    file = open("english.txt", "r")
    file = file.readlines()
    for i in file:
        i = i.strip("\n")
        if i not in word:
            word += [i]
    random.shuffle(word)
    return word
    

