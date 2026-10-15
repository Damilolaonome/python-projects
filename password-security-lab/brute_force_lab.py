import string

# Define character sets
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

# Combine all character sets
characters = lowercase + uppercase + digits + symbols

# Remove duplicate characters, if any
characters = "".join(sorted(set(characters)))

print("=" * 45)
print("       PASSWORD SEARCH SPACE ANALYZER")
print("=" * 45)

print(f"Available characters: {len(characters)}")
print("Supported length: 1 to 100 characters")

# Get password input
password = input("\nEnter a test password: ")

# Validate password length
if not 1 <= len(password) <= 100:
    print("\nError: Password must contain 1 to 100 characters.")

else:
    # Calculate the search space for this password length
    character_count = len(characters)
    password_length = len(password)

    combinations = character_count ** password_length

    print("\n" + "=" * 45)
    print("             ANALYSIS RESULTS")
    print("=" * 45)

    print(f"Password length: {password_length}")
    print(f"Available characters: {character_count}")
    print(f"Possible combinations at this length: {combinations:,}")

    print("\nThis is a theoretical search-space calculation.")
    print("The program does not attempt to crack the password.")

    print("=" * 45)




