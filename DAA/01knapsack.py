def knapsack_01(weight, value, capacity):
    n = len(value)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weight[i - 1] <= w:
                # Take max of including or excluding the item
                dp[i][w] = max(value[i - 1] + dp[i - 1][w - weight[i - 1]], dp[i - 1][w])
            else:
                # If item weight exceeds current capacity, skip it
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Example input
value = [60, 100, 120]
weight = [10, 20, 30]
capacity = int(input("Enter capacity of knapsack: "))

max_value = knapsack_01(weight, value, capacity)
print("Maximum value in Knapsack =", max_value)
