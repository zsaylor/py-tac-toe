import unittest
import sys
import collections
from unittest import mock
from unittest.mock import patch

sys.path.insert(0, '/Users/temporaryadmin/PycharmProjects/100-days-of-code/83-TicTacToe')

from pytactoe import game, board

Player = collections.namedtuple('Player', ["name", "symbol"])


class TestBoard(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestBoard, self).__init__(*args, **kwargs)
        self.board = board.Board()
        self.p1 = Player("Player One", "X")
        self.p2 = Player("Player Two", "O")
        self.game = game.Game(self.board, self.p1, self.p2)

    def test_turn(self):
        """
        Test that method can successfully place player's symbol in empty slot.
        """

        # ARRANGE
        self.game.choose_coords = mock.MagicMock(return_value=None)
        self.game.choice_row = 1
        self.game.choice_column = 1

        # ACT
        self.game.turn(self.p1)
        result = self.game.game_board.board[0][0]

        # ASSERT
        self.assertEqual(result, "X")

    def test_check_win(self):
        """
        Test that method can detect a 'win' (i.e. 3 consecutive player symbols in a row).
        """

        # ARRANGE
        self.game.game_board.board[0][0] = "X"
        self.game.game_board.board[0][1] = "X"
        self.game.game_board.board[0][2] = "X"

        # ACT
        result = self.game.check_win()

        # ASSERT
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
