#!/usr/bin/env python3
import argparse

# To run the program -> python frequentword.py --filepath <file_path>
# e.g. python frequentword.py --filepath "C:\Users\lenovo\Desktop\Python\code\story"


parser = argparse.ArgumentParser(description="Parse the input file path")
parser.add_argument('--filepath',type=str,required=True,help="Input file")
args = parser.parse_args()
file_path = args.filepath
#print("file_path")

FH = open(file_path,"r")
text = FH.read()
words = text.split()
#print(text.split())

# Key = word , value = word count
wordsdict = {}

# store the word and it's count in the dictionary.
for ele in words:
    wordsdict[ele] = words.count(ele)

# used code snippet from Day 5 Tutorial.
def get_key(key):
    return wordsdict[key]

i = 1
for word in sorted(wordsdict,key=get_key,reverse=True):
    print(word,wordsdict[word])
    if i == 10:
        break
    else:
        i += 1

FH.close()
