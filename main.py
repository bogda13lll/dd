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