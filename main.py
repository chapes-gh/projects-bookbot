def main():
    file_contents = ""
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()
    
    print(file_contents)

main()