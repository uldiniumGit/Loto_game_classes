from loto_classes import Card, Game, GameCompVsComp, PvPGame


class TestLoto:

    def test_card(self):
        card = Card()
        assert card.values == 9, "Ожидается 9 значений на карте"
        assert card.lines == 3, "Ожидается 3 линии на карте"
        assert card.nums_in_line == 5, "Ожидается 5 чисел в линии"
        assert card.empts_in_line == 4, "Ожидается 4 пустых места в линии"

    def test__eq__(self):
        card1 = Card()
        card2 = Card()
        assert card1 == card2, "Карты должны быть равны"

    def test_game(self):
        game = Game()
        assert isinstance(game.user_card, Card), "user_card должен быть экземпляром Card"
        assert isinstance(game.computer_card, Card), "computer_card должен быть экземпляром Card"
        assert len(game.kegs) == 90, "Должно быть 90 кеглей"

    def test__eq__game(self):
        game1 = Game()
        game2 = Game()
        try:
            eq_result = (game1.user_card == game2.user_card) and (game1.computer_card == game2.computer_card)
        except Exception:
            assert False, "Сравнение карт вызвало исключение"
        else:
            assert eq_result, "Карты в играх должны быть равны"

    def test_game_comp_vs_comp(self):
        game = GameCompVsComp()
        assert isinstance(game.user_card, Card), "user_card должен быть экземпляром Card"
        assert isinstance(game.computer_card, Card), "computer_card должен быть экземпляром Card"
        assert len(game.kegs) == 90, "Должно быть 90 кеглей"

    def test_game_pvp(self):
        players_count = 2
        game = PvPGame(players_count)
        assert len(game.kegs) == 90, "Должно быть 90 кеглей"
        assert len(game.card_list) == players_count, f"Должно быть {players_count} карточек"

    def test_pvp__str__(self):
        players_count = 3
        game = PvPGame(players_count)
        assert str(game) == f'кол-во игроков: {players_count}', "Строковое представление не совпадает"

    def test_pvp__eq__(self):
        game1 = PvPGame(3)
        game2 = PvPGame(3)
        assert game1 == game2, "Игры PvP должны быть равны"
