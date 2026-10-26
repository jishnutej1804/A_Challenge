def climb_stairs(n):
    if n <= 2:
        return n

    prev2 = 1
    prev1 = 2

    for step in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1


if __name__ == "__main__":
    test_cases = [1, 2, 3, 4, 5, 6]

    for n in test_cases:
        print(f"Steps: {n}, Ways: {climb_stairs(n)}")