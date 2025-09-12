# ЛР1
#### Задание 1

``` Python
name = input('Имя: ')
age = int(input("Возраст: "))
print(f'Привет {name}! Через год тебе будет {age + 1}')
```

![alt text](image.png)
#### Задание 2

``` Python
a = float(input('a: '))
b = float(input('b: '))
print(f'sum={a+b}; avg={3.88}')
```
![alt text](image-1.png)


#### Задание 3
```Python
price = float(input())
discount = float(input())
vat = float(input())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скидки: {base}')
print(f'НДС: {vat_amount}')
print(f'Итого к оплате: {total}')
```
![alt text](image.png)
#### Задание 4
``` Python
m = int(input("Минуты: "))
print(f'{m//60}:{m % 60}')
```
![alt text](image-2.png)
####  Задание 5
``` Python
a = input('ФИО: ').strip()
print('Инициалы: ',''.join([i[0].upper() for i in a.split()]), '.',sep='')
print("Длина (символов)", len(a)-4)
```
![alt text](image-1.png)