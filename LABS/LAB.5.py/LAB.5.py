
import string
import random

# Part A: Individual Validation Functions

def check_min_length(password, min_len=8):
    return len(password) >= min_len

def has_uppercase(password):
    return any(char in string.ascii_uppercase for char in password)

def has_lowercase(password):
    return any(char in string.ascii_lowercase for char in password)

def has_digit(password):
    return any(char.isdigit() for char in password)

def has_special_char(password):
    return any(char in string.punctuation for char in password)


# Part B: Master Validation Function

def validate_password(password):
    results = {
        "Minimum Length": check_min_length(password),
        "Has Uppercase": has_uppercase(password),
        "Has Lowercase": has_lowercase(password),
        "Has Digit": has_digit(password),
        "Has Special Character": has_special_char(password)
    }

    results["is_valid"] = all(results.values())

    return results


# Part C: User Interface and Testing

def main():

    encouragement_messages = [
        "Keep trying! You're getting closer!",
        "Tip: Try adding numbers and symbols.",
        "A strong password protects your data!",
        "Mix uppercase, lowercase, numbers, and symbols."
    ]

    password = input("Enter a password to validate: ")

    results = validate_password(password)

    print("\nPassword Validation Results:")

    for rule, passed in results.items():
        if rule != "is_valid":
            print(f"{rule}: {'Met' if passed else 'Not Met'}")

    if results["is_valid"]:
        print("\nOverall Result: STRONG password ")
    else:
        print("\nOverall Result: WEAK password")
        print(random.choice(encouragement_messages))



if __name__ == "__main__":
    main()