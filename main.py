def array(x):
    nums = []
    while x > 0:
        b = x % 10
        nums.append(b)
        x //= 10
    return list(reversed(nums))

k = int(input('Введите число K: '))

with open("Test.txt", "r") as F:
    for line in F:
        print("\nЧисло:", line.strip())
        x = int(line.strip())
        a = array(x)
        b = []
        [b.append(i) for i in a if i not in b]
        if len(a) - len(b) == k:
            print("Десятки числа: ", a[len(a) - 2])
        else:
            if len(a) - len(b) < k and len(a) - len(b) != 0:
                print("Дубликатов меньше, чем K\n")
            if len(a) - len(b) > k and len(a) - len(b) != 0:
                print("Дубликатов больше, чем K\n")
            if len(a) - len(b) == 0:
                print("Дубликатов нет\n")








