#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.
#Дополнительно: можете проверить, что это действительно число, и что это действительно входит в нужный диапазон

a = int(input('Введите цифру, обозначающую день недели => '))
if 0<a<=5:
    print (a, '-> нет')
elif 5<a<=7:
    print (a, '-> да')
else:
    print ('ошибка')