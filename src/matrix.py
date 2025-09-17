def transpose(mat):
    if len(mat) == 0 or mat == [[]]:
        return []
    for i in mat:
        if len(i) != len(mat[0]):
            return 'ValueError'
    lst = []
    for i in range(len(mat[0])):
        new_row = []
        for j in mat:
            new_row.append(j[i])
        lst.append(new_row)
    return lst

def row_sums(mat):
    for i in mat:
        if len(i) != len(mat[0]):
            return 'ValueError'
    lst = []
    for i in mat:
        lst.append(sum(i))
    return lst

def col_sums(mat):
    for i in mat:
        if len(i) != len(mat[0]):
            return 'ValueError'
    lst = [0] * len(mat[0])
    for i in mat:
        for j in range(len(mat[0])):
            lst[j] += i[j]          
    return lst

arr = [[1, 2, 3], [4, 5, 6]]
print(col_sums(arr))