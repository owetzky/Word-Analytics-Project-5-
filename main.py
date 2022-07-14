# This function returns the entirety of "Dracula" as a string
def readBook():
  f = open("dracula.txt", "r")
  s = f.read().replace("-", " ")
  f.close()
  return ''.join(c for c in s if c.isalnum() or c == " ")

# create a variable to hold the story of Dracula, and then assign it to the result of this function
draculaText = readBook()

# user needs to load text 
text = readBook()

# change the text into a list of words
words = text.split()

# dictionary to count words 
wordCount = {
}


# The word that shows up the most often
# import 
import collections

mostCommon = collections.Counter(words).most_common(1)


# How many unique four-letter words are in the book
count = 0
for characters in words:
  if len(characters) == 4:
    count += 1

  
# Every word that shows up more than 500 times, and how many times that word shows up throughout the book (see the "Walkthrough" section for an example)
# iterate over each word in each line 
for word in words:
# convert the characters in line to lowercase to avoid case mismatch
  word = word.lower()
  
# check if the word is already in dictionary
# if the word is there add one to the count 
  if word in wordCount:
    wordCount[word] = wordCount[word] + 1
    
# add the word to dictionary and set count 1
  else:
    wordCount[word] = 1
    
wordCount = dict(sorted(wordCount.items(), key=lambda item: item[1]))

# print the dictionary contents 
for key, value in wordCount.items():
  if value >= 10:  
    print(f"{key} - {value}")
print()

print(f"There are {count} words that are four letters long")

print()

print(f"{mostCommon} is the word that appears most throughout the text.")