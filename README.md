# ЛР2
#### Задание 1

```Python
def min_max(arr):
    if len(arr) == 0:
        return 'ValueError'
    else:
        return (min(arr), max(arr))
def unique_sorted(arr):
    return tuple(set(sorted(arr)))
def flatten(arr):
    lst = []
    for i in arr:
        for j in i: 
            if isinstance(j, int) or isinstance(j, float):
                lst.append(j)
            else:
                return 'TypeError'
    return lst
arr = [3, -1, 5, 5, 0]
print(min_max(arr))
```

![alt text](images/image-1.1.png)
![alt text](images/image-1.2.png)
![alt text](images/image-1.3.png)