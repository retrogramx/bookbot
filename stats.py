def convert_words_to_num(file_contents):
	words = file_contents.split()
	num_words = len(words)
	return num_words

def count_characters(file_contents):
	characters = {}

	for character in file_contents:
		character = character.lower()
		if character in characters:
			characters[character] = characters[character] + 1
		else:
			characters[character] = 1
	return characters
