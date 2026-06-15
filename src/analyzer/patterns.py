
import re

def detect_repetition(password):
    """To detect the password with repeated string"""

    repetition = 0

    if re.search(r"(.{3,})\1", password):
        repetition = 1
    
    return repetition

def detect_character_repetition(password):
    """To detect the password with repeated characters"""

    character_repetition = 0

    if re.search(r"(.)\1{3,}", password):
        character_repetition = 1
    
    return character_repetition

def detect_palindrome(password):
    """To detect if a password is a palindrome"""

    palindrome = 0
    
    reversed_password = password[::-1]

    if reversed_password == password:
        palindrome = 1
    
    return palindrome
