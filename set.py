#Проверить, есть ли в последовательности чисел списка дубликаты.

a = [1,2,4,5,3,7,2,5,5]
b=set(a)
print(set(a))
if len(a)==len(b) :
	print('нет дубликотов')
else:
	print('да есть дубликаты')