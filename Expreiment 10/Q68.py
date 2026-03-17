#WAP to replace all occurrences of a word in a file with another word
filename = input("Enter file name: ")
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

file = open(filename, "r")
content = file.read()
file.close()

new_content = content.replace(old_word, new_word)

file = open(filename, "w")
file.write(new_content)
file.close()

print("Word replaced successfully!")