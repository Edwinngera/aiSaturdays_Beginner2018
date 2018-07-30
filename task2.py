import random

words = [word.rstrip('\n') for word in open('words.txt')]
randomPhrase = " ".join([words[random.randrange(0, len(words))] for i in range(4)])
reversedWords= randomPhrase[::-1]
print(randomPhrase)
print(reversedWords)
