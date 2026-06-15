
import re

def wordlist_lower_case(words):
    """Put the content of a set into a lower"""

    lower_words = set()
    for word in words:
        lower_words.add(word.lower())
    
    return lower_words


def remove_spaces(password, display):
    """To remove space between anr around the password entered by the users"""

    if re.search(r"\s", password):
        new_password = "".join(password.split())

        if display:
            print(f"\nSpace(s) have been removed from password: {password} --> {new_password}")
    
    else:
        new_password = password
    
    return new_password

