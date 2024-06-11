import numpy as np


def calculate(numlist):
    if len(numlist) != 9:
        raise ValueError('List must contain nine numbers.')
    matrix = np.reshape(numlist, (3, 3))
    return {
        'mean': [list(np.mean(matrix, axis=0)), list(np.mean(matrix, axis=1)), np.mean(numlist)],
        'variance': [list(np.var(matrix, axis=0)), list(np.var(matrix, axis=1)), np.var(numlist)], 
        'standard deviation': [list(np.std(matrix, axis=0)), list(np.std(matrix, axis=1)), np.std(numlist)],
        'min': [list(np.min(matrix, axis=0)), list(np.min(matrix, axis=1)), np.min(numlist)],
        'max': [list(np.max(matrix, axis=0)), list(np.max(matrix, axis=1)), np.max(numlist)],
        'sum': [list(np.sum(matrix, axis=0)), list(np.sum(matrix, axis=1)), np.sum(numlist)]
    }
