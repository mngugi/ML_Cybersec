def ssq(n):
    digits = [int(digit) for digit in str(n)]  # Convert number to string to extract digits
    return sum(digit**2 for digit in digits)   # Square each digit and sum them up

# Example usage:
print(ssq(23))  # Output: 13
print(ssq(154)) # Output: 42
