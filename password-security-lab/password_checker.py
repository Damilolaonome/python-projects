
import string


def check_password(password):
    score = 0
    feedback = []

    # Check password length
    if len(password) >= 16:
        score += 3
    elif len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # Check character variety
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Consider adding special characters.")

    # Check for repeated characters
    if any(
        password[i] == password[i + 1] == password[i + 2] == password[i + 3]
        for i in range(len(password) - 3)
    ):
        score -= 2
        feedback.append("Avoid four identical consecutive characters.")

    # Check for simple ascending digit sequences
    for i in range(len(password) - 3):
        sequence = password[i:i + 4]

        if sequence in "0123456789":
            score -= 2
            feedback.append("Avoid simple ascending digit sequences.")
            break

    if score < 0:
        score = 0

    if score >= 7:
        rating = "Strong"
    elif score >= 5:
        rating = "Moderate"
    else:
        rating = "Weak"

    return score, rating, feedback


password = input("Enter a test password: ")

score, rating, feedback = check_password(password)

print(f"\nPassword score: {score}")
print(f"Estimated rating: {rating}")

if feedback:
    print("\nSuggestions:")
    for suggestion in feedback:
        print(f"- {suggestion}")
else:
    print("No basic weaknesses detected.")



