from loto_classes import Game, GameCompVsComp, PvPGame


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

    # Класс для игры человека против человека отличается от других, так что игру проведем тоже отдельно от других
    elif game_type == 3:
        players = int(input('введите кол-во игроков\n'))
        game = PvPGame(players)

        # Создаем словарь для подсчета очков
        players_score_dict = {}
        for i in range(players):
            players_score_dict[str(i + 1)] = 0

        while True:

            # Выводим в терминал карты всех игроков
            game.show_cards(players)

            # Проводим раунд
            result = game.play_game(players)

            # Если игрок ошибается, он сразу проигрывает
            if result == 'you_lost':
                print('Вы проиграли')
                break

            # result возвращает список с номерами победивших в раунде игроков, добавляем им по одному очку
            for k, v in players_score_dict.items():
                if k in result:
                    players_score_dict[k] += 1
                    # Выводим счет
                    print('Счет игроков: ', players_score_dict)

            # Игра ведется до трех очков. Подводим итоги
            if 3 in players_score_dict.values():
                list_01 = players_score_dict.keys()
                list_02 = players_score_dict.values()
                x = [i for i, ltr in enumerate(list_02) if ltr == 1]
                winners = ([v for k, v in enumerate(list_01) if k in x])
                print('Победили игроки', winners)
                break

        # Если игра шла по этому сценарию, то она заканчивается на этом моменте
        quit()

    else:
        print('Некорректный пункт меню')

# Если игрок выбрал варианты 'Человек против компьютера' или 'Компьютер против компьютера', то идем сюда.
# Создаем переменные для подсчета очков
player_score = 0
computer_score = 0

# Игра продолжается, пока кто-нибудь не наберет 3 очка или не ошибется с ответом
while player_score < 3 and computer_score < 3:
    if game_type == 1:
        print(f'Ваши очки: {player_score}\nОчки бота: {computer_score}')
    elif game_type == 2:
        print(f'Очки первого бота: {player_score}\nОчки второго бота: {computer_score}')

    # Проводим раунд
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

# Подводим итоги игры
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
