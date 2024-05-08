import numpy as np

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps

    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    ### YOUR CODE HERE
    eigenvector = np.random.rand(data.shape[1])

    for _ in range(num_steps):
        data_dot_eigv = np.dot(data, eigenvector)
        eigenvector_1 = data_dot_eigv / np.linalg.norm(data_dot_eigv)
        if np.linalg.norm(eigenvector_1 - eigenvector) < 1e-6:
            break
        eigenvector = eigenvector_1
    eigenvalue = float(np.dot(eigenvector, np.dot(data, eigenvector)) / np.dot(eigenvector, eigenvector))

    return eigenvalue, eigenvector