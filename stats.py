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

def sort_on(list_of_dicts):
	return list_of_dicts['num']

def sort_dict(characters):
	# Convert dictionary to a list of dictionaries
	list_of_dicts = [{'char': key, 'num': value} for key, value in characters.items()]
	list_of_dicts.sort(reverse=True, key=sort_on)
	return list_of_dicts
