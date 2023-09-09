def fibo_recursive(n, cache):
    # Check if the result is already cached
    if cache[n] != -1:
        return cache[n]
    
    # Base cases for Fibonacci sequence
    if n == 0:
        cache[n] = 0
    elif n == 1:
        cache[n] = 1
    else:
        # Recursively calculate Fibonacci and store the result in cache
        cache[n] = fibo_recursive(n - 1, cache) + fibo_recursive(n - 2, cache)
    
    return cache[n]

def t_init(n):
    # Create a list 'T' of size (n+1) and initialize all values to -1
    T = [-1] * (n + 1)
    
    # Call the recursive Fibonacci function with memoization
    return fibo_recursive(n, T)

n = 10  # You can change the value of 'n' as needed
result = t_init(n)
print(f"The Fibonacci number at position {n} is {result}")

# You can use lru_cache for memoization as well
# from functools import lru_cache
# @lru_cache(maxsize=None)
