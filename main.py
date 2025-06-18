from stats import convert_words_to_num

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = convert_words_to_num(book_text)
    print(f"{num_words} words found in the document")
main()
