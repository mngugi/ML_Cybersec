# Quadratic Iteration Model Function
def quadratic_iteration(x, n):
    iterations = [x]
    for _ in range(n):
        x = x**2
        iterations.append(x)
    return iterations

# Example IoT Data (Normalized)
iot_data = [0.2, 0.5, 0.8]  # Sensor readings

# Apply Quadratic Iteration Model
for data in iot_data:
    result = quadratic_iteration(data, 5)
    print(f"Input: {data}, Iterations: {result}")
