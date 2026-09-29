import random
import matplotlib.pyplot as plt

ROWS = 20
SEATS_PER_ROW = 6


def front_to_back():
    total_time = 0

    for row in range(ROWS):
        passengers = [
            random.randint(2, 5)
            for _ in range(SEATS_PER_ROW)
        ]

        total_time += max(passengers)

    return total_time


def alternating_rows():
    total_time = 0

    order = list(range(0, ROWS, 2)) + \
            list(range(1, ROWS, 2))

    for row in order:
        passengers = [
            random.randint(2, 5)
            for _ in range(SEATS_PER_ROW)
        ]

        total_time += max(passengers)

    # Assume a small efficiency improvement
    return total_time * 0.95


def window_middle_aisle():
    total_time = 0

    # Window passengers
    total_time += ROWS * 3

    # Middle passengers
    total_time += ROWS * 2

    # Aisle passengers
    total_time += ROWS * 2

    return total_time


results = {
    "Front-to-Back": front_to_back(),
    "Alternating Rows": alternating_rows(),
    "Window-Middle-Aisle": window_middle_aisle()
}

print("\nAircraft Deplaning Times")
print("-" * 35)

for method, time in results.items():
    print(f"{method}: {time:.1f} seconds")

best_method = min(results, key=results.get)

print("\nBest Method:")
print(f"{best_method} ({results[best_method\]:.1f} seconds)")

plt.figure(figsize=(8, 5))

plt.bar(
    results.keys(),
    results.values(),
    color=["skyblue", "orange", "green"]
)

plt.ylabel("Time (seconds)")
plt.title("Aircraft Deplaning Strategy Comparison")
plt.tight_layout()

plt.savefig("deplaning_results.png")
plt.show()
