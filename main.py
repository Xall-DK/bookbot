import sys
from stats import word_count
from stats import character_count
from stats import report_count
from stats import get_book_text

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


path_string = sys.argv[1]
textstring = get_book_text(path_string)
wordcount = word_count(textstring)
#print(f"Found {wordcount} total words")
chars = character_count(textstring)
#print(chars)
report = report_count(path_string, wordcount, chars)