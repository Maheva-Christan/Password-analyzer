
import re
from .progress_bar import display_progress_bar


def evaluate_strength(analysis):
    """To evaluate the strength of the password and give the verdict"""

    security_strength = analysis["security_strength"]

    entropy = analysis["entropy"]
    print(f"\nEntropy: {entropy:.2f} bits")
    
    if security_strength <= 20:
        print("Verdict: VERY WEAK")

    elif security_strength <= 40:
        print("Verdict: WEAK")
    
    elif security_strength <= 60:
        print("Verdict: MEDIUM")
    
    elif security_strength <= 80:
        print("Verdict: STRONG")
    
    else:
        print("Verdict: EXCELLENT")
    
    display_progress_bar(analysis)


def reasoning(analysis):
    """To give the reasons of the verdict"""

    password = analysis["password"]

    indication = 0

    print("\nPENALISATION:")

    if analysis["in_wordlist"]: #if the password is present in the wordlist
        print("\t- Your password already exists in the wordlist")
        indication = 1
    
    if re.match(r"^[a-z]+$", analysis["password"]): #if a password contains only lower characters
        print("\t- Your password contains only lower characters")
        indication = 1
        
    elif re.match(r"^[A-Z]+$", analysis["password"]): #if a password contains only upper characters
        print("\t- Your password contains only upper characters")
        indication = 1
    
    elif re.match(r"^[0-9]+$", analysis["password"]): #If a password contains only digits
        print("\t- Your password contains only digits")
        indication = 1

    elif re.match(r"^[a-zA-Z]+$", analysis["password"]): #if a password contains only characters
        print("\t- Your password contains only characters")
        indication = 1

    if analysis["length"] < 8: #if a password is too short
        print("\t- Your password is too short")
        indication = 1

    if re.search(r"(.{3,})\1", analysis["password"]) or re.search(r"(.)\1{3,}", analysis["password"]): #if the password contains repetition
        print("\t- Your password contains repetition")
        indication = 1

    if analysis["contains_common_words"][0]: #if the password contains a common word
        common_words = ""
        for word in analysis["contains_common_words"][1]:
            if word != analysis["contains_common_words"][1][len(analysis["contains_common_words"][1]) - 1]:
                common_words += word + ", "
            else:
                common_words += word

        print(f"\t- Your password contains common words: {common_words}")
        indication = 1
    
    if analysis["palindrome"] and (len(password) < 10 or password.isalpha()):
        print("\t- Your password is a weak palindrome")
        indication = 1
    
    if len(password) > 6 and (len(re.findall(r"^[0-9]$", password)) <= 2 or len(re.findall(r"^[A-Z]$", password)) <= 2 or len(re.findall(r"^[a-z]$", password)) <= 2):
        indication = 1

    if (len(re.findall(r"[a-z]", analysis["password"])) >= 3 and len(re.findall(r"[A-Z]", analysis["password"])) >= 3 and len(re.findall(r"[0-9]", analysis["password"])) >= 2 and len(re.findall(r"[^a-zA-Z0-9]", analysis["password"])) >= 2 and analysis["length"] >= 10 and not analysis["in_wordlist"]) or not bool(indication): #Case of a strong password
        print("\nREMARK:")
        print("\t- Your password is strong")
