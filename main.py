def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    return_report = report(file_contents)



def report(text):
     word_count = numOfWords(text)
     print("--- Begin report of books/frankenstein.txt ---")
     print(word_count, "words found in this document\n")
     character_count = characterCounts(text)
     print("--- End Report ---")


def numOfWords(text):
    words = text.split()
    return len(words)

def characterCounts(text):
    letterCounts = {}

    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
                
            if letter in letterCounts:
                letterCounts[letter] += 1
            else:
                letterCounts[letter] = 1
    
    letter_items = letterCounts.items()

    def get_count(item):
        return item[1]
    sorted_counts = sorted(letter_items, key=get_count, reverse=True)
    for letter, count in sorted_counts:
        print(f"The '{letter}' character was found {count} times")
    
main()