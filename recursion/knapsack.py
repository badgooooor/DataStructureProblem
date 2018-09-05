def knapsack(bag, weight, value, n):
    if n == 0 or bag == 0:
        return 0
    if bag < weight[n-1]:
        return knapsack(bag, weight, value, n-1)
    else:
        return max(
            knapsack(bag, weight, value, n-1), 
            value[n-1] + knapsack(bag - weight[n-1], weight, value, n-1)
        )

# Test
value = [50, 100, 120]
weight  = [10,20,30]
bag = 50

print(knapsack(bag, weight, value, len(weight)))