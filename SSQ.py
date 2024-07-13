def ssq(n):
    digits = [int(digit) for digit in str(n)]  # Convert number to string to extract digits
    return sum(digit**2 for digit in digits)   # Square each digit and sum them up

# Example usage:
print(ssq(23))  # Output: 13
print(ssq(154)) # Output: 42
def ssq(n):
    return sum(int(digit)**2 for digit in str(n))

def ssq_sequence(start):
    seen = set()
    sequence = []
    current = start

    while current not in seen:
        sequence.append(current)
        seen.add(current)
        current = ssq(current)

    # To show the cycle
    cycle_start = sequence.index(current)
    cycle = sequence[cycle_start:]
    
    return sequence, cycle

# Example usage
start_number = 61
sequence, cycle = ssq_sequence(start_number)
print("Sequence:", sequence)
print("Cycle:", cycle)
