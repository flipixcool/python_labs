def min_max(arr):
    if len(arr) == 0:
        return 'ValueError'
    else:
        return (min(arr), max(arr))
def unique_sorted(arr):
    return list(set(sorted(arr)))
def flatten(arr):
    lst = []
    for i in arr:
        for j in i: 
            if isinstance(j, int) or isinstance(j, float):
                lst.append(j)
            else:
                return 'TypeError'
    return lst
arr = [[1, 2], [3, 4]] 
print(flatten(arr))