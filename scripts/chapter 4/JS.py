'''
    No, we are not writing browser scripts here :-)
'''

def jaccard_measure_between(set_1, set_2):
    '''
    shows how similar the sets are 
    '''
    res = len(set_1 & set_2) / len(set_1 | set_2)

    return res


A = {1, 2, 3}
B = {5, 7, 1}

assert jaccard_measure_between(A, B) == 0.2
