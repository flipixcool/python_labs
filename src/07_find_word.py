
line = input()
first_digit = 0
r = 0
while line:
    if line[r].isupper():
        first_digit = r
        break
    r += 1
second_digit = 0
while line:
    if line[r].isdigit():
        second_digit = r
        break
    r += 1
step = second_digit-first_digit
new_line = ''
for i in range(first_digit, line.index('.'), step + 1):
    new_line += line[i]
print(new_line)