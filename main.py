from stats import count_words, count_characters, character_info
import sys

def get_books_text(filepath:str) -> str:
    with open(filepath) as f:
        text = f.read()
    return text 

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")
    rel_path = sys.argv[1]
    print(f"Analyzing book found at {rel_path}")
    
    book_text = get_books_text(rel_path)
    print("----------- Word Count ----------")
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_dict = count_characters(book_text)
    profiles = character_info(char_dict)
    
    for profile in profiles:
            print(f"{profile["character"]}: {profile["count"]}")

main()