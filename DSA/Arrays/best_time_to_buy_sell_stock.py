# Problem: Best Time to Buy and Sell Stock
# Approach: Single Pass
# Time Complexity: O(n)
# Space Complexity: O(1)

def max_profit(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


# Test Cases
print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
print(max_profit([7, 6, 4, 3, 1]))     # 0
print(max_profit([2, 4, 1]))           # 2