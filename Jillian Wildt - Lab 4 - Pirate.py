# Name: Jillian Wildt
# Lab 4 - Pirate
# Description: This program changes English words into pirate words.

# Translate English words into pirate words
def toPirate(sentence):
    pirateWords = {
        "hello": "Avast",
        "excuse": "Arrr",
        "sir": "Matey",
        "boy": "Matey",
        "man": "Matey",
        "madam": "Proud beauty",
        "woman": "Proud beauty",
        "officer": "Foul blaggart",
        "the": "Th'",
        "my": "Me",
        "your": "Yer",
        "is": "Be",
        "are": "Be",
        "kitchen": "Galley",
        "hotel": "Fleabag inn"
    }

    newSentence = ""
    for word in sentence.split():
        newSentence += pirateWords.get(word.lower(), word) + " "
    return newSentence.strip()

sentence = input("Enter a sentence: ")
print("Pirate translation:", toPirate(sentence))
