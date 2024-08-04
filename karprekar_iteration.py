def kaprekar_iteration(num):
    if not (1000 <= num <= 9999):
        raise ValueError("Input number must be a four-digit number")

    iterations = 0
    while num != 6174:
        # Convert number to string and pad with leading zeros if necessary
        num_str = f"{num:04d}"

        # Create the largest and smallest numbers possible from the digits
        large_num = int("".join(sorted(num_str, reverse=True)))
        small_num = int("".join(sorted(num_str)))

        # Subtract the smaller number from the larger number
        num = large_num - small_num

        # Increment the iteration count
        iterations += 1

        print(f"Iteration {iterations}: {large_num} - {small_num} = {num:04d}")

    return iterations


# Example usage:
initial_num = int(input("Enter a four-digit number: "))
try:
    total_iterations = kaprekar_iteration(initial_num)
    print(f"Kaprekar's routine reached 6174 in {total_iterations} iterations.")
except ValueError as e:
    print(e)
