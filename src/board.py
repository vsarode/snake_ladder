import time

from src.exceptions import GameOverException


class Board:
    def __init__(self, snakes):
        self.snakes = snakes
        self.start = 0
        self.end = 100

    def move(self, player, value_on_dice):
        next_value = player.position + value_on_dice
        if self.snakes.get(next_value):
            print(
                f'Snack bites to player {player.name} with start position: {next_value} to {self.snakes.get(next_value)}')
            time.sleep(2)
            player.position = self.snakes.get(next_value)
        else:
            player.position = next_value
        if player.position >= self.end:
            print(f'Game won by {player.name}')
            raise GameOverException
