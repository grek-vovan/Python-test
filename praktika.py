# Напиши программу, которая принимает на вход десятизначное число (например:1234567893) и находит в нём все четные числа.
a = input('вводите десятизначное число:')
b= str(a)
c=''
for x in a:
    if int(x) % 2 == 0:
     c=c+x
print(c)


