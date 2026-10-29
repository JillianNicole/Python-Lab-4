# Name: Jillian Wildt
# Lab 4 - Words
# Description: This program counts the words in a sentence.

# Count the words in a sentence
def countWords(sentence):
    return len(sentence.split())

sentence = input("Enter a sentence: ")
print("Number of words:", countWords(sentence))
