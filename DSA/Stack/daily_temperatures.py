
def daily_temperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n
    stack = []

    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            previous_day = stack.pop()
            answer[previous_day] = i - previous_day

        stack.append(i)

    return answer


print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(daily_temperatures([30, 40, 50, 60]))
print(daily_temperatures([30, 60, 90]))
print(daily_temperatures([90, 80, 70]))
