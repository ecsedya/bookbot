def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    print(f"--- Begin report of {book_path} ---")
    words = get_num_words(text)
    print(f"{words} found in the document")
    print()
    get_num_chars(text)
    print(f"--- End report ---")
    
def get_num_chars(text):
    chars = {}    
    for test_char in text.lower():
        if test_char in chars and test_char.isalpha():
            chars[test_char] +=1
        elif test_char.isalpha():
            chars[test_char] = 1
    
    chars = dict(sorted(chars.items()))
    
    for char in chars.keys():
        print(f"The '{char}' character was found {chars[char]} times")
    
    return


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()