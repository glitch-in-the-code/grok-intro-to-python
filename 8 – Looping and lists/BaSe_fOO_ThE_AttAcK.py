code = input("code: ")

words = code.split()
filtered_words = [word for word in words if word[0].isupper()]
filtered_words.reverse()
message = " ".join(word.lower() for word in filtered_words)

print("says:", meswsage)
