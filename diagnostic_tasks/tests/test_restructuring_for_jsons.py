from tasks_for_yandex_job.diagnostic_tasks.restructuring_for_jsons import (
    sort_nested_dictionaries
) 
import unittest


class TestSortNestedDictionaries(unittest.TestCase):
    def test_result_1(self):
        self.assertEqual(
            sort_nested_dictionaries([
                {"offer_id": "offer1", "market_sku": 10846332, "price": 1490}, 
                {"offer_id": "offer2", "market_sku": 682644, "price": 499},
                {"offer_id": "offer3", "market_sku": 832784, "price": 14000}
            ]),
            [
                {"offer_id": "offer2", "market_sku": 682644, "price": 499},
                {"offer_id": "offer1", "market_sku": 10846332, "price": 1490}, 
                {"offer_id": "offer3", "market_sku": 832784, "price": 14000}
            ]
        )


if __name__ == "__main__":
    unittest.main()