import unittest

from src.board import Board
from src.dice import NormalDice
from src.exceptions import GameOverException
from src.player import Player


class TestGameBoard(unittest.TestCase):

    def setUp(self) -> None:
        self.__dice = NormalDice()
        self.__player = Player('Ram', self.__dice)
        self.__snakes = {5: 2}
        self.__board = Board(self.__snakes)

    def test_move_changes_player_position(self):
        previous_position = self.__player.position
        next_position = self.__player.play_turn()
        self.__board.move(self.__player, next_position)
        assert self.__player.position != previous_position

    def test_move_raise_game_over_exception_for_the_position_more_than_100(
            self):
        self.__player.position = 99
        next_position = self.__player.play_turn()
        self.assertRaises(GameOverException,
                          lambda: self.__board.move(self.__player,
                                                    next_position))


if __name__ == '__main__':
    unittest.main()
