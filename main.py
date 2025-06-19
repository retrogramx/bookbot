import sys
from stats import convert_words_to_num, count_characters, sort_dict

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def main(filepath):
	print(f'============ BOOKBOT ============')
	book_text = get_book_text(filepath)
	print(f'Analyzing book found at {filepath}...')
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
			print(f'{char}: {num}')
	print(f'============= END ===============')

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print(f'Usage: python3 main.py <path_to_book>')
		sys.exit(1)
	else:
		filepath = sys.argv[1]
		main(filepath)
