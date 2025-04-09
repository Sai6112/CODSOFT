import random
import string

def generate_password(length):
    # Define possible characters: letters, digits, and punctuation
    # Letters --> A to Z, a to z
    # Digits ---> 0 to 9
    # Punctuation --> All the Symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Welcome message
print("🔐 PASSWORD GENERATOR 🔐")
print("Create strong and random passwords easily!\n")

# Take user input for password length
while True:
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 3:  
            print("Length should be a positive number and greater than 3. Please try again.")
            continue
        elif length >256: # The length of the password should be less than 256
            print("Enter the length within the range.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

# Generate and display the password
generated_password = generate_password(length)
print(f"\nYour generated password is: 🔑 {generated_password}")
