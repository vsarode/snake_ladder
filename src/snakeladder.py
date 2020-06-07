from src.board import Board
from src.dice import NormalDice
from src.exceptions import GameOverException
from src.player import Player


class SnakeLadder:
    def __init__(self, player, board, turns):
        self.player = player
        self.board = board
        self.turns = turns

    def play(self):
        for _ in range(self.turns):
            try:
                value_on_dice = self.player.play_turn()
                self.board.move(self.player, value_on_dice)
                print(
                    f'Player {self.player.name} position: {self.player.position}')
            except GameOverException:
                print(
                    f'Player {self.player.name} position: {self.player.position}')
                break
        print(f'Game over !! As turns are over.')


if __name__ == '__main__':
    dice = NormalDice()
    player = Player('Ram', dice)
    snakes = {4: 2}
    board = Board(snakes)
    game = SnakeLadder(player, board, 10)
    game.play()
