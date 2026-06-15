
def check_wordlist(password, words, sensitive):
    """To verify if the password is present in the wordlist"""

    word_presence = 0

    if sensitive: #case of a password with case sensitive
        if password in words:
            word_presence = 1

    
    else: #case of password without case sensitive
        if password.casefold() in words:
            word_presence = 1

    
    return word_presence
