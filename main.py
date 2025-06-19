from stats import convert_words_to_num, count_characters, sort_dict

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def main():
	print(f'============ BOOKBOT ============')
	book_path = 'books/frankenstein.txt'
	book_text = get_book_text(book_path)
	print(f'Analyzing book found at {book_path}...')
	print(f'----------- Word Count ----------')
	num_words = convert_words_to_num(book_text)
	print(f'Found {num_words} total words')
	print(f'--------- Character Count -------')
	characters = count_characters(book_text)

	list_of_dicts = sort_dict(characters)
	
	for dict_item in list_of_dicts:
		char = dict_item['char']
		num = dict_item['num']
		if char.isalpha():		    
			print(f"{char}: {num}")
	print(f'============= END ===============')


main()
