"""Лабораторная работа №2. Вариант №8. | Laboratory work #2. Option №8.
Написать программу, которая читая последовательность чисел из файла, выводит на экран десятки чисел, если в них есть более К одинаковых чисел.
Write a program that reads a sequence of numbers from a file and displays tens of numbers if there are more than K identical numbers."""


import time
import os

def array(x): # Функция, заполняющая массив.
    nums = []
    while x > 0:
        b = x % 10
        nums.append(b)
        x //= 10
    return list(reversed(nums))

try:
    print("\n-----Результат работы программы-----\n -----Локальное время",time.ctime(),"-----")
    while 1: # Проверка на то, чтобы число K было цифрой.
        digit = (input("Введите цифру K: "))
        if digit >= '0' and digit <= '9':
            k = int(digit)
            break
        else:
            print('Это не цифра.')
    start = time.time()
    with open("Test.txt", "r") as file: # Открытие файла.
        file.seek(0, os.SEEK_END)  # Проверка на пустоту файла.
        if file.tell():
            file.seek(0)
        else:
            print("\nФайл text.txt в директории проекта пустой.\nДобавьте не пустой файл в директорию или переименуйте существующий *.txt файл.")
        for line in file:
             print("\nЧисло:", line.strip())
             x = int(line.strip())
             a = array(x)
             b = []
             [b.append(i) for i in a if i not in b]
             if len(a) - len(b) == k: # Сравнивание длин неотсортированного и отсортированного числа.
                 print("Десятки числа: ", a[len(a) - 2])
             else:
                 if len(a) - len(b) < k and len(a) - len(b) != 0:
                     print("Дубликатов меньше, чем K\n")
                 if len(a) - len(b) > k and len(a) - len(b) != 0:
                     print("Дубликатов больше, чем K\n")
                 if len(a) - len(b) == 0:
                     print("Дубликатов нет\n")

    finish = time.time()
    result = finish - start
    print("Program time: " + str(result) + " seconds.")

except FileNotFoundError:
    print("\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
except ValueError:
    print("Файл text.txt содержит символы. Откорректируйте файл text.txt в директории или переименуйте существующий *.txt файл")