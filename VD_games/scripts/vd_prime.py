import random
import prompt

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    print("Добро пожаловать в VD-игры!")
    name = prompt.string("Как вас зовут? ")
    print(f"Привет, {name}!")
    print('Ответьте "да", если число простое. В противном случае — "нет".')

    correct_answers = 0
    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f"Вопрос: {number}")
        answer = prompt.string("Ваш ответ: ")

        correct_answer = "да" if is_prime(number) else "нет"

        if answer.lower() == correct_answer:
            print("Верно!")
            correct_answers += 1
        else:
            print(f'"{answer}" — неверный ответ ;(. Правильный ответ был "{correct_answer}".')
            print(f"Попробуем снова, {name}!")
            return

    print(f"Поздравляем, {name}!")
    

if __name__ == "__main__":
    main()
