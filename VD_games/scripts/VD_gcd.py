import random
import math

def gcd_game():
    print("Добро пожаловать в VD-games!")
    name = input("Как вас зовут? ")
    print(f"Привет, {name}!")
    print("Найдите наибольший общий делитель (НОД) данных чисел.")

    rounds = 3

    for _ in range(rounds):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        correct = math.gcd(a, b)
        print(f"Вопрос: {a} {b}")
        try:
            answer = int(input("Ваш ответ: "))
        except ValueError:
            print(f"'{answer}' неверный ответ ;(. Правильный ответ был '{correct}'.")
            print(f"Попробуем снова, {name}!")
            return
        if answer != correct:
            print(f"'{answer}' неверный ответ ;(. Правильный ответ был '{correct}'.")
            print(f"Попробуем снова, {name}!")
            return
        else:
            print("Верно!")
    print(f"Поздравляем, {name}!")

def main():
    gcd_game()

if __name__ == "__main__":
    main()
