import random

def progression_game():
    print("Добро пожаловать в VD-games!")
    name = input("Как вас зовут? ")
    print(f"Привет, {name}!")
    print("Определите пропущенное число в прогрессии.")

    rounds = 3

    for _ in range(rounds):
        length = random.randint(5, 10)
        start = random.randint(1, 20)
        step = random.randint(1, 10)
        hidden_index = random.randint(0, length - 1)
        progression = [start + i * step for i in range(length)]
        correct = progression[hidden_index]
        progression_display = progression.copy()
        progression_display[hidden_index] = ".."
        print("Вопрос:", " ".join(str(x) for x in progression_display))
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
    progression_game()

if __name__ == "__main__":
    main()
