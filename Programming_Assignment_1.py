import sys

def frac(n: int) -> int:
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return n * frac(n - 1)
    
def series(ip: int) -> float:
    
    
    total_sum = 0.0
    for i in range(1, ip + 1):
        factorial_i = frac(i)  # Calculate factorial of i using the frac function
        series_element = 1 / factorial_i
        total_sum += series_element
    
    return total_sum

# Preserve the main structure without changes
try:
    value = series(int(sys.argv[1]))
    print(value)
except IndexError:
    print("Error: Please provide an integer argument.")
except ValueError:
    print("Error: Provided argument is not a valid integer.")
