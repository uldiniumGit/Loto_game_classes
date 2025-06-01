from loto_classes import Game, GameCompVsComp, PvPGame

print('\nИгра лото\n')
print('1. Игрок против компьютера')
print('2. Компьютер против компьютера')
print('3. Игрок против игрока')

while True:
    try:
        game_type = int(input('\nВыберите пункт меню: '))
    except ValueError:
        print('Введите корректное число.')
        continue

    if game_type == 1:
        game = Game()
        break

    elif game_type == 2:
        game = GameCompVsComp()
        break

    elif game_type == 3:
        players = int(input('Введите количество игроков: '))
        game = PvPGame(players)

        # Словарь для подсчета очков каждого игрока
        players_score_dict = {str(i + 1): 0 for i in range(players)}

        while True:
            # Показываем карты всех игроков
            game.show_cards()

            # Проводим раунд
            result = game.play_round()

            if result == 'you_lost':
                print('Вы проиграли')
                break

            # result — список игроков, которые выиграли раунд, добавляем им очки
            if isinstance(result, list):
                for player_num in result:
                    if player_num in players_score_dict:
                        players_score_dict[player_num] += 1

                print('Счет игроков:', players_score_dict)

            elif isinstance(result, str) and result.startswith('player_'):
                # Например: 'player_2_win' или 'player_3_lost'
                parts = result.split('_')
                player_num = parts[1]
                status = parts[2]
                if status == 'win':
                    players_score_dict[player_num] = players_score_dict.get(player_num, 0) + 1
                    print(f'Игрок {player_num} выиграл раунд!')
                    print('Счет игроков:', players_score_dict)
                elif status == 'lost':
                    print(f'Игрок {player_num} выбыл из игры.')
                    # Можно добавить логику удаления игрока из игры, если надо

            # Игра идет до 3 очков
            if any(score >= 3 for score in players_score_dict.values()):
                winners = [k for k, v in players_score_dict.items() if v >= 3]
                print('Победили игроки:', ', '.join(winners))
                break

        quit()

    else:
        print('Некорректный пункт меню')

# Для режимов 1 и 2 — играем до 3 очков или ошибки
player_score = 0
computer_score = 0

while player_score < 3 and computer_score < 3:
    if game_type == 1:
        print(f'Ваши очки: {player_score}\nОчки бота: {computer_score}')
    elif game_type == 2:
        print(f'Очки первого бота: {player_score}\nОчки второго бота: {computer_score}')

    result = game.play_round()

    # Обработка результата:
    # Предполагается, что метод play_round возвращает:
    # 0 — продолжить,
    # 1 — выиграл игрок,
    # 2 — выиграл компьютер,
    # 3 — игрок ошибся (проигрыш),
    # 4 — ничья (оба получили очко)
    if result == 0:
        continue
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

# Итоги
if game_type == 1:
    if player_score == 3:
        print('Вы победили')
    elif computer_score == 3:
        print('Вы проиграли')

elif game_type == 2:
    if player_score == 3:
        print('Победил бот 1')
    elif computer_score == 3:
        print('Победил бот 2')
