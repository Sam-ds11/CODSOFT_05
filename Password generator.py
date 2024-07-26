import random
import string

def generate_password(length):
    """Generate a random password of given length."""
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation
    all_characters = letters + digits + special_characters
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    """Main function to handle user input and display the password."""
    print("Password Generator")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 8:
                print("Password length should be at least 8 characters for better security.")
                continue
            
            password = generate_password(length)
            print(f"Generated Password: {password}")
            
            again = input("Do you want to generate another password? (yes/no): ").strip().lower()
            if again != 'yes':
                break
        
        except ValueError:
            print("Invalid input. Please enter a valid integer for the password length.")
    
    print("Thank you for using the Password Generator!")

if __name__ == "__main__":
    main()
