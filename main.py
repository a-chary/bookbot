import sys
from stats import get_num_words, char_count, sorted_dic_list

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents
    
def print_report(f_path, num_words, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {f_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_list:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")
    return

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    f_path = sys.argv[1]

    text = get_book_text(f_path)
    num_words = get_num_words(text)
    character_count = char_count(text)
    char_count_list = sorted_dic_list(character_count)
    print_report(f_path, num_words, char_count_list)

main()