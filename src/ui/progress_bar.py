
def display_progress_bar(analysis):

    security_strength = analysis["security_strength"]


    filled = max(0, min(int((security_strength)/5), 20))

    progress_bar = "[" + "="*filled + " "*(20-filled) + "]"

    if security_strength <= 30:
        print(f"\033[31m{progress_bar} {security_strength:.2f}%\033[0m")
    
    elif security_strength <= 65:
        print(f"\033[33m{progress_bar} {security_strength:.2f}%\033[0m")
    
    elif security_strength <= 97:
        print(f"\033[32m{progress_bar} {security_strength:.2f}%\033[0m")
    
    elif security_strength > 97:
        print(f"\033[32m[=================== ] 97.00% \033[0m")
