# Varibales
fullAlphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
  "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "ü", "ä", "ö", "ß", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
  "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Ü", "Ä", "Ö"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

book_path = "books/frankenstein.txt"


# Functions: main, book_path, num_words, count_chars
def main():
    text = get_book_path(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document. ")
    counter = count_chars()
    counter = sort_by_num(counter)
    for key, value in counter.items():
        print(f"""The '{key}' character was found {value} times.""")

def sort_by_num(counter):
    counter = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
    return counter

def get_book_path(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def count_chars():
    text = get_book_path(book_path)
    counter = {}
    for char in text:
        char = char.lower()
        if char in fullAlphabet:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
    
    # counter.sort(reverse=True)
    return counter

# Start of program
main()



# A, B, C, D, E, F, G, H, I, J, K, L, M,
# N, O, P, Q, R, S, T, U, V, W, X, Y, Z