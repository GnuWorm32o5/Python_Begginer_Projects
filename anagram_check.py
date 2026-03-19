
def anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())
word1 = input("Enter your frist word: ")
word2 = input("Enter your second word: ")

print(anagram(word1, word2))