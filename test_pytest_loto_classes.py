from loto_classes import Card, Game, GameCompVsComp, PvPGame


class TestLoto:

    def test_card(self):
        card = Card()
        assert card.values == 9
        assert card.lines == 3
        assert card.nums_in_line == 5
        assert card.empts_in_line == 4

    def test_game(self):
        game = Game()
        assert isinstance(game.user_card, Card)
        assert isinstance(game.computer_card, Card)
        assert len(game.kegs) == 90

    def test_game_comp_vs_comp(self):
        game = GameCompVsComp()
        assert isinstance(game.user_card, Card)
        assert isinstance(game.computer_card, Card)
        assert len(game.kegs) == 90

    def test_game_pvp(self):
        game = PvPGame(2)
        assert len(game.kegs) == 90
        assert len(game.card_list) == 2
