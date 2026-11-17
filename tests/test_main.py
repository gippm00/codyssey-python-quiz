import unittest
from unittest.mock import patch

from main import Quiz, QuizGame


class QuizTest(unittest.TestCase):
    def test_correct_answer(self):
        quiz = Quiz("질문", ["1", "2", "3", "4"], 2)
        self.assertTrue(quiz.is_correct(2))
        self.assertFalse(quiz.is_correct(1))

    def test_default_quizzes_have_at_least_five_items(self):
        self.assertGreaterEqual(len(QuizGame.default_quizzes()), 5)

    def test_invalid_quiz_data_is_rejected(self):
        with self.assertRaises(ValueError):
            Quiz.from_dict({"question": "질문", "choices": ["1", "2"], "answer": 1})


class InputTest(unittest.TestCase):
    def test_read_int_retries_invalid_empty_and_out_of_range_values(self):
        with patch("builtins.input", side_effect=["abc", "", "0", " 2 "]):
            result = QuizGame.read_int("답: ", 1, 4)
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
