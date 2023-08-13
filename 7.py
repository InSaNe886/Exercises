#Написать несколько вариантов целочисленного извлечения квадратного корня из
#натурального числа. Сравнить способы по времени выполнения,
#количеству выполненных операций и диапазону применения.


#бинарный поиск:

def square(n):
    left = 1
    right = n

    while right >= left:
        mid = (left + right) // 2

        if mid ** 2 == n:
            return mid

        elif mid ** 2 < n:
            left = mid + 1

        else:
            right = mid - 1
    return right

n = int(input())
print(square(n))


#метод Ньютона:

def square(n):

    if n == 0:
        return 0

    x = n
    while True:
        guess = (x + n / x) // 2
        if abs(guess - x) < 1:
            return guess
        x = guess

n = int(input())
print(int(square(n)))


#перебор:

def square(n):
    for i in range(n + 1):
        if i ** 2 > n:
            return i - 1
    return n

n = int(input())
print(square(n))
