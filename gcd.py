"""遞廻函式 例子1: 求兩整數的最大公約數"""

def gcd(a, b):
    """ This is a recursive function
    to determin the greatest common divisor among two integers
    遞廻函式: 求兩整數的最大公約數
    """

    # checking two inputs must be positive integers
    if type(a) != int:
        raise ValueError("First input must be a non-negative integer")

    if type(b) != int:
        raise ValueError("Second input must be a non-negative integer")

    # computing the remainders
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# Example gcd
if __name__ == '__main__':
    print(f'gcd(16,4) = {gcd(16, 4)}\n')
    print(f'gcd(20,30) = {gcd(20, 30)}\n')
