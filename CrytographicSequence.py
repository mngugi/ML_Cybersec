import secrets
import string
import pyfiglet # type: ignore

def display_title(title):
    ascii_art = pyfiglet.figlet_format(title)
    print(ascii_art)

if __name__ == "__main__":
    display_title("Generated cryptographic sequence")

def generate_cryptographic_sequence(length=32):
    # Define the character set
    charset = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a secure random sequence
    sequence = ''.join(secrets.choice(charset) for _ in range(length))
    return sequence

# Example usage
sequence = generate_cryptographic_sequence(64)
print("Generated Cryptographic Sequence:", sequence)
