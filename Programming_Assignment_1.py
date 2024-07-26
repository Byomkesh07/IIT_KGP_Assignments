import sys

def frac(n: int) -> int:
    
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n * frac(n - 1)
    
def series(ip: int) -> float:

    total_sum = 0.0
    for i in range(1, ip + 1):
        factorial_i = frac(i)  # Calculate factorial of i using the frac function
        series_element = i / factorial_i
        total_sum += series_element
    return round(total_sum, 2)

    ## CODEBASE:S01 End


## DO NOT MODIFY THIS PART, Please maintain this structure
if __name__ == "__main__":
    print("sys.argv:", sys.argv)
    simulated_args = ['compute_series.py', '5']
    sys.argv = simulated_args
    
    try:
        value = series(int(sys.argv[1]))
        print(value)
    except IndexError:
        print("Error: Please provide an integer input.")
    except ValueError:
        print("Error: Please provide a valid integer input.")