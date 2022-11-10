#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:39:15 2022

@author: jesusvazquez
"""

# The words parameter is a list of strings.
def build_dictionary(words):
    # The frequencies dictionary will be built with your code below.
    # Each key is a word string and the corresponding value is an integer 
    # indicating that word's frequency.
    
    wordDict = {}
    ''' Type your code here (remove the "pass" statement below) '''
    #pass

    for word in words:
        if(wordDict.get(word,'na') == 'na'):
            #print(f'Word is not in Dict {word}')
            wordDict[word] = 1
        else:
            wordDict[word] += 1
    return wordDict

# The following code asks for input, splits the input into a word list, 
# calls build_dictionary(), and displays the contents sorted by key.
if __name__ == '__main__':
    words = input().split()
    your_dictionary = build_dictionary(words)
    sorted_keys = sorted(your_dictionary.keys())
    for key in sorted_keys:
        print(key + ': ' + str(your_dictionary[key]))