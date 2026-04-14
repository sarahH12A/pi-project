import random

def estimate_pi(n):
    inside_circle = 0

    for _ in range(n):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi = (4 * inside_circle) / n
    print(f"Estimated Pi = {pi}")

# 👇 هذا مهم جداً
if __name__ == "__main__":
    estimate_pi(1000000)