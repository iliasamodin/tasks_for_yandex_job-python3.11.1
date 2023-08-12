from collections import OrderedDict


# Class whose objects are trading days
class TradingDay:
    def __init__(self, day_position, closing_price):
        self.position = day_position
        self.closing_price = closing_price

    def __lt__(self, other):
        return self.closing_price < other.closing_price

    def __truediv__(self, other):
        return self.closing_price / other.closing_price

    def __str__(self):
        return str(self.position)


# The class of the history of asset quote in a limited period of time
class QuoteHistory:
    def __init__(self, amount_of_days, list_of_trading_days):
        self.amount_of_days = amount_of_days
        self.list_of_trading_days = list_of_trading_days

    # Method for finding the two most profitable long trades 
    #   in the historical time frame
    def search_for_best_trades(self):
        profitable_trades = self.__finding_best_trade(
            0, self.amount_of_days
        )

        # If profitable long trades are found 
        #   on the historical time period, 
        #   then the two most profitable trades 
        #   are selected among these trades
        if profitable_trades:
            profitable_trades.sort(key=lambda trade: trade[2])
            profitable_trades = [
                OrderedDict(open=str(opening_day), close=str(closing_day))
                for opening_day, closing_day, _ in profitable_trades
            ]

            if len(profitable_trades) >= 2:
                profitable_trades = profitable_trades[-2:]
                profitable_trades.sort(key=lambda trade: int(trade["open"]))

                # If a short trade is found inside 
                #   the most profitable long trade, 
                #   the profitability of which is in second place 
                #   among all found trades, 
                #   then the most profitable long trade is divided 
                #   into two long trades, 
                #   the total profit of which exceeds 
                #   the profit of the undivided trade
                if int(profitable_trades[1]["open"]) > \
                int(profitable_trades[1]["close"]):
                    (
                        profitable_trades[0]["close"], 
                        profitable_trades[1]["close"]
                    ) = (
                        profitable_trades[1]["close"], 
                        profitable_trades[0]["close"]
                    )

            amount_of_trades = len(profitable_trades)

        else:
            amount_of_trades = 0

        return amount_of_trades, profitable_trades

    # A method that calls the calculation of the most profitable trade 
    #   for slices from the original historical time period, 
    #   and then combines profitable trades into a list
    def __finding_best_trade(self, start_index, end_index, step=1):
        profitable_trades = []

        history_slice_stack = [(start_index, end_index, step)]
        while history_slice_stack:
            start_index, end_index, step = history_slice_stack.pop()

            if start_index == end_index or \
            start_index < 0 or end_index > self.amount_of_days:
                continue

            smallest_price, highest_price = \
                self.calculation_smallest_and_highest_prices(
                    start_index, end_index, step
                )
            if smallest_price is not highest_price:
                profitable_trade = highest_price / smallest_price
                profitable_trades.append((
                    smallest_price,
                    highest_price,
                    profitable_trade
                ))

                # If the most profitable long trade 
                #   for the entire historical period of time is found, 
                #   then the search for less profitable trades 
                #   is performed before, within and after 
                #   the most profitable long trade
                if len(profitable_trades) == 1:
                    history_slice_stack.append((
                        start_index, smallest_price.position-1, 1
                    ))
                    history_slice_stack.append((
                        highest_price.position-1, 
                        smallest_price.position-1, 
                        -1
                    ))
                    history_slice_stack.append((
                        highest_price.position, end_index, 1
                    ))

        return profitable_trades

    # Method for calculating one most profitable trade 
    #   on a slice of a historical time period
    def calculation_smallest_and_highest_prices(
            self, 
            start_index, end_index, step=1
        ):

        smallest_price = highest_price = temporary_floor_price = \
            self.list_of_trading_days[start_index]

        for idx in range(start_index, end_index, step):
            if self.list_of_trading_days[idx] < temporary_floor_price:
                temporary_floor_price = self.list_of_trading_days[idx]
            elif self.list_of_trading_days[idx] / temporary_floor_price > \
            highest_price / smallest_price:
                smallest_price = temporary_floor_price
                highest_price = self.list_of_trading_days[idx]

        return smallest_price, highest_price


if __name__ == "__main__":
    with open("input.txt") as input_file:
        amount_of_days, closing_prices_of_each_day = input_file.readlines()

    amount_of_days = int(amount_of_days.strip())
    list_of_trading_days = [
        TradingDay(day_position, int(closing_price_of_day))
        for day_position, closing_price_of_day in enumerate(
            closing_prices_of_each_day.strip().split(" "),
            start=1
        )
    ]

    quote_history = QuoteHistory(amount_of_days, list_of_trading_days)
    amount_of_trades, profitable_trades = \
        quote_history.search_for_best_trades()
    profitable_trades = "\n".join(
        [" ".join(trade.values()) for trade in profitable_trades]
    )

    with open("output.txt", "w") as output_file:
        print(amount_of_trades, file=output_file)
        if profitable_trades:
            print(profitable_trades, file=output_file)