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


# Основной класс для игры
class Game:
    user_card = None
    computer_card = None

    # Лист с фишками
    kegs = list(range(1, 91))
    shuffle(kegs)

    # Создаем объекты ранее написанного класса Card
    def __init__(self):
        self.user_card = Card()

        self.computer_card = Card()

    # Функция, проводящая один раунд игры
    def play_round(self):

        # Достаем фишку из листа
        keg = str(self.kegs.pop())
        # Добавляем нолик для красивого отображения в терминале
        if len(str(keg)) < 2:
            keg = '0' + keg

        # Выводим в терминал фишку и карточки игроков
        print(f'Новая фишка: {keg} (осталось {len(self.kegs)})\n')
        print(f'Ваша карточка:\n{self.user_card.line}\n')
        print(f'Карточка компьютера:\n{self.computer_card.line}\n')

        # Действие игрока
        user_answer = input('Зачеркнуть цифру? (да/нет)\n').lower()

        # Проверяем не ошибся ли игрок. Если ошибся, он проигрывает
        if user_answer == 'да' and keg not in self.user_card.line or user_answer != 'да' and keg in self.user_card.line:
            return 3

        # Если в раунде ничья
        if keg in self.user_card.line and keg in self.computer_card.line:
            self.user_card.line = self.user_card.line.replace(keg, keg[0] + '̶' + keg[1] + '̶')
            self.computer_card.line = self.computer_card.line.replace(keg, keg[0] + '̶' + keg[1] + '̶')
            return 4

        # Если в раунде победил игрок
        if keg in self.user_card.line:
            self.user_card.line = self.user_card.line.replace(keg, keg[0] + '̶' + keg[1] + '̶')
            return 1

        # Если в раунде победил бот
        if keg in self.computer_card.line:
            self.computer_card.line = self.computer_card.line.replace(keg, keg[0] + '̶' + keg[1] + '̶')
            return 2

        # Если в раунде ничего не произошло
        return 0


# Наследованием создаем класс для игры компьютера против компьютера
class GameCompVsComp(Game):

    def __init__(self):
        Game.__init__(self)

    def play_round(self):

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


# Создал новый класс для игры человек против человека с возможностью выбора кол-ва участников
class PvPGame:
    # Лист для карт всех участников
    card_list = []

    # Лист с фишками
    kegs = list(range(1, 91))
    shuffle(kegs)

    def __init__(self, players):

        # Заполняем лист с картами в зависимости от кол-ва участников
        for i in range(players):
            player_card = Card()
            self.card_list.append(player_card)

    # Вывод карт в терминал
    def show_cards(self, players):

        for i in range(players):
            print(f'Карточка игрока {i + 1}:\n{self.card_list[i].line}\n')

    # Функция, проводящая один раунд игры
    def play_game(self, players):

        while True:

            # Вытягиваем фишку и выводим в терминал
            keg = str(self.kegs.pop())
            if len(str(keg)) < 2:
                keg = '0' + keg

            print(f'Новая фишка: {keg} (осталось {len(self.kegs)})\n')

            # Даем ход каждому игроку и проверяем ответы
            for i in range(players):
                # Спрашиваем ответ
                user_answer = input(f'Ход игрока {i + 1}. Зачеркнуть цифру? (да/нет)\n')
                # Проверяем ответ
                if user_answer == 'да' and keg not in self.card_list[i].line or user_answer != 'да' \
                        and keg in self.card_list[i].line:
                    # Если ответ неверный
                    return 'you_lost'

            # Зачеркиваем выбывшие цифры и создаем лист с номерами игроков, заработавших очки в этом раунде
            for i in range(players):
                if keg in self.card_list[i].line:
                    self.card_list[i].line = self.card_list[i].line.replace(keg, keg[0] + '̶' + keg[1] + '̶')

                    list_return = []

                    list_return.append(str(i + 1))

                    # Лист с номерами игроков, заработавших очки в этом раунде. Потом добавим им по одному очку.
                    return list_return
