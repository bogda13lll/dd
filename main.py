import random 
name = input("Введіть ваше ім'я: ")
age_input = input("Введіть ваш вік: ")
age = int(age_input)
print("Привіт {}, тобі {}!".format(name, age))
if age > 18:
    print("Вхід дозволено!")
else:
    print("Вхід заборонено!")
secret_number = random.randint(1, 10)
attempts = 3
print("Я загадав число від 1 до 10. У тебе є 3 спроби!")
for i in range(attempts):
    guess = int(input("Спроба №" + str(i + 1) + ". Введи число: "))
    if guess == secret_number:
        print("Вгадав!")
        break
    elif guess > secret_number:
        print("Менше")
    else:
        print("Більше")
if guess != secret_number:
    print("Спроби закінчилися. Було число " + str(secret_number))
    start = int(input("Введіть число з якого починати: "))
end = int(input("Введіть число по яке виводити: "))
print("Список чисел від " + str(start) + " до " + str(end) + ":")
for i in range(start, end + 1):
    print(i)
n = int(input("Введіть число n: "))
print("Парні числа від " + str(n) + " до 1 у зворотному порядку:")
for i in range(n, 0, -1):
    if i % 2 == 0: 
        print(i, end=" ") 
        score = int(input("Введіть кількість балів (0-100): "))

if score >= 0 and score <= 49:
    print("Незадовільно")
elif score >= 50 and score <= 69:
    print("Задовільно")
elif score >= 70 and score <= 89:
    print("Добре")
elif score >= 90 and score <= 100:
    print("Відмінно")
else:
    print("Помилка: введіть число від 0 до 100")