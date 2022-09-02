# Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых файла: test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
# После этого удалите созданную папку.
# Все операции выполнять с помощью встроенных функций библиотеки os
import os


#os.mkdir(r"C:\Users\Grek\Desktop\Files")
os.chdir(r"C:\Users\Grek\Desktop\Files")
os.chdir('..')
#os.makedirs('f1.txt/f2.txt/f3.txt')
#os.removedirs('f3.txt')
# os.mkdir('f1.txt')
# os.mkdir('f2.txt')
# os.mkdir('f3.txt')
# os.rename('f1.txt','rename_1.txt')
# os.rename('f2.txt','rename_2.txt')
# os.rename('f3.txt','rename_3.txt')
#os.rmdir('rename_1.txt')
#os.rmdir('rename_2.txt')
#os.rmdir('rename_3.txt')
os.rmdir('Files')
print(os.getcwd())


