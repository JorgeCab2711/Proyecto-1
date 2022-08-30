def matrix(rows, columns, anyList):
    matrix = []
    for m in range(rows):
        ListRow = []
        for k in range(columns):
            ListRow.append(anyList[rows * m + k])
        matrix.append(ListRow)
    return matrix
