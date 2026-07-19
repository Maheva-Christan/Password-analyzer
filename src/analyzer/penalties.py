
import re

from .entropy import estimate_entropy
from .patterns import detect_repetition, detect_character_repetition, detect_palindrome
from .checker import check_wordlist

def final_evaluation(words, common_words, password, sensitive):
    """To penalize password that contains weakness and return the final score"""

    penalty = 1
    entropy = estimate_entropy(password)[0]

    if check_wordlist(password, words, sensitive): #if the password is present in the wordlist
        penalty *= 0.01

    for word in common_words:
        if word.casefold() in password.casefold(): #if password contains a common words
            penalty *= 0.2
            break
    
    if detect_repetition(password): #if a password contains a repeated string
        penalty *= 0.4
    
    if detect_character_repetition(password): #if a password contains a repeated character
        penalty *= 0.4

    if detect_palindrome(password) and len(password) < 10: #if a password is a weak palindrome
        penalty *= 0.4
    
    elif detect_palindrome(password) and password.isalpha():
        penalty *= 0.4

    elif detect_palindrome(password) and len(password) >= 10 and re.search(r"(?=.*[a-z])", password) and re.search(r"(?=.*[A-Z])", password) and re.search(r"(?=.*[0-9])", password) and re.search(r"(?=.*[^a-zA-Z0-9])", password): #if a password is a strong palindrome
        penalty *= 0.8
    
    if len(password) < 8:
        penalty *= 0.4
    
    if re.match(r"^[a-zA-Z]+$", password) and len(password) < 12:
        penalty *= 0.3

    if re.match(r"^[a-zA-Z]+$", password) and len(password) >= 12:
        penalty *= 0.8
    
    if re.match(r"^[0-9]+$", password):
        penalty *= 0.3
        
    if len(password) > 6 and (len(re.findall(r"^[0-9]$", password)) <= 2 or len(re.findall(r"^[A-Z]$", password)) <= 2 or len(re.findall(r"^[a-z]$", password)) <= 2):
        penalty *= 0.5
    
    security_strength = entropy * penalty
    
    return [penalty, security_strength]
