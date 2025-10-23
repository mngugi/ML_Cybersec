# a program to generate crytographic sequence 
import pyfiglet # type: ignore

def display_title(title):
    ascii_art = pyfiglet.figlet_format(title)
    print(ascii_art)

if __name__ == "__main__":
    display_title("Generates a cryptographic sequence")
    
def quadratic_iteration(seed, c, p, length):
    """
    Generates a cryptographic sequence using quadratic iteration.

    Parameters:
        seed (int): Initial value (X_0) for the sequence.
        c (int): Constant added to the quadratic term.
        p (int): Prime modulus for finite field arithmetic.
        length (int): Number of values to generate.

    Returns:
        list: Generated sequence.
    """
    sequence = []
    x = seed
    for _ in range(length):
        x = (x**2 + c) % p
        sequence.append(x)
    return sequence

# Example usage
if __name__ == "__main__":
    seed = 7  # Initial value
    c = 5     # Constant
    p = 97    # Prime modulus
    length = 10  # Length of the sequence

    sequence = quadratic_iteration(seed, c, p, length)
    print("Generated Cryptographic Sequence:")
    print(sequence)
