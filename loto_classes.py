from random import randint, shuffle


class Card:
    lines = 3
    values = 9
    nums_in_line = 5
    empts_in_line = 4

    def __init__(self):
        numbers_list = list(range(1, 91))
        shuffle(numbers_list)

        self.lines_data = []  # Список из 3 списков — карта

        start_index = 0
        for _ in range(self.lines):
            line = []
            fulls = 0
            empts = 0

            for a in range(self.values):
                number = numbers_list[start_index + a]
                if empts < self.empts_in_line and fulls < self.nums_in_line:
                    if randint(0, 1) == 0:
                        line.append(None)  # пустое место
                        empts += 1
                    else:
                        line.append(number)
                        fulls += 1
                elif empts >= self.empts_in_line:
                    line.append(number)
                    fulls += 1
                else:  # fulls >= nums_in_line
                    line.append(None)
                    empts += 1
            start_index += self.values
            self.lines_data.append(line)

    def __str__(self):
        result = ''
        for line in self.lines_data:
            row_str = ''
            for val in line:
                if val is None:
                    row_str += '__ '
                elif isinstance(val, int):
                    row_str += f'{val:02d} '
                else:
                    # val уже зачёркнутое число (строка)
                    row_str += f'{val} '
            result += row_str.rstrip() + '\n'
        return result

    def has_number(self, number: int) -> bool:
        for line in self.lines_data:
            if number in line:
                return True
        return False

    def cross_number(self, number: int):
        # Заменяем число на зачёркнутое (обрамляем тильдами, например)
        for i, line in enumerate(self.lines_data):
            for j, val in enumerate(line):
                if val == number:
                    self.lines_data[i][j] = f'~{number:02d}~'


class Game:
    def __init__(self):
        self.user_card = Card()
        self.computer_card = Card()
        self.kegs = list(range(1, 91))
        shuffle(self.kegs)

    def __str__(self):
        return f'Ваша карта:\n{self.user_card}\nКомпьютер:\n{self.computer_card}'

    def play_round(self):
        if not self.kegs:
            print("Фишки закончились. Игра окончена.")
            return "draw"

        keg = self.kegs.pop()
        print(f'Новая фишка: {keg:02d} (осталось {len(self.kegs)})\n')
        print(f'Ваша карта:\n{self.user_card}')
        print(f'Карта компьютера:\n{self.computer_card}')

        answer = input('Зачеркнуть цифру? (да/нет): ').strip().lower()
        user_has = self.user_card.has_number(keg)

        # Проверяем ошибку пользователя
        if (answer == 'да' and not user_has) or (answer != 'да' and user_has):
            print('Вы ошиблись! Вы проиграли.')
            return 'lose'

        # Если пользователь зачёркивает, отмечаем число
        if user_has:
            self.user_card.cross_number(keg)

        # Компьютер автоматически зачёркивает, если есть
        if self.computer_card.has_number(keg):
            self.computer_card.cross_number(keg)

        # Проверяем, выиграл ли кто-то (все числа зачёркнуты)
        if self.check_win(self.user_card):
            print('Поздравляем! Вы выиграли!')
            return 'user_win'
        if self.check_win(self.computer_card):
            print('Компьютер выиграл!')
            return 'computer_win'

        return 'continue'

    @staticmethod
    def check_win(card: Card) -> bool:
        # Если в карте нет чисел (только None или зачёркнутые), значит выиграл
        for line in card.lines_data:
            for val in line:
                if isinstance(val, int):  # есть незачёркнутое число
                    return False
        return True


class PvPGame:
    def __init__(self, players: int):
        self.players = players
        self.card_list = [Card() for _ in range(players)]
        self.kegs = list(range(1, 91))
        shuffle(self.kegs)

    def show_cards(self):
        for idx, card in enumerate(self.card_list, 1):
            print(f'Карточка игрока {idx}:\n{card}')

    def play_round(self):
        if not self.kegs:
            print("Фишки закончились. Игра окончена.")
            return "draw"

        keg = self.kegs.pop()
        print(f'Новая фишка: {keg:02d} (осталось {len(self.kegs)})\n')

        for i in range(self.players):
            card = self.card_list[i]
            print(f'Карточка игрока {i + 1}:\n{card}')
            answer = input(f'Игрок {i + 1}, зачеркнуть цифру? (да/нет): ').strip().lower()
            has_num = card.has_number(keg)

            if (answer == 'да' and not has_num) or (answer != 'да' and has_num):
                print(f'Игрок {i + 1} ошибся! Выбыл из игры.')
                return f'player_{i+1}_lost'

        # Если все игроки ответили правильно — зачёркиваем
        for i in range(self.players):
            card = self.card_list[i]
            if card.has_number(keg):
                card.cross_number(keg)

        # Проверяем победителей
        winners = []
        for i, card in enumerate(self.card_list, 1):
            if Game.check_win(card):
                winners.append(i)

        if winners:
            if len(winners) == 1:
                print(f'Игрок {winners[0]} выиграл!')
                return f'player_{winners[0]}_win'
            else:
                print(f'Победители: {", ".join(map(str, winners))} (ничья)')
                return 'draw'

        return 'continue'


if __name__ == "__main__":
    mode = input("Выберите режим: 1 - против компьютера, 2 - PvP: ").strip()
    if mode == '1':
        game = Game()
        while True:
            result = game.play_round()
            if result != 'continue':
                break

    elif mode == '2':
        players_count = int(input("Введите количество игроков: "))
        game = PvPGame(players_count)
        game.show_cards()
        while True:
            result = game.play_round()
            if result != 'continue':
                break

    else:
        print("Неверный режим.")

