def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = text.split()
    low_text = text.lower()
    word_count = len(words)
   
    letters_count= {}
    for letter in low_text:
        if letter in letters_count:
            letters_count[letter] += 1
        else:
            letters_count[letter] = 1

    print(text)
    print(f"{word_count} words found in the document")
    print (f"{len(low_text)} total characters in the document")
    print (letters_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()



main()
