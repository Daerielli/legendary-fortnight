count = int(input("Введите количество билетов:"))
a = 0
age = int(input("Введите возраст посетителей:"))
for price in range (1, count + 1):
    if 18 <= age <= 25:
        price = 990
    elif 0 <= age <= 18:
        price = 0
    elif 25 <= age <= 99:
        price = 1390
    else:
        print("Введите корректный возраст!")
a = a + price
print(a)