from random import randint


def bubble(array):
    for i in range(N - 1):
        for j in range(N - i - 1):
            if array[j] < array[j + 1]:
                buff = array[j]
                array[j] = array[j + 1]
                array[j + 1] = buff


N = 201
a = []
for i in range(201):
    a.append(randint(-100, 100))

print(a)
bubble(a)
print(a)