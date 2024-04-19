from piLib import pi_BBP
import time

ndigits = 10_000
print(f'Estimating π in {ndigits:,} digits after-decimal:')

start_time = time.time()
pi = pi_BBP(ndigits)
stop_time = time.time()
time_taken = stop_time - start_time
print(f'===>Took {time_taken} seconds.')

digits=str(pi)

# Extract the first digit of every 100-blocks in the last 1000 digits
for n in range(ndigits-1000, ndigits+1, 100):
    print(f'===>{n:,}-th digit\t {digits[n]}')

# Extract the last 10 digits
last10 = ndigits - 9
print(f'Last 10 digits of estimated π: {digits[last10:]}')
