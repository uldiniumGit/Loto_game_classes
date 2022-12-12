from random import randint, shuffle


# Класс описывает карту игрока. Она создается случайно по правилам игры лото.
class Card:
    # Количество рядов в карте
    lines = 3
    # Количество значений в ряду
    values = 9
    # Количество чисел среди значений
    nums_in_line = 5
    # Количество пустых значений
    empts_in_line = 4

    def __init__(self):

        # Строка, в которой хранится сама карта
        self.line = ''
        numbers_list = list(range(1, 90))
        shuffle(numbers_list)

        # Цикл создает нужное количество рядов. Цикл внутри этого правильно генерирует один ряд.
        for i in range(self.lines):
            # Переменные для подсчета количества пустых и заполненных значений в ряду
            fulls = 0
            empts = 0

            # Цикл генерирует один ряд
            for a in range(self.values):
                number = str(numbers_list[a + self.values * (i - 1)])
                if empts < self.empts_in_line and fulls < self.nums_in_line:
                    x = randint(0, 1)
                    if x == 0:
                        self.line += '_'
                        empts += 1
                    else:
                        if len(number) == 1:
                            self.line += '0'
                        self.line += number
                        fulls += 1

                elif empts >= self.empts_in_line:
                    if len(number) == 1:
                        self.line += '0'
                    self.line += number

                elif fulls >= self.nums_in_line:
                    self.line += str('_')

                if a + 1 < self.values:
                    self.line += ' '

            if i + 1 < self.lines:
                self.line += '\n'


class Game:
    user_card = None
    computer_card = None

    kegs = list(range(1, 90))
    shuffle(kegs)
    game_over = False

    def __init__(self):
        self.user_card = Card()

        self.computer_card = Card()

    def play_round(self):
        """
        :return:
        0 - game must go on
        1 - user wins
        2 - computer wins
        """

        keg = str(self.kegs.pop())
        if len(str(keg)) < 2:
            keg = '0' + keg
        print(f'Новая фишка: {keg} (осталось {len(self.kegs)})\n')
        print(f'Ваша карточка:\n{self.user_card.line}\n')
        print(f'Карточка компьютера:\n{self.computer_card.line}\n')

        user_answer = input('Зачеркнуть цифру? (да/нет)\n').lower()
        if user_answer == 'да' and keg not in self.user_card.line or user_answer != 'да' and keg in self.user_card.line:
            return 3

        if keg in self.user_card.line and keg in self.computer_card.line:
            self.user_card.line = self.user_card.line.replace(keg, keg[0] + '̶' + keg[1] + '̶')
            self.computer_card.line = self.computer_card.line.replace(keg, keg[0] + '̶' + keg[1] + '̶')
            return 4

        if keg in self.user_card.line:
            self.user_card.line = self.user_card.line.replace(keg, keg[0] + '̶' + keg[1] + '̶')
            return 1

        if keg in self.computer_card.line:
            self.computer_card.line = self.computer_card.line.replace(keg, keg[0] + '̶' + keg[1] + '̶')
            return 2

        return 0


'''
'''


class GameCompVsComp(Game):

    def __init__(self):
        Game.__init__(self)

    def play_round(self):
        """
        :return:
        0 - game must go on
        1 - computer 1 wins
        2 - computer 2 wins
        """

        keg = str(self.kegs.pop())
        if len(str(keg)) < 2:
            keg = '0' + keg
        print(f'Новая фишка: {keg} (осталось {len(self.kegs)})\n')
        print(f'Карточка бота 1:\n{self.user_card.line}\n')
        print(f'Карточка бота 2:\n{self.computer_card.line}\n')

        if keg in self.user_card.line and keg in self.computer_card.line:
            self.user_card.line = self.user_card.line.replace(keg, keg[0] + '̶' + keg[1] + '̶')
            self.computer_card.line = self.computer_card.line.replace(keg, keg[0] + '̶' + keg[1] + '̶')
            return 4

        if keg in self.user_card.line:
            self.user_card.line = self.user_card.line.replace(keg, keg[0] + '̶' + keg[1] + '̶')
            return 1

        if keg in self.computer_card.line:
            self.computer_card.line = self.computer_card.line.replace(keg, keg[0] + '̶' + keg[1] + '̶')
            return 2

        return 0


class GamePVP(Game):

    def __init__(self):
        Game.__init__(self)

    def play_round(self):
        """
        :return:
        0 - game must go on
        1 - user 1 wins
        2 - user 2 wins
        """

        keg = str(self.kegs.pop())
        if len(str(keg)) < 2:
            keg = '0' + keg
        print(f'Новая фишка: {keg} (осталось {len(self.kegs)})\n')
        print(f'Карточка игрока 1:\n{self.user_card.line}\n')
        print(f'Карточка игрока 2:\n{self.computer_card.line}\n')

        user01_answer = input('Ход игрока 1. Зачеркнуть цифру? (да/нет)\n').lower()
        if user01_answer == 'да' and keg not in self.user_card.line or user01_answer != 'да' and keg in self.user_card.line:
            return 3

        user02_answer = input('Ход игрока 2. Зачеркнуть цифру? (да/нет)\n').lower()
        if user02_answer == 'да' and keg not in self.computer_card.line or user02_answer != 'да' and keg in self.computer_card.line:
            return 3

        if keg in self.user_card.line and keg in self.computer_card.line:
            self.user_card.line = self.user_card.line.replace(keg, keg[0] + '̶' + keg[1] + '̶')
            self.computer_card.line = self.computer_card.line.replace(keg, keg[0] + '̶' + keg[1] + '̶')
            return 4

        if keg in self.user_card.line:
            self.user_card.line = self.user_card.line.replace(keg, keg[0] + '̶' + keg[1] + '̶')
            return 1

        if keg in self.computer_card.line:
            self.computer_card.line = self.computer_card.line.replace(keg, keg[0] + '̶' + keg[1] + '̶')
            return 2

        return 0
