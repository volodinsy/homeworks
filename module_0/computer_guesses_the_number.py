import random #подключаем модуль для генерации случайных чисел

number = random.randint(0, 101)#случайное целое число от "0" до "101"
guess = random.randint(0, 101)#случайное целое число от "0" до "101"

print('Компьютер загадал число "',number,'"\n')
print('Первое сгенерированное для угадывания число "',guess,'"\n')
tmp=[1,102]
attempts = 0 #Счётчик попыток
while guess != number:#цикл продолжается до тех пор, пока компьютер не угадает число
    attempts += 1
    if guess > number:
        print('Загаданное число меньше ', guess)
        tmp[1]=guess
        guess=(tmp[0]+tmp[1])//2
    else:
        print('Загаданное число больше ', guess)
        tmp[0] = guess
        guess = (tmp[0] + tmp[1]) // 2
print('\nУра! число угадано ', guess)
print('\nКоличество попыток алгоритма =', attempts)