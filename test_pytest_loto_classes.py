from loto_classes import Card, Game, GameCompVsComp, PvPGame


class TestLoto:

    def test_card(self):
        card = Card()
        assert card.values == 9
        assert card.lines == 3
        assert card.nums_in_line == 5
        assert card.empts_in_line == 4

    def test__eq__(self):
        card = Card()
        card_02 = Card
        assert card == card_02

    def test_game(self):
        game = Game()
        assert isinstance(game.user_card, Card)
        assert isinstance(game.computer_card, Card)
        assert len(game.kegs) == 90

    def test__eq__game(self):
        game = Game()
        game_02 = Game()
        try:
            game.user_card == game_02.user_card and game.computer_card == game_02.computer_card
        except:
            assert False
        else:
            assert True

    def test_game_comp_vs_comp(self):
        game = GameCompVsComp()
        assert isinstance(game.user_card, Card)
        assert isinstance(game.computer_card, Card)
        assert len(game.kegs) == 90

    def test_game_pvp(self):
        game = PvPGame(2)
        assert len(game.kegs) == 90
        assert len(game.card_list) == 2

    def test_pvp__str__(self):
        game_01 = PvPGame(3)
        assert game_01.__str__() == 'кол-во игроков: 3'

    def test_pvp__eq__(self):
        game = PvPGame(3)
        game_02 = PvPGame(3)
        assert game == game_02
