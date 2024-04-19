from decimal import *


def goldenRatio(num, a=1, b=1):
    """ This is a Fibonacci function to estimate the golden ratio
    估算黃金比例：相鄰二項斐波那契數相除接近法
    """

    # checking the inputs must be positive integers
    if type(num) != int:
        raise ValueError("The inputs must be positive integers")
    elif num < 1:
        raise ValueError("The inputs must be positive integers")

    if type(a) != int:
        raise ValueError("The inputs must be positive integers")
    elif a < 1:
        raise ValueError("The inputs must be positive integers")

    if type(b) != int:
        raise ValueError("The inputs must be positive integers")
    elif b < 1:
        raise ValueError("The inputs must be positive integers")

    a, b = Decimal(a), Decimal(b)

    # iterating the loop
    for step in range(num):
        a, b = b, a + b

    # print(f'{type(a)}, a={a}')
    # print(f'{type(b)}, b={b}')

    # return f'{b/a:.100f}'
    return a, b


# Main
if __name__ == '__main__':

    # decimal precision can be set to accomodate our need
    getcontext().prec = 101

    # 3. 黃金比例相鄰二項斐波那契數相除接近法
    print(f"3. 黃金比例相鄰二項斐波那契數相除接近法\n")
    for i in range(240, 241, 1):
        x0, x1 = goldenRatio(i)
        print(f'===> 斐波那契數({i}) 黃金比例估值 =')
        print(102 * '=')
        print(f'{x1/x0}')
        # print(14 * '=')

        print(f'a={x0}\nb={x1}\n')

    # Method 2: 模擬手算除法
    precision = 101
    fibo_max = 66

    x0, x1 = goldenRatio(fibo_max)

    # 求商數
    q = x1 // x0

    # 求餘數
    r = x1 % x0

    ans = [f'{q}.']
    for i in range(precision):
        # 選擇斐波那契裡兩個連續的數，小的做被除數，大的做除數

        # 除數不變，被除數=餘數*10
        r *= 10

        # 小數點後每一位是兩者的商值
        q = r // x0
        r = r % x0
        ans.append(int(str(q)))

    # 輸出後面的100位小數點
    print(
        f'2. Golden Ratio simulating fibo({fibo_max}) {precision} decimals = {ans[0]}')
    for i in range(1, precision, 10):
        print(ans[i:i + 10])
