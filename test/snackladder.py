import unittest
from unittest.mock import MagicMock

from src.board import Board
from src.dice import NormalDice
from src.player import Player
from src.snakeladder import SnakeLadder


class TestPlayer(unittest.TestCase):

    def setUp(self) -> None:
        self.__dice = NormalDice()
        self.__player = Player('Ram', self.__dice)
        self.__snakes = {5: 2}
        self.__board = Board(self.__snakes)
        self.__snake_ladder = SnakeLadder(self.__player, self.__board, 1)

    def test_play_calls_play_turn(self):
        self.__player.play_turn = MagicMock(return_value=2)
        self.__snake_ladder.play()
        self.__player.play_turn.assert_called_with()


if __name__ == '__main__':
    unittest.main()
