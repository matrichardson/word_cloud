import collections

book = open('98-0.txt',mode="r",encoding="utf8") # Set correct encoding for it to open properly in windows
stopwords = open(stopwords, mode="r", encoding="utf8")
wordslistraw = book.read().split()

''' 
Now we've got a list containing all of the words in the book.  Next step is to load words
into a dictionary:-

1) If the word already exists (as a key), then increment the value (int)
2) If the word doesn't already exist, then add it with a value of 1

'''

words = {} # Create empty dictionary
wordscomplete = []


for i in wordslistraw:
    if i in words:
        words[i] += 1
    else:
        words[i] = 1

for key,value in words.items():
    temp = [value, key]
    wordscomplete.append(temp)

wordscomplete.sort(reverse=True)

print(wordscomplete[:10])
