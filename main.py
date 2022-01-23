import collections
from board import Board
from game import Game
import itertools

Player = collections.namedtuple('Player', ["name", "symbol", "score"])


def main():
    print("Tic Tac Toe!")
    player_one_name = str(input("Player One, enter your name:\n"))
    player_two_name = str(input("Player Two, enter your name:\n"))
    player_one = Player(player_one_name, "X", 0)
    player_two = Player(player_two_name, "O", 0)
    players = [player_one, player_two]

    board = Board()

    new_game = Game(board, player_one, player_two)

    for player in itertools.cycle(players):
        new_game.turn(player)
        if new_game.check_win():
            print(f"{player.name} won!")
            break


main()
