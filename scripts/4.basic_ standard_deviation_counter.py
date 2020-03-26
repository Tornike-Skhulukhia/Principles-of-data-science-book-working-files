def get_std(nums):
    '''
    get list and return standard deviation of it
    '''
    import numpy as np

    mean = np.mean(nums)

    # calculate the mean of (deviations from means squares)
    squared_differences = []

    for num in nums:
        squared_differences.append((num - mean) ** 2)

    return np.sqrt(np.mean(squared_differences))


assert (get_std([31, 32, 32, 31, 28, 29, 31, 38, 32, 31, 30, 29, 30, 31, 26])) == 2.5157283018817607

