def fractional_knapsack(value, weight, capacity):
    n = len(value)
    items = []

    # Store value, weight, and value/weight ratio
    for i in range(n):
        ratio = value[i] / weight[i]
        items.append((ratio, value[i], weight[i]))

    # Sort items by ratio (highest first)
    items.sort(reverse=True)

    total_value = 0.0

    for ratio, val, wt in items:
        if capacity >= wt:
            # Take the whole item
            capacity -= wt
            total_value += val
        else:
            # Take the fraction of the remaining capacity
            total_value += val * (capacity / wt)
            break

    return total_value


# Example input
value = [60, 100, 120]
weight = [10, 20, 30]
capacity = int(input("Enter capacity of knapsack: "))

max_value = fractional_knapsack(value, weight, capacity)
print("Maximum value in Knapsack =", max_value)
