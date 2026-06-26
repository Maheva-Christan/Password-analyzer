
import os
import sys
from src.wordlists import load_wordlist, load_user_file, load_common_words, wordlist_lower_case, remove_spaces
from src.analyzer import check_wordlist, analyze_password, estimate_bruteforce
from src.ui import evaluate_strength, reasoning
    

def main(words):

    common_words = load_common_words()

    print("\nDo you want the verification to be case-sensitive? [Default:yes]")
    print("1) Yes")
    print("2) No")
    print("3) Exit")

    possible_entry = ["1", "2", "3"]

    choice = (input("[1|2|3] --> ")).strip()

    while choice not in possible_entry:
        print("Wrong Entry")
        choice = input("[1|2|3] --> ")

    sensitive = 1

    if choice == "2":
        words = wordlist_lower_case(words)
        sensitive = 0
    
    elif choice == "1":
        pass
    
    else:
        print("\nThanks for using this program")
        sys.exit(0)

    prompt = "[\033[37m----\033[34m] --> "

    os.system("cls" if os.name == "nt" else "clear")

    print("Enter Your password\n")

    try:
        while True:

            password = input("\033[34m" + prompt + "\033[0m")

            if not password or password.strip() == "":
                print("\033[33mpassword cannot be empty\033[0m")
                continue

            if remove_spaces(password, 0).upper() == "\\EXIT":
                print("\nThanks for using this program")
                sys.exit(0)
            
            elif remove_spaces(password, 0).upper() == "\\CLEAR":
                os.system("cls" if os.name == "nt" else "clear")
                continue   

            password = remove_spaces(password, 1)

            if check_wordlist(password, words, sensitive):
                print("\n\033[31m✘ Warning: Your password is present in the wordlist\033[0m")
                prompt = "[\033[31mFOUND\033[34m] --> "
            
            else:
                print("\n\033[32m✔ Message: Your password is missing in the wordlist\033[0m")
                prompt = "[\033[32mSAFE\033[34m] --> "

            analysis = analyze_password(password, words, common_words, sensitive)

            evaluate_strength(analysis)

            reasoning(analysis)

            estimate_bruteforce(analysis)  

            print()          


    except KeyboardInterrupt:
        print("\nThanks for using this program")
        sys.exit(0)


if __name__ == "__main__":

    default_path = "data/darkc0de.txt"

    print("WELCOME! This program will check your password strength and will estimate the time to crack it.\n")
    
    print("Would you want to use your own wordlist or the wordlist built-in with this project")
    print("1) Use wordlist built-in with this project")
    print("2) Use your own wordlist")
    print("3) exit")

    possible_entry = ["1", "2", "3"]

    choose_type_file = input("[1|2|3] --> ").strip()

    while choose_type_file not in possible_entry:
        print("Wrong entry")
        choose_type_file = input("[1|2|3] --> ").strip()
    
    if choose_type_file == "2":
        words = load_user_file()
    
    elif choose_type_file == "1":
        if os.path.exists(default_path):
            words = load_wordlist(default_path)
        
        else:
            print("Default file has been removed or displaced, please enter a path of your own file")
            words = load_user_file()

    else:
        print("Thanks for using this program")
        sys.exit(0)

    main(words)
