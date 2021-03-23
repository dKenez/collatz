import matplotlib.pyplot as plt
import numpy as np
from math import log2

from collatz import collatz


# number until which to calculate
data_size = 100

# array for storing number of iterations for every number
v = np.empty((data_size, ), dtype=int)

# array for storing the theoretical minimum number of iterations for a given number (log2(n))
log2_nums = np.arange(1, data_size + 1)

log2_arr = np.vectorize(lambda n: log2(n))
log2_nums = log2_arr(log2_nums)

# iterate over the numbers until reaching data_size
for i in range(1, data_size + 1):
    iteration = 0
    num = i

    # calculate number of iterations to get to 1
    while True:
        if num == 1:
            break

        num = collatz(num)
        iteration += 1

    # save iterations in v array
    v[i - 1] = iteration

# plot results
plt.plot(v)
plt.plot(log2_nums)
plt.title('Number of iterations to reach 1')
plt.xlabel('number')
plt.ylabel('number of iterations')
plt.show()
