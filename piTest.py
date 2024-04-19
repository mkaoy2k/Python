"""估算π值
ChatGPT wrote this Python program, but not working.
"""
import mpmath

exact_pi_1001 = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

def estimate_pi(precision):
    """
    Chudnovsky 算法估算圓周率到指定的小數位數
    """
    mpmath.mp.dps = precision + 1

    # 初始值
    C = mpmath.mpf(426880) * mpmath.sqrt(mpmath.mpf(10005))
    T = mpmath.mpf(13591409)
    L = mpmath.mpf(1)
    X = mpmath.mpf(1)
    M = mpmath.mpf(1)
    S = mpmath.mpf(13591409)
    K = mpmath.mpf(6)

    while abs(M) > 1e-100:
        M = (mpmath.mpf(K)**3 - mpmath.mpf(16 * K)) * \
            L / (mpmath.mpf(K + 1)**3)
        L *= X**2
        S += M
        X *= T
        T += C
        K += 1

    # 因為我們計算的是 pi/12，所以需要乘以 12
    pi = mpmath.mpf(1) / (mpmath.mpf(12) * S)

    # 因為我們計算了一位多出來的小數，所以要四捨五入到指定的精度
    return int(mpmath.nstr(pi, precision))

def matchDigit(pi):
    """Return the matched digits of 𝜋
    """

    for n in range(len(exact_pi_1001)):
        matched = (str(pi)[:n] == exact_pi_1001[:n])
        if matched is False:
            print(f'===>π值 = {exact_pi_1001[:n]}')
            print(f'===>π值~= {pi}')
            print(f"===>matched upto {n-2} after-dec point\n")
            break
    return matched

def main():

    print("7. Using Chudnovsky 算法:")
    pi = estimate_pi(100)
    if matchDigit(pi):
        print(f'===>π值 = {exact_pi_1001}')
        print(f'===>π值~= {pi}')
        print(f"===>matched upto 1,000 after-dec point\n")

if __name__ == "__main__":
    main()


# import decimal as dec

# # The following string 'exact_pi_val' contains 1001 correct digit of 𝜋.
# # So, The program will itself check if the calculated 𝜋 value
# # is right or wrong up to 1000 digit.
# exact_pi_1001 = str(31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989)




# def estimate_pi(precision):
#     """
#     Chudnovsky 算法估算圓周率到指定的小數位數
#     """
#     dec.getcontext().prec = precision * 2

#     # 初始值
#     C = dec.Decimal(426880) * dec.Decimal(10005).sqrt()
#     T = dec.Decimal(13591409)
#     L = dec.Decimal(1)
#     X = dec.Decimal(1)
#     M = dec.Decimal(1)
#     S = dec.Decimal(13591409)
#     K = dec.Decimal(6)

#     while abs(M) > 1e-100:
#         M = (dec.Decimal(K**3) - dec.Decimal(16 * K)) * \
#             L / (dec.Decimal(K + 1)**3)
#         L = L * X
#         L = L * X
#         S = S + M
#         X = X * T
#         T = T + dec.Decimal(C)
#         K += 1

#     # 因為我們計算的是 pi/12，所以需要乘以 12
#     pi = dec.Decimal(1) / (dec.Decimal(12) * S)

#     # 因為我們計算了一位多出來的小數，所以要四捨五入到指定的精度
#     return int(round(pi, precision) * precision)


# # 使用例子
# if __name__ == "__main__":
#     print(f"7. Using Chudnovsky 算法:")
#     pi = estimate_pi(105)
#     if matchDigit(pi):
#         print(f'===>π值 = {exact_pi_1001}')
#         print(f'===>π值~= {pi}')
#         print(f"===>matched upto 1,000 after-dec point\n")