import numpy as np


def visit_island(
    islands_matrix: np.ndarray, row_to_visit: int, column_to_visit: int
) -> None:
    """
    Visit the island recursively
    Can be reimplemented using pure function with returning the visited matrix as a result
    :param islands_matrix: Input matrix of islands
    :param row_to_visit: row to visit
    :param column_to_visit: column to visit
    :return: None (change the matrix in place)
    """

    if (
        row_to_visit < 0
        or row_to_visit >= islands_matrix.shape[0]
        or column_to_visit < 0
        or column_to_visit >= islands_matrix.shape[1]
        or islands_matrix[row_to_visit][column_to_visit] == 0
    ):
        # Check out of bounds or not an island
        # 0 in islands_matrix means that cell is not an island or the cell is already visited
        return

    # Current cell is visited so not consider it anymore
    islands_matrix[row_to_visit][column_to_visit] = 0

    visit_island(islands_matrix, row_to_visit - 1, column_to_visit)
    visit_island(islands_matrix, row_to_visit, column_to_visit - 1)
    visit_island(islands_matrix, row_to_visit + 1, column_to_visit)
    visit_island(islands_matrix, row_to_visit, column_to_visit + 1)


def get_islands_count_recursive(
    islands_matrix_shape: tuple[int, int], islands_matrix: np.ndarray
) -> int:
    """
    Get the number of islands in the 2D matrix
    :param islands_matrix_shape: Shape of the matrix
     (needed by problem definition, but function can be implemented without it)
    :param islands_matrix: Input matrix of islands
    :return: Number of islands in the matrix
    """
    # Since method changes the matrix in place, we need to copy it to avoid changing the original matrix
    islands_matrix = islands_matrix.copy()
    if islands_matrix_shape != islands_matrix.shape:
        raise ValueError("Invalid shape")

    islands_count = 0

    # Check all cells in the matrix
    for i in range(islands_matrix_shape[0]):
        for j in range(islands_matrix_shape[1]):
            # If cell is not an island or already visited, continue
            if islands_matrix[i][j] == 0:
                continue

            # Visit the island otherwise anb increase the count
            visit_island(islands_matrix, i, j)
            islands_count += 1

    return islands_count
