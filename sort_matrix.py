def sort_matrix(matrix):
    # Flatten the matrix
    flat = [num for row in matrix for num in row]

    # Sort all elements
    flat.sort()

    # Reshape back into matrix with original dimensions
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    sorted_matrix = []
    for i in range(rows):
        # Create each row from flatten
        sorted_matrix.append(flat[i*cols:(i+1)*cols])

    return sorted_matrix


# Example
matrix = [
    [3, 2, 1],
    [6, 5, 4],
    [16, -5, 44]
]

sorted_mat = sort_matrix(matrix)
for row in sorted_mat:
    print(row)
