from collections import OrderedDict
from tasks_for_yandex_job.internship_tasks.if_i_knew_i_would_buy_it import (
    TradingDay, QuoteHistory
)
import unittest


class TestQuoteHistory(unittest.TestCase):
    def make_list_of_trading_days(self, closing_prices_of_each_day):
        list_of_trading_days = [
            TradingDay(day_position, int(closing_price_of_day))
            for day_position, closing_price_of_day in enumerate(
                closing_prices_of_each_day,
                start=1
            )
        ]
        return list_of_trading_days

    def test_of_result_1(self):
        quote_history = QuoteHistory(
            6, 
            self.make_list_of_trading_days([1, 4, 2, 3, 3, 5])
        )

        self.assertEqual(
            quote_history.search_for_best_trades(), 
            (
                2, 
                [
                    OrderedDict(open="1", close="2"), 
                    OrderedDict(open="3", close="6")
                ]
            )
        )

    def test_of_result_2(self):
        quote_history = QuoteHistory(
            5, 
            self.make_list_of_trading_days([10, 5, 5, 7, 6])
        )

        self.assertEqual(
            quote_history.search_for_best_trades(), 
            (1, [OrderedDict(open="2", close="4")])
        )

    def test_of_result_3(self):
        quote_history = QuoteHistory(
            3, 
            self.make_list_of_trading_days([3, 2, 2])
        )

        self.assertEqual(quote_history.search_for_best_trades(), (0, []))


if __name__ == "__main__":
    unittest.main()