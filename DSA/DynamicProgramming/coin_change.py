def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount:
                dp[current_amount] = min(
                    dp[current_amount],
                    dp[current_amount - coin] + 1
                )

    return dp[amount] if dp[amount] != float("inf") else -1


print(coin_change([1, 2, 5], 11))
print(coin_change([2], 3))
print(coin_change([1], 0))
print(coin_change([1, 3, 4], 6))
print(coin_change([2, 5, 10, 1], 27))