import re

def validate_password(password):
    if len(password) < 8:
        print(f"'{password}' is Invalid. Less than 8 Characters.")
        return
    
    special_chars = set("!@#$%&?")
    errors = []
    
    if not any(c.isupper() for c in password):
        errors.append("Missing Uppercase letters")
    if not any(c.islower() for c in password):
        errors.append("Missing Lowercase letters")
    if not any(c.isdigit() for c in password):
        errors.append("Missing Numbers")
    
    special_chars = set(re.findall(r'[^a-zA-Z0-9]', password))
    if not special_chars:
        errors.append("Missing Special characters")
    elif not special_chars.issubset(special_chars):
        errors.append(f"Contains invalid special characters: {''.join(special_chars - special_chars)}")
    
    if errors:
        print(f"'{password}' is Invalid. {', '.join(errors)}")
    else:
        print(f"'{password}' is Valid.")

test_passwords = [
    "Elephant42!",
    "blankspace",
    "LIBRARY789",
    "Sunshine!",
    "24681012",
    "Tiger1!",
    "MountainPeak1",
    "Brilliant#9"
]

for password in test_passwords:
    validate_password(password)
