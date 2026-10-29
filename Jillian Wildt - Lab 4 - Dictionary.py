# Name: Jillian Wildt
# Lab 4 - Dictionary
# Description: This program stores and updates student test scores.

# Make a dictionary from two lists
def makeDictionary(names, scores):
    newDict = {}
    for i in range(len(names)):
        newDict[names[i]] = scores[i]
    return newDict

# Find the average score
def getAverage(scoreDict):
    return sum(scoreDict.values()) / len(scoreDict)

names = ["Joe", "Tom", "Barb", "Sue", "Sally"]
scores = [10, 23, 13, 18, 12]

scoreDict = makeDictionary(names, scores)
print(scoreDict)

print("Barb's score:", scoreDict["Barb"])

scoreDict["John"] = 19
print(scoreDict)

sortedScores = sorted(scoreDict.values())
print("Sorted scores:", sortedScores)

print("Average:", getAverage(scoreDict))

scoreDict["Sally"] = 13
print(scoreDict)

del scoreDict["Tom"]
print(scoreDict)
