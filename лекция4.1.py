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
#либо так res = random.sample(range(0, 1000), N)
print(*res)
