print("PASSWORD MUST BE CAPITAL , SMALL ,SYMBOL AND DIGIT")

password = input("Enter a password: ")


if len(password) < 8:
    print("Password must be at least 8 characters long.")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in "!@#$%^&*()_+-=[]{}|;:,.<>?":
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        print("Password is strong.")
    else:
        print("Password is weak.")