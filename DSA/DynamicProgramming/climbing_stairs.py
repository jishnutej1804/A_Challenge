def climb_stairs(n):
    if n <= 2:
        return n

    first = 1
    second = 2

    for i in range(3, n + 1):
        current = first + second
        first = second
        second = current

    return second


print(climb_stairs(2))
print(climb_stairs(3))
print(climb_stairs(4))
print(climb_stairs(5))
print(climb_stairs(10))