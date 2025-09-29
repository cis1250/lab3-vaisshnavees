#!/usr/bin/env python3
# Word frequency exercise

import re

# checking if the sentence is good through if 
def is_sentence(text):
    # no empty spaces
    if not isinstance(text, str) or not text.strip():
        return False

    # starts with capital letters
    if not text[0].isupper():
        return False

    # punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # has at least one word
    if not re.search(r'\w+', text):
        return False

    return True

def main():
    #user input
    user_sentence = input("Enter a sentence: ")

    # if not valid
    while not is_sentence(user_sentence):
        print("This does not meet the criteria for a sentence.")
        user_sentence = input("Enter a sentence: ")
    
    
    cleaned_sentence = user_sentence[:-1].lower()
    
    words = cleaned_sentence.split()
    
    word_list = []        
    frequency_list = []   
    
    
    for word in words:
        # removing puncuation
        clean_word = word.strip('.,!?;:"')
        
        if clean_word in word_list:
            index = word_list.index(clean_word)
            frequency_list[index] += 1
        else:
            word_list.append(clean_word)
            frequency_list.append(1)
    
    # output
    print("\nWord frequencies:")
    for i in range(len(word_list)):
        print(f"{word_list[i]}: {frequency_list[i]}")

# Run the program
if __name__ == "__main__":
    main()
