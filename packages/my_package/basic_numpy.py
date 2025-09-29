import numpy as np

def add_numbers(a, b):
    return np.add(a, b)

if __name__ == "__main__":
    x = 5
    y = 7
    result = add_numbers(x, y)
    print(f"The sum of {x} and {y} is: {result}")
