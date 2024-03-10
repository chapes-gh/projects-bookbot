def get_word_count(text):
    return len(text.split(" "))

def main():
    file_contents = ""
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()
    
    word_count = get_word_count(file_contents)

    print(f"Word Count: {word_count}")

main()