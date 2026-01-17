words = []
word = input('Word: ')

while word != '':
    if word not in words:  
        words.append(word)  
    word = input('Word: ')  
    

number_words_int = len(words)
number_words = str(number_words_int)

print("You know " + number_words + " unique word(s)!")