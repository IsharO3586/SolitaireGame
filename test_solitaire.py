
import unittest
from solitaire_game import EnglishSolitaire

class TestSolitaireGame(unittest.TestCase):

    def setUp(self):
        self.game = EnglishSolitaire()

    def test_valid_move(self):
        result = self.game.make_move(3, 1, 3, 3)
        self.assertTrue(result)
        self.assertEqual(self.game.board[3][1], " ")
        self.assertEqual(self.game.board[3][2], " ")
        self.assertEqual(self.game.board[3][3], "●")

    def test_invalid_move(self):
        result = self.game.make_move(0, 2, 0, 4)
        self.assertFalse(result)

    
    #sprint 3: New test
    def test_game_over(self):
        game = EnglishSolitaire()
        game.board = [[" " for _ in range(7)] for _ in range(7)]
        self.assertTrue(game.is_game_over())

    def test_count_pegs(self):
        game = EnglishSolitaire()
        self.assertEqual(game.count_pegs(), 32)

if __name__ == "__main__":
    unittest.main()
