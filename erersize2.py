result = None # summory result
operand =None # save the flowing number
operator = None # parameter of FOUR meanings "+", "-", "*". "/"
wait_for_number = True # Flag, show us what must be enter (-nd or -or)


# while True:
#     r = int(input('Plese enter a number: '))
#     for i in range(0, 9):
#         continue




    # ===============================


    while True:
    # Запитати користувача про операцію та числа
    operator = input("Введіть операцію (+,-,*,/): ")
    if operator not in ['+', '-', '*', '/']:
        print("Некоректна операція")
        continue
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))

    # Обчислити результат відповідно до операції
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Помилка: Ділення на нуль")
            continue
        result = num1 / num2

    # Вивести результат
    print(f"Результат: {result}")
    # Запитати користувача, чи він бажає продовжити роботу з калькулятором
    choice = input("Бажаєте продовжити? (y/n): ")
    if choice.lower() != 'y':
        break
    
