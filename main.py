def get_book_contents(file_path):
    with open(file_path) as file:
        return file.read()

def get_word_count(text):
    return len(text.split(" "))

def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_contents(book_path)
    word_count = get_word_count(book_contents)

    print(f"Word Count: {word_count}")

main()