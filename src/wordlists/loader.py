
import os
import sys

def load_wordlist(path):
    """Put the content of a file in a set"""

    try: #open normally the file
        with open(path, "r", encoding="utf-8") as file:
            words = {line.strip().casefold() for line in file if line.strip()}
    
    except UnicodeDecodeError: #if utf-8 can't load the file
        with open(path, "r", encoding="latin-1") as file:
            words = {line.strip().casefold() for line in file if line.strip()}
    
    return words

def load_common_words():
    """Load content of common words in a set"""

    if os.path.exists("../data/common_words.txt"):
        with open("../data/common_words.txt", "r") as c_file:
            common_words = set(c_file.read().splitlines())
    
    else:
        print("Some file is missing or have been removed/displaced")
        sys.exit(0)
    
    return common_words

def load_user_file():
    """To load the user's file"""

    path = ""

    print("Enter the path of the wordlist:")

    try:
        path = input("[PATH] --> ")

        if path.upper() == "\\EXIT":
            print("Thanks for using this program")
            sys.exit(0)

        while not os.path.exists(path):
            print("Specified file doesn't exist, please enter a valid path")
            path = input("[PATH] --> ")

            if path.upper() == "\\EXIT":
                print("Thanks for using this parogram")
                sys.exit(0)

        words = load_wordlist(path)

        while words == set():
            print("Specified file is empty, please choose a file with some content")
            path = input("[PATH] --> ")

            if path.upper() == "\\EXIT":
                print("Thanks for using this parogram")
                sys.exit(0)

            words = load_wordlist(path)
    
    except IsADirectoryError:
        print("This is not a file but a Directory")
    
    except KeyboardInterrupt:
        print("Thanks for using this program")
        sys.exit(0)
    
    return words
