#Выведи на экран все числа в диапазоне от 54 до 9184 кратные 5

i=int(input('введите число нижнего диапозона:'))
a=int(input('введите число верхнего диапозона: '))
n=int(input('введите кратное число:'))
for x in range(i,a+1):
    if x%n==0:
        print(x)
