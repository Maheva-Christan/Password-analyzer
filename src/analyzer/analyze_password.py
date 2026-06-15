
from .entropy import estimate_entropy
from .penalties import final_evaluation
from .checker import check_wordlist
from .patterns import detect_repetition, detect_character_repetition, detect_palindrome

def analyze_password(password, words, common_words, sensitive):

    entropy, charset = estimate_entropy(password)
    penalty, security_strength = final_evaluation(words, common_words, password, sensitive)
    in_wordlist = bool(check_wordlist(password, words, sensitive))
    contains_common_words = [False, []]

    for word in common_words:
        if word.casefold() in password.casefold():
            contains_common_words[0] = True
            contains_common_words[1].append(word.casefold())
    
    if contains_common_words[0]:
        l_string = contains_common_words[1][0]
        u_common_words = []

        for item in contains_common_words[1]:
            if len(l_string) <= len(item):
                l_string = item
        
        u_common_words.append(l_string)

        for item in contains_common_words[1]:
            if item in l_string:
                pass
            else:
                u_common_words.append(item)
        
        contains_common_words[1].clear()
        contains_common_words[1] = u_common_words

    
    repetition = bool(detect_repetition(password))
    character_repetition = bool(detect_character_repetition(password))
    palindrome = bool(detect_palindrome(password))

    real_combination = 2 ** entropy
    penalised_combination = real_combination * penalty

    analysis = {
        "password":password, "length":len(password), "entropy":entropy,
        "charset":charset, "security_strength":security_strength, "in_wordlist":in_wordlist,
        "contains_common_words":contains_common_words, "repetition":repetition, "palindrome":palindrome,
        "character_repetition":character_repetition, "penalised_combination":penalised_combination,
        "real_combination":real_combination, "words":words, "common_words":common_words}
    
    return analysis
