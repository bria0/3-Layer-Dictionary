'''
Created on Nov. 27, 2022
@author: Brianna Nguyen
Assignment: CP312 Letter Dictionary
Date: November 27th, 2022
Description: Python program which takes in user input to define words 
            in a 3 layer hash table. the table starts with 26*26 and 
            grows with the user's new definitions. The program is able
            to add, remove, overwrite, and output definitions.
'''


def main():
    validDictionary = validWords()
    table = {}
    for i in range(97, 123):
        print(chr(i).upper(), end=" ")
        table[chr(i).upper()] = {}
        for k in range(97, 123):
            table[chr(i).upper()][chr(k).upper()] = {}
    print("\n")

    flag = True
    while flag:
        input_word = input('ENTER 99 TO STOP\nEnter the 3 letter word you would like to add: \n') 
        if input_word.isalpha() and len(input_word)==3:
            if not exists(validDictionary, input_word.upper()):
                print("Word is not valid, try another 3 letter word\n")
            else:
                input_desc = input('Enter the definition of the word: \n')
                define_word(table, input_word.upper(), input_desc)
        else:
            flag = False
    flag = True
    while flag:
        input_cmd = input('To search for a definition, enter 1\nTo remove a word from the dictionary, enter 0\nTo exit this program, enter 99\n')
        if input_cmd == "1":
            input_word = input('Enter the 3 letter word you wish to define\n')
            if len(input_word)==3:
                print(search_word(table, input_word.upper()))
            else: 
                print("Word must be 3 letters long, try again")
        elif input_cmd == "0":
            input_word = input('Enter the 3 letter word you wish to remove\n')
            if len(input_word)==3:
                remove_word(table, input_word.upper())
                print(input_word.upper() + " is now deleted")
            else: 
                print("Word must be 3 letters long, try again")
        else:
                flag = False
    print("STOPPING PROGRAM")

def define_word(main_table, word, definition):
    " takes the dictionary to add to, 3 letter word string, and its definition string"
    first = word[0]
    inner = word[1]
    last = word[2]

    if main_table:
        main_table[first][inner][last] = definition
    return main_table

def exists(table, val):
    flag = False
    if not table:
        raise Exception("dictionary is empty")
    else:
        if val[2] in table[val[0]][val[1]]:
            flag = True
    return flag

def search_word(table, val):
    result = val + " does not exist."
    if not table:
        raise Exception("dictionary is empty")
    if exists(table, val):
            #print(val + " exists!")
            result = val + ": " + table[val[0]][val[1]][val[2]]
    return result

def remove_word(main_table, word):
    table = main_table
    if exists(main_table, word):
        table[word[0]][word[1]].pop(word[2])
    return table

def validWords():
    dictionary = {}
    for i in range(97, 123):
        #TESTprint(chr(i).upper(), end=" ")
        dictionary[chr(i).upper()] = {}
        for k in range(97, 123):
            dictionary[chr(i).upper()][chr(k).upper()] = {}
    with open("words.txt") as openfileobject:
            for line in openfileobject:
                define_word(dictionary, line, "valid")
                
    #TESTprint(dictionary)
    return dictionary

main()

