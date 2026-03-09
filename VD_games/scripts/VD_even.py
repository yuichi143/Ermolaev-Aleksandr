import random

def is_even_game():
    print("Добро пожаловать в VD-games!")
    name = input("Как вас зовут? ")
    print(f"Привет, {name}!")
    print('Ответьте "да", если число чётное, иначе "нет".')
    
    rounds = 3
    for _ in range(rounds):
        num = random.randint(1, 100)
        print(f"Вопрос: {num}")
        answer = input("Ваш ответ: ").lower()
        correct = "да" if num % 2 == 0 else "нет"
        if answer != correct:
            print(f"'{answer}' неверный ответ ;(. Правильный ответ был '{correct}'.")
            print(f"Попробуем снова, {name}!")
            return
        else:
            print("Верно!")
    print(f"Поздравляем, {name}!")

def main():
    is_even_game()

if __name__ == "__main__":
    main()
