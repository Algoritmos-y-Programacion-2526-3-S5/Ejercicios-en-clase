dictionary = {}
words = input("Please enter words español:ingles and separated by commas:")
#Hello:Hola,Bye:Adios,How:Como,Are:Estas,You:Tu
word_list = words.split(",")
for element in word_list:
    translate_list = element.split(":")
    dictionary[translate_list[0]] = translate_list[1]
    
text = input("Please enter a text:")
words_in_text = text.split(" ")
for word in words_in_text:
    print(dictionary.get(word, word), end = " ")