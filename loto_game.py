from loto_classes import Game, GameCompVsComp, GamePVP

print('')
print('Игра лото')
print('')
print('1. Игрок против компьютера')
print('2. Компьютер против компьютера')
print('3. Игрок против игрока')

while True:

    game_type = int(input('\nВыберите пункт меню\n'))

    if game_type == 1:
        game = Game()
        break

    elif game_type == 2:
        game = GameCompVsComp()
        break

    elif game_type == 3:
        game = GamePVP()
        break

    else:
        print('Некорректный пункт меню')

player_score = 0
computer_score = 0

while player_score < 3 and computer_score < 3:
    if game_type == 1:
        print(f'Ваши очки: {player_score}\nОчки бота: {computer_score}')
    elif game_type == 2:
        print(f'Очки первого бота: {player_score}\nОчки второго бота: {computer_score}')
    elif game_type == 3:
        print(f'Очки первого игрока: {player_score}\nОчки второго игрока: {computer_score}')

    result = game.play_round()
    if result == 0:
        pass
    elif result == 1:
        player_score += 1
    elif result == 2:
        computer_score += 1
    elif result == 3:
        print('Вы проиграли')
        break
    elif result == 4:
        player_score += 1
        computer_score += 1

if game_type == 1:
    if player_score == 3:
        print('Вы победили')
    if computer_score == 3:
        print('Вы проиграли')

elif game_type == 2:
    if player_score == 3:
        print('Победил бот 1')
    if computer_score == 3:
        print('Победил бот 2')

elif game_type == 3:
    if player_score == 3:
        print('Победил игрок 1')
    if computer_score == 3:
        print('Победил игрок 2')
