import argparse

def get_book_contents(file_path):
    with open(file_path) as file:
        return file.read()

def get_word_count(text):
    return len(text.split(" "))

def get_letter_counts(text):
    lowercase = text.lower()

    counts = {}
    for item in lowercase:
        if item in counts:
            current_count = counts[item]
        else:
            current_count = 0
        counts[item] = current_count + 1

    return counts

def format_letter_counts(letter_counts):
    def sort_on(dict):
        return dict["count"]

    count_list = []
    for key in letter_counts:
        if key.isalpha():
            count_list.append({ "letter": key, "count": letter_counts[key] })
    
    count_list.sort(reverse=True, key=sort_on)

    return count_list

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True, dest="file", type=str, help='file path (Required)')

    args = parser.parse_args()
    
    book_path = args.file
    book_contents = get_book_contents(book_path)

    word_count = get_word_count(book_contents)
    letter_counts = get_letter_counts(book_contents)
    count_list = format_letter_counts(letter_counts)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for item in count_list:
        letter = item["letter"]
        count = item["count"]
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")

main()