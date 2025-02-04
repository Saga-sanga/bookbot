def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_dict= count_chars(text)
    print_report(book_path, num_words, char_dict)

def count_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_chars(text):
    dict = {}
    for char in text:
        lowered = char.lower()
        if lowered not in dict:
            dict[lowered] = 1
        else:
            dict[lowered] += 1
    return dict

def format_dict(dict):
    formatted_list = []
    for element in dict:
        if element.isalpha():
            formatted_list.append({element: dict[element]})
    formatted_list.sort(reverse=True, key=lambda x: list(x.values())[0])
    return formatted_list

def print_report(book_path, num_words, char_dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    formatted_list = format_dict(char_dict)
    for item in formatted_list:
        for key, value in item.items():
            print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

main()
