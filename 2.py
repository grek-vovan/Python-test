#Пользователь вводит два числа с клавиатуры,  необходимо вывести на экран все отрицательные числа, лежащие между ними.
# Например, пользователь ввел -5 и 3, на экране вывелось -4,-3,-2,-1
a=int(input('введите первое число:'))
b=int(input('введите второе число:'))

if b>=a or a>=b :
   while b>=a or a>=b :
      if a>0 and b>0  :
        print('неверное число')
        break
      elif a<b and b<-1:
          a+=1
          print(a)
      elif  a>b and b<-1:
         b+=1
         print(b)
      elif b >a and a<-1 :
        a += 1
        print(a)
      elif b<a and b>-1  :
          print('неверное число')
          break
      elif  a==b and a>=0 :
          print('неверное число')
          break

