#Ввести в файл ‘input.txt’ 2 числа в одну строку через пробел. Вывести в файл ‘output.txt’ их разность



x = int(input())
y = int(input())
with open('input.txt', 'w') as f_input, open('output.txt', 'w') as f_output:
   f_input.write(f'{x} {y}')
   f_output.write(f'{x-y}')
