def reverse_words(sentence):
    words = []
    word = ""
    for char in sentence:
        if char == " ":
            if word:
                words.append(word)
                word = ""
        else:
            word += char
    if word: 
        words.append(word)
    reversed_sentence = ""
    for i in range(len(words) - 1, -1, -1):
        reversed_sentence += words[i]
        if i != 0:
            reversed_sentence += " "
    
    return reversed_sentence
print(reverse_words("My name is Vineet Vishwakarma"))
