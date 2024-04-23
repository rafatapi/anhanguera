a = 1
b = 2
print(f"total = {a+b}")

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
        return fib_sequence

n = 1000
fibonacci_sequence = fibonacci(n)
print(f"Fibonacci sequence of {n}: {fibonacci_sequence}")