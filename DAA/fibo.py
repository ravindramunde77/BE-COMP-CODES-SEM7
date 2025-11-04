def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

num = int(input("Enter number: "))
print("Fibonacci sequence (Recursive):")
for i in range(num + 1):
    print(fibonacci_recursive(i), end=" ")
print("\n")
# Iterative Fibonacci Function
def fib_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

# Driver code
n = int(input("Enter a number: "))
print("Fibonacci sequence (Iterative) =", fib_iterative(n))
