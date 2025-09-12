n = int(input())
full_time = 0
for i in range(n):
    full_information = input().split()
    if full_information[3] == 'True':
        full_time += 1
print(full_time, n-full_time)