import random

while True:
    try:
        N = int(input("Введите нужное количество элементов массива: "))
        break
    except (TypeError, ValueError) as e:
        print("Упс, что-то пошло не так, попробуйте снова ввести целое число!", e)

res = []
for x in range(0, N):
    res.append(random.randint(0, 1000))


def sort(res):
    n = len(res)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if res[j] > res[j + 1]:
                res[j], res[j + 1] = res[j + 1], res[j]
    return res


print(*sort(res))
© 2022 GitHub, Inc.
Terms
Privacy
Security
St
