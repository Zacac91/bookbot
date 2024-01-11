def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = text.split()
    low_text = text.lower()
    word_count = len(words)
   
    letters_count= {}
    for letter in low_text:
        if letter.isalpha():
            if letter in letters_count:
                letters_count[letter] += 1
            else:
                letters_count[letter] = 1

    char_list = [[k,v] for k, v in letters_count.items()]
    char_list.sort(key=lambda x: x[1], reverse=True)
    book_report = "\n".join([f"The character '{item[0]}' was found {item[1]} times" for item in char_list])

    #print (text)
    #print (f"{word_count} words found in the document")
    #print (f"{len(low_text)} total characters in the document")
    #print (letters_count)
    
    print (f"--- Begin report for {book_path} --- \nThe document has {word_count} words, made up of {len(low_text)} characters.\n{book_report}\n--- End of Report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()



main()
