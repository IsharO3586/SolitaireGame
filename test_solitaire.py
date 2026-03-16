import unittest
from solitaire_game import SolitaireGame

class TestSolitaireGame(unittest.TestCase):

    def setUp(self):
        self.game = SolitaireGame()

    def test_valid_move(self):
        result = self.game.make_move(3, 1, 3, 3)
        self.assertTrue(result)
        self.assertEqual(self.game.board[3][1], " ")
        self.assertEqual(self.game.board[3][2], " ")
        self.assertEqual(self.game.board[3][3], "●")

    def test_invalid_move(self):
        result = self.game.make_move(0, 2, 0, 4)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()