print("*" * 10, " КРЕСТИКИ-НОЛИКИ ДЛЯ 2-х ИГРОКОВ ", "*" * 10)

play_field = list(range(1, 10))

winn_comb = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


# Определение глобальной переменной (список с числами от"1" до "9")

def print_play_field(play_field):  # функция печатает игровое поле
    print("-" * 13)
    for i in range(3):
        print("|", play_field[0 + i * 3], "|", play_field[1 + i * 3], "|", play_field[2 + i * 3], "|")
        print("-" * 13)


# Задаём цикл от "0" до "2"
# За один проход цикла будет печататься одна строка игрового поля
# с числами из нашей глобальной переменной


def participate(player_token):
    while True:
        value = input("Куда поставим " + player_token + "? ")
        if not (value in '123456789'):
            print('Некорректный ввод. Повторите')
            continue
        value = int(value)
        if str(play_field[value - 1]) in 'XO':  # Проверка занята эта ячейка или нет
            print("Эта клетка уже занята!")
            continue
        play_field[value - 1] = player_token
        break


def victory(play_field):
    for each in winn_comb:
        if play_field[each[0] - 1] == play_field[each[1] - 1] == play_field[each[2] - 1]:
            return play_field[each[1] - 1]
    else:
        return False


def main(play_field):
    counter = 0
    while True:
        print_play_field(play_field)
        if counter % 2 == 0:
            participate('X')
        else:
            participate('O')
        if counter > 3:
            winner = victory(play_field)
            if winner:
                print_play_field(play_field)
                print(winner, "выиграл!")
                break
        counter += 1
        if counter > 8:
            print_play_field(play_field)
            print("Ничья!")
            break


main(play_field)

input("Нажмите Enter для выхода!")
