from tasks_for_yandex_job.internship_tasks.perfectionism_is_problem import (
    sculptures_completion_calculation
)
import unittest


class TestSculpturesCompletionCalculation(unittest.TestCase):
    def test_of_result_1(self):
        self.assertEqual(
            sculptures_completion_calculation(
                5, 2,
                [5, 10, 6]
            ),
            (2, ["1", "3"])
        )

    def test_of_result_2(self):
        self.assertEqual(
            sculptures_completion_calculation(
                19, 32,
                [36, 10, 72, 4, 50]
            ),
            (2, ["2", "4"])
        )

    def test_of_result_3(self):
        self.assertEqual(
            sculptures_completion_calculation(
                25, 10,
                [1, 10, 42, 9]
            ),
            (0, [])
        )


if __name__ == "__main__":
    unittest.main()