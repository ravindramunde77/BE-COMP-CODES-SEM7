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
print("Recursive Time Complexity: O(2^n)")
print("Recursive Space Complexity: O(n)\n")
def fibonacci_iterative(n):
    a, b = 0, 1
    print("Fibonacci sequence (Iterative):")
    print(a, end=" ")
    for _ in range(n):
        print(b, end=" ")
        a, b = b, a + b
    print("\n")
num = int(input("Enter number: "))
fibonacci_iterative(num)
print("Non-Recursive Time Complexity: O(n)")
print("Non-Recursive Space Complexity: O(1)")
