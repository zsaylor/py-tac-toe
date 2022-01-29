import unittest
import sys

sys.path.insert(0, '/Users/temporaryadmin/PycharmProjects/100-days-of-code/83-TicTacToe')

from pytactoe import board


class TestBoard(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestBoard, self).__init__(*args, **kwargs)
        self.board = board.Board()

    def test1_insert_symbol(self):
        """
        Test that method can insert a new symbol into the board.
        """

        # ARRANGE
        symbol = "X"
        tile_coords = (1, 1)

        # ACT
        result = self.board.insert_symbol(symbol, tile_coords)

        # ASSERT
        self.assertEqual(result, True)

    def test2_clear_board(self):
        """
        Test that method can erase all symbols from board
        """

        # ARRANGE
        # Nothing to arrange...

        # ACT
        result = self.board.clear_board()

        # ASSERT
        self.assertEqual(result, True)

    def test3_check_full_board(self):
        """
        Test that method can determine if the board is full or not.
        """

        # ARRANGE
        self.board.board = [["X"] * 3 for i in range(3)]
        print(self.board)

        # ACT
        result = self.board.check_full_board()

        # ASSERT
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
