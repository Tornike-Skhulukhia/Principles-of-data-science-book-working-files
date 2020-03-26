def get_geometric_mean(nums):
    '''
    returns geometric mean of numbers list
    '''
    import numpy as np

    product = 1

    for num in nums:
        product *= num

    return product ** (1 / len(nums))

assert get_geometric_mean(
            [31, 32, 32, 31, 28, 29, 31, 38, 32, 31, 30, 29, 30, 31, 26]) == 30.63473484374659


