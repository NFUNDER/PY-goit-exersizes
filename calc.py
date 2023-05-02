result = None
operand = None
operator = None
wait_for_number = True


while True:
 
    # Запитати користувача про операцію та числа
    operator = input("Введіть операцію (+,-,*,/): ")
    if operator not in ['+', '-', '*', '/']:
        print("Некоректна операція")
        continue

    operand1 = int(input("Enter first number: "))

    operand2 = int(input("enter second number: "))
    if operand1 and operand2 not in range(0, 9):
        print("Некоректна операція")
        break
 
    # Обчислити результат відповідно до операції
    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        if operand2 == 0:
            print("Помилка: Ділення на нуль")
            continue
        result = operand1 / operand2

    # Вивести результат
    print(f"Результат: {result}")
    # Запитати користувача, чи він бажає продовжити роботу з калькулятором
    choice = input("Бажаєте продовжити? (y/n): ")
    if choice.lower() != 'y':
        break