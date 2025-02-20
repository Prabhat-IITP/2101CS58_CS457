import re

def validate_password(password):
    if len(password) < 8:
        return False, "Less than 8 Characters"
    
    allowed_special_chars = set("!@#")
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
    elif not special_chars.issubset(allowed_special_chars):
        errors.append(f"Contains invalid special characters: {''.join(special_chars - allowed_special_chars)}")
    
    return (False, ", ".join(errors)) if errors else (True, "Valid")

valid_count = 0
invalid_count = 0

with open("input.txt", "r") as file:
    passwords = file.readlines()

for password in passwords:
    password = password.strip()
    is_valid, message = validate_password(password)
    if is_valid:
        valid_count += 1
    else:
        invalid_count += 1
    print(f"'{password}' is {message}.")

print(f"Total Valid Passwords: {valid_count}")
print(f"Total Invalid Passwords: {invalid_count}")

