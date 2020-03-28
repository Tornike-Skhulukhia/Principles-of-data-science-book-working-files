'''
    Class to multiply matrices
'''

class Matrix:
    '''
    For 2D matrices
    '''
    def __init__(self, data):
        '''
        gets data in form:
            [
                [1, 2, 3],
                [9, 6, 4],
                [7, 0, 8],
            ]
        '''
        self._data = data
        self.shape = (len(data), len(data[0]))  # just ignore error cases in initialization for now
        self._col_width = max([len(str(j)) for i in data for j in i]) + 1 if len(data) else 0

    def __str__(self):
        return "\n".join([" ".join([str(j).rjust(self._col_width) for j in i]) for i in self._data])

    def __repr__(self):
        return self.__str__()

    def __mul__(self, other):
        '''
        multiply matrices and return the result as the same Matrix object
        '''
        if not isinstance(other, Matrix):
            return "Please use Matrices only"
        if self.shape[1] != other.shape[0]: 
            return f"Can not multiply {self.shape} and {other.shape} shape matrices"

        # multiply
        res = []

        for row in self._data:
            res_row = []
            for col_index, _ in enumerate(other._data[0]):
                multiply_by = [i[col_index] for i in other._data]
                res_row.append(sum([i * j for i, j in zip(row, multiply_by)]))
            res.append(res_row)
        return Matrix(res)


################
# test
################
import numpy as np

# make few quick checks
for i in range(10):
    # random 3x3 matrix
    a = np.random.randint(1, 100, (3, 3))
    b = np.random.randint(1, 100, (3, 3))

    c = Matrix(a) * Matrix(b)

    np_res = np.dot(np.array(a), np.array(b))
    assert np.array_equal(np_res, np.array(c._data))

    # random 4x7 matrix
    a = np.random.randint(1, 100, (4, 7))
    b = np.random.randint(1, 100, (7, 9))

    c = Matrix(a) * Matrix(b)

    np_res = np.dot(np.array(a), np.array(b))
    assert np.array_equal(np_res, np.array(c._data))

