#Написать программу нахождения целой части и остатка кубического корня из
#натурального числа (целочисленное извлечение кубического корня).
#Обобщить на корень произвольной натуральной степени, большей двух.

#с помощью бинарного поиска

def triple(n):
    
    left = 1
    right = n

    while right >= left:
        mid = (left + right) // 2

        if mid ** 3 == n:
            return mid
        
        elif n > mid ** 3:
            left = mid + 1
            
        else:
            right = mid - 1
    return right

n = int(input())
print(triple(n))

#обобщение корня произвольной натуральной степени

def triple(n):
    left = 1
    right = n

    while right >= left:
        mid = (left + right) // 2

        if mid ** k == n:
            return mid

        elif n > mid ** k:
            left = mid + 1

        else:
            right = mid - 1
    return right


n = int(input())
k = int(input())
print(triple(n))
