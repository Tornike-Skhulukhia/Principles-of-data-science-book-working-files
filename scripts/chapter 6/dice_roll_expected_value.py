import random
import matplotlib.pyplot as plt
plt.style.use('dark_background')

def get_rand_result():
    return random.randint(1, 6)

means = []
try_nums = list(range(10, 10_000, 10))

# test means for different number of experiments
for try_num in try_nums:
    mean = sum([get_rand_result() for _ in range(try_num)]) / try_num
    means.append(mean)
    if try_num % 1000 == 0:
        print(try_num)

plt.plot(try_nums, means)
plt.show()