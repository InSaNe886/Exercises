#Даны три числа. Определите, можно ли из отрезков с такими длинами составить треугольник.
#Определите вид треугольника (прямоугольный, тупоугольный, остроугольный), если он существует.
#Даны числа min и max. Найдите все треугольники с целочисленными длинами сторон от min до max включительно.
#Напишите программу, которая определяет,
#можно ли из четырех отрезков с данными длинами a, b, c и d составить прямоугольник.


#с тремя сторонами:

def pif(x, y, z):
    
    if x + y > z and y + z > x and z + x > y:
        
        if x * x + y * y - z * z > 0:
            return 'Остроугольный'

        elif x * x + y * y - z * z < 0:
            return 'Тупоугольный'

        else:
            return 'Прямоугольный'

    else:
        return 'Нельзя составить'


x = int(input())
y = int(input())
z = int(input())

print(pif(x, y, z))


#с числами min и max:

def pif(x, y, z):
    if x + y > z and y + z > x and z + x > y:

        if x * x + y * y - z * z > 0:
            return 'Остроугольный'

        elif x * x + y * y - z * z < 0:
            return 'Тупоугольный'

        else:
            return 'Прямоугольный'

    else:
        return 'Нельзя составить'

min = int(input())    #минимальная сторона
max = int(input())    #максимальная сторона

for x in range(min, max + 1):
    for y in range(x, max + 1):
        for z in range(y, max + 1):
            if x + y > z:
                type = pif(x, y, z)
                if type != 'нельзя':
                    print(x, y, z, type)

print(pif(x, y, z))


#прямоугольник:

def rect(a, b, c, d):
    if a > 0 and b > 0 and c > 0 and d > 0:
        
        if (a == c and b == d) or (a == b and c == d):
            return 'Можно'
        
        else:
            return 'Нельзя'

a = float(input())
b = float(input())
c = float(input())
d = float(input())

print(rect(a, b, c, d))

