
import matplotlib.pyplot as plt
import numpy as np


views = [21, 230, 157, 253, 147, 1265, 151, 37, 57, 107, 142, 338, 301, 672, 479, 161, 158, 170, 198, 76, 290, 346, 101, 233, 134, 18, 94, 283, 1110, 91, 176, 211, 78, 57, 175, 166, 67, 112, 184, 119, 152, 79, 268, 169, 95, 242, 139, 736, 98, 154, 192, 171, 101, 267, 145, 102, 154, 207, 207, 239, 43, 1591, 255, 302, 65, 301, 152, 172, 150, 147, 73, 802, 102, 351, 120, 91, 166, 39, 69, 156, 211, 97, 748, 182, 79, 97, 177, 379, 178, 283, 118, 227, 1281, 234, 82, 478, 195, 282, 95, 239]
data_len = len(views)

mean = np.mean(views)
median = np.median(views)
std = np.std(views)



# actual data
plt.bar(range(data_len), views)

plt.plot((0, data_len - 1), (mean, mean), '*g-', linewidth=2)
plt.plot((0, data_len - 1), (mean + std, mean + std), 'b-',  linewidth=2)
plt.plot((0, data_len - 1), (mean - std, mean - std), 'r-',  linewidth=2)

plt.title('View Numbers')
plt.xlabel('Element')
plt.ylabel('Views')

plt.savefig('views.png')

plt.clf()

# Z-scores
z_scores = [(i - mean)/std for i in views]

plt.bar(range(data_len), z_scores)

plt.title('Z-scores Of Views')
plt.xlabel('Element')
plt.ylabel('Z-Score')

plt.savefig('z_scores.png')
# plt.show()

