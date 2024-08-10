import random

# Simulated functions for malware detection and removal
def detect_malware():
    # Simulate detection of a random number of malware files
    return [f"malware_{i}" for i in range(random.randint(0, 5))]


def remove_malware(malware_list):
    print(f"Removing malware: {malware_list}")
    # Simulate successful removal of malware
    return True


def kaprekar_security_iteration(system_state):
    iterations = 0
    while True:
        # Simulate malware detection
        malware_list = detect_malware()

        if not malware_list:
            print("System is clean.")
            break

        # Simulate malware removal
        remove_malware(malware_list)

        # Increment the iteration count
        iterations += 1

        print(f"Iteration {iterations}: System cleaned from {len(malware_list)} malware(s).")

    return iterations


# Example usage:
system_state = "infected"
total_iterations = kaprekar_security_iteration(system_state)
print(f"System reached a clean state in {total_iterations} iterations.")
