def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_num_words(text)
    characters = get_num_characters(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document\n")
    for c in characters:
        print(f"The '{c["character"]}' character was found {c["number"]} times")
    print("--- End report ---")


def get_num_characters(text):
    characters = {}
    for c in text:
        if not c.isalpha():
            continue
        lowered = c.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1

    sorted_list = []
    for c in characters:
        sorted_list.append({"character": c, "number": characters[c]})
    return sorted(sorted_list, reverse = True, key = lambda x: x["number"])


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
