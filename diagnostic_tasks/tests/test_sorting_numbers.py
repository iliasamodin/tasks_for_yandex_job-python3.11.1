from tasks_for_yandex_job.diagnostic_tasks.sorting_numbers import (
    get_integers_from_server
)
import unittest


# Be sure to run server_for_test_sorting_numbers.py 
#   on a dedicated terminal before running unittest
class TestGetIntegersFromServer(unittest.TestCase):
    def test_result_1(self):
        self.assertEqual(
            get_integers_from_server("http://127.0.0.1", "7777", "2", "4"),
            [-19, -17, -2, 2, 4, 6, 8, 17, 256, 1024]
        )


if __name__ == "__main__":
    unittest.main()