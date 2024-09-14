def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = count_characters(text)
    print (f"--- Begin report of{book_path} ---")
    print (f"{num_words} words found in the document")
    for char, count in char_count.items():
        print (f"the '{char}' character was found {count} times")



    print("--- End report ---")



def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_characters(text):
    character_count = {}
    for i in text:
        i = i.lower()
        if i.isalpha():
            if i in character_count:
                character_count[i] += 1
            else:
                character_count[i] = 1
    character_count = dict(sorted(character_count.items()))
    return character_count





    

    
    


main()




