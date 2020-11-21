# Randomized Matrix Multiplication
# from MIT 18.065 2018 Lecture 13

import numpy as np


def random_matrix(n, m):
    return np.random.rand(n, m)


def calculate_column_norm(matrix):
    return np.linalg.norm(np.transpose(matrix), axis=1)


def calculate_row_norm(matrix):
    return np.linalg.norm(matrix, axis=1)


def assign_probability(mat_A, mat_B):
    norm_A = calculate_column_norm(mat_A)
    norm_B = calculate_row_norm(mat_B)

    probability = norm_A * norm_B
    normalize = norm_A.dot(norm_B)
    return probability / normalize


def accumulate(prob):
    return np.cumsum(prob)

# Sample column index from probability
def sample_column_index(cum_prob):
    return np.searchsorted(cum_prob, np.random.rand(1))


def get_column(mat, i):
    return mat[:, i]


def get_row(mat, i):
    return mat[i, :]


def randomized_multiply(mat_A, mat_B, samples):
    prob = assign_probability(mat_A, mat_B)
    cum_prob = accumulate(prob)

    rows = mat_A.shape[0] if mat_A.ndim != 1 else 1
    cols = mat_B.shape[1] if mat_B.ndim != 1 else mat_B.shape[0]
    res = np.zeros((rows, cols))

    for _ in range(samples):
        i = sample_column_index(cum_prob)
        sample = get_column(mat_A, i).dot(get_row(mat_B, i)) / prob[i]
        res = np.add(res, sample)

    return res / samples


n, m = 10, 10
A = random_matrix(n, m)
B = random_matrix(n, m)
samples = 50

approximated = randomized_multiply(A, B, samples)
actual = np.matmul(A, B)
diff = approximated - actual

print(actual)
print(approximated)
print(diff)

# As number of samples increase, the error decreases
print(np.linalg.norm(diff))  # Frobenius norm
