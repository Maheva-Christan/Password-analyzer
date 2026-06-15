
import re
import math

def estimate_entropy(password):
    """To calculate the entropy of the password"""

    charset = 0
    n = len(password)

    if re.search(r"(?=.*[a-z])", password):
        charset += 26
    
    if re.search(r"(?=.*[A-Z])", password):
        charset += 26
    
    if re.search(r"(?=.*\d)", password):
        charset += 10
    
    if re.search(r"(?=.*[^a-zA-Z0-9])", password):
        charset += 32
    
    if charset == 0:
        return [0, 0]
    
    entropy = n * math.log2(charset) #Entropy = Size * Log2(Sharset)

    return [entropy, charset]
