import random
import operator

def calc_game():
    print("Добро пожаловать в VD-games!")
    name = input("Как вас зовут? ")
    print(f"Привет, {name}!")
    print("Вычислите результат выражения.")

    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}
    rounds = 3

    for _ in range(rounds):
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        op_symbol = random.choice(list(ops.keys()))
        correct = ops[op_symbol](a, b)
        print(f"Вопрос: {a} {op_symbol} {b}")
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
    calc_game()

if __name__ == "__main__":
    main()
