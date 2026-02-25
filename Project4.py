password = input("Enter your password: ")

has_letter = False
has_number = False
has_space = False

for ch in password:
    if ch.isalpha():
        has_letter = True
    if ch.isdigit():
        has_number = True
    if ch.isspace():
        has_space = False
        break
if len(password) >= 6 and has_letter and has_number:
    print("Valid Password")
else:
    print("Invalid Password")