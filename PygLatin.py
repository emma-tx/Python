#Pyg Latin Translator
#Based on CodeAcademy.com project
#January 2013

#Most these variables are for text substitution
pyg = 'ay'
original = raw_input('Enter word: ')
word = original.lower()
first = word[0]
new_word = str(word) + pyg
length = len(word)

#Check the user's input phrase is valid
if len(original) > 0 and original.isalpha():
	if first == 'a' or first == 'e' or first == 'i' or first == 'u':
		print original
	else:
		new_word = word[1:length] + word[0] + pyg
		print new_word
else:
	print 'Incorrect - Cannot translate'
