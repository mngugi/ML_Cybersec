# Quadratic iteration model: X_{n+1} = X_n^2
# Initial value
def display_title(title):
    ascii_art = pyfiglet.figlet_format(title)
    print(ascii_art)

if __name__ == "__main__":
    display_title("Quadratic iteration model")

X_0 = 0.1  # Initial vulnerability level
iterations = 10  # Number of iterations
results = [X_0]  # List to store results

# Perform the iterations
for _ in range(iterations):
    X_next = results[-1]**2
    results.append(X_next)

# Prepare the results for visualization
results
