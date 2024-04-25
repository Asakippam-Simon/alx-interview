def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # Set first element of each row to 1
        if i > 0:
            # Calculate each element of the current row based on the previous row
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)  # Set last element of each row to 1
        triangle.append(row)

    return triangle
