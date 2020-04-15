from import_helpers import (
                            np,
                            pd,
                            plt,
                            )
from scipy import stats
from scipy.stats import poisson

# why do they use loc > 0 in the book???
long_breaks = poisson.rvs(loc=0, mu=60, size=3000)
short_breaks = poisson.rvs(loc=0, mu=15, size=6000)
breaks = np.concatenate([long_breaks, short_breaks])

# pd.Series(breaks).hist()

parameter = np.mean(breaks)
print(f'Population parameter - Mean = {parameter:.3f}')

sample_breaks = np.random.choice(breaks, size=100)
print(f'Point estimate - Mean based on sample = {np.mean(sample_breaks):.3f}')

# calculate more samples
point_estimates = [np.mean(np.random.choice(breaks, 100)) for _ in range(500)]
estimates_mean = np.mean(point_estimates)

print(f'Mean of 500 point estimates = {estimates_mean:.3f}')
print(f'Difference from parameter {estimates_mean - parameter:.3f} ({(estimates_mean - parameter) / parameter * 100:.3f}%)')

plt.title('Distribution of 500 point estimate means')
pd.Series(point_estimates).hist(bins=50)

plt.show()
