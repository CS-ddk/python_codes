import re

common_passwords = {"password", "123456", "123456789", "qwerty", "letmein", "abc123", "welcome", "1234", "admin"}

def check_password_strength(password):
    if len(password) < 12:
        return "Weak: Password should be at least 12 characters long."
    
    has_lowercase = bool(re.search(r'[a-z]', password))
    has_uppercase = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special_char = bool(re.search(r'[@#$%^&+=!]', password))
    
    if any(common in password.lower() for common in common_passwords):
        return "Weak: Password contains common patterns or is a common password."
    
    if re.search(r'(1234|abcd|qwerty|asdf)', password.lower()):
        return "Weak: Password contains sequential patterns."

    if re.search(r'(.)\1\1\1', password):
        return "Weak: Password contains repeated characters."

    if not (has_lowercase and has_uppercase and has_digit and has_special_char):
        return "Medium: Password lacks complexity. It should include lowercase, uppercase, digits, and special characters."

    score = 0
    score += len(password) >= 12  
    score += has_lowercase
    score += has_uppercase
    score += has_digit
    score += has_special_char

    if score == 5:
        return "Strong: Password is strong."
    elif score >= 3:
        return "Medium: Password is decent, but could be improved."
    else:
        return "Weak: Password is weak and easy to guess."

while True:
    password = input("Enter a password to check its strength (or type 'q' to quit): ")
    if password.lower() in ['q', 'quit']:
        print("Exiting password strength checker...")
        break
    
    strength = check_password_strength(password)
    print(strength)
