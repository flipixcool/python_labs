a = input('ФИО: ').strip()
print('Инициалы: ',''.join([i[0].upper() for i in a.split()]), '.',sep='')
print("Длина (символов)", len(a)-4)
# print('Инициалы:', a[0] + b[0] + c[0])