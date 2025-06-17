def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def convert_words_to_num(file_contents):
	words = file_contents.split()
	num_words = len(words)
	return num_words

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = convert_words_to_num(book_text)
    print(f"{num_words} words found in the document")
main()
