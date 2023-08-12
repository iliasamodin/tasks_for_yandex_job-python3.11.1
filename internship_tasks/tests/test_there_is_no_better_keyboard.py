import unittest
from tasks_for_yandex_job.internship_tasks.there_is_no_better_keyboard import (
    number_of_transitions_by_rows_calculation
)


class TestNumberOfTransitionsByRowsCalculation(unittest.TestCase):
    def test_of_result_1(self):
        self.assertEqual(
            number_of_transitions_by_rows_calculation(
                [1, 2, 3, 4],
                [1, 2, 1, 2],
                [1, 2, 3, 1, 4]
            ),
            3
        )

    def test_of_result_2(self):
        self.assertEqual(
            number_of_transitions_by_rows_calculation(
                [42, 3, 14],
                [1, 3, 3],
                [3, 14, 14, 3]
            ),
            0
        )


if __name__ == "__main__":
    unittest.main()