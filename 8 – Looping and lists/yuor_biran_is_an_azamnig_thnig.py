word1, word2 = input("Enter words: ").split()

if sorted(word1) == sorted(word2) and word1[0] == word2[0] and word1[-1] == word2[-1]:
    print("Super Anagram!")
else:
    print("Huh?")
