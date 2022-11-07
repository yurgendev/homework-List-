# Homework 5
# задача 1 про счастливый билетик
x = list(int(i) for i in input("enter numbers: "))
if sum(x[:2]) == sum(x[2:]):
    print('lucky')
else:
    print("unlucky")

# # задача 2 на проверку является ли вводимое шестизначное число полиандромом

poliandr = [int(i) for i in input("enter numbers: ")]
if sum(poliandr[:3]) == sum(reversed(poliandr[3:])):
    print('ok')
else:
    print('not polyandr')


# Задача 3 Дано коло з центром на початку координат та радіусом 4.
# Користувач вводить з клавіатури координати точки x та y.
# Написати програму, яка визначить, лежить ця точка всередині кола чи ні.

r = 4
x, y = int(input('x=')), int(input('y='))
d = x ** 2 + y ** 2

if r == d:
    print('on circle')
elif r < d:
    print('inside of circle')
else:
    print('out of circle')




