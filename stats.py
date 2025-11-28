def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        #print(file_contents)
        return file_contents
    
def word_count(bookstring):
    list_words = bookstring.split()
    num_words = len(list_words)
    #print(num_words)
    return num_words

def sort_on(items):
    return items["num"]

def character_count(bookstring):
    list_words = bookstring.split()
    count = {}
    for word in list_words:
        chars = list(word.lower())
        for char in chars:
            if char in count.keys():
                count[char] += 1
            else:
                count[char] = 1      
    return count

def report_count(path_to_file, wordcount, charcount):
    listchar = []
    for char in charcount:
        if char.isalpha() == True:
            listchar.append({"char": char, "num":charcount[char]})
    listchar.sort(reverse=True, key=sort_on)
    #print(listchar)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for line in listchar:
        print(f"{line["char"]}: {line["num"]}") 
    print("============= END ===============")
    return listchar