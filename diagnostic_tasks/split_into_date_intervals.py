from datetime import datetime, timedelta


# Class whose objects are date intervals
class DateInterval:
    def __init__(self, original_date_interval):
        self.start_of_interval = original_date_interval[0]
        self.end_of_interval = original_date_interval[1]

    # A method that divides the original date interval 
    #   into subintervals 
    #   according to the type of expected subintervals
    def split_into_date_intervals(self, subinterval_type):
        divided_date_intervals = []
        start_of_subinterval = self.start_of_interval
        end_of_subinterval = self.start_of_interval

        if subinterval_type == "WEEK":
            while True:
                day_of_the_week = start_of_subinterval.weekday()
                end_of_subinterval = start_of_subinterval + \
                    timedelta(days=6-day_of_the_week)

                start_of_subinterval = self._add_subinterval(
                    divided_date_intervals, 
                    start_of_subinterval,
                    end_of_subinterval
                )
                if start_of_subinterval is None:
                    break

        elif subinterval_type == "MONTH":
            while True:
                intermediate_date = start_of_subinterval + \
                    timedelta(days=32-start_of_subinterval.day)
                end_of_subinterval = \
                    intermediate_date - timedelta(days=intermediate_date.day)

                start_of_subinterval = self._add_subinterval(
                    divided_date_intervals, 
                    start_of_subinterval,
                    end_of_subinterval
                )
                if start_of_subinterval is None:
                    break

        elif subinterval_type == "QUARTER":
            while True:
                month_of_subinterval_start = \
                    start_of_subinterval.strftime("%b")
                if month_of_subinterval_start in {"Jan", "Feb", "Mar"}:
                    end_of_subinterval = start_of_subinterval.replace(
                        month=3,
                        day=31
                    )
                elif month_of_subinterval_start in {"Apr", "May", "Jun"}:
                    end_of_subinterval = start_of_subinterval.replace(
                        month=6,
                        day=30
                    )
                elif month_of_subinterval_start in {"Jul", "Aug", "Sep"}:
                    end_of_subinterval = start_of_subinterval.replace(
                        month=9,
                        day=30
                    )
                else:
                    end_of_subinterval = start_of_subinterval.replace(
                        month=12,
                        day=31
                    )

                start_of_subinterval = self._add_subinterval(
                    divided_date_intervals, 
                    start_of_subinterval,
                    end_of_subinterval
                )
                if start_of_subinterval is None:
                    break

        elif subinterval_type == "YEAR":
            while True:
                end_of_subinterval = start_of_subinterval.replace(
                    month=12,
                    day=31
                )

                start_of_subinterval = self._add_subinterval(
                    divided_date_intervals, 
                    start_of_subinterval,
                    end_of_subinterval
                )
                if start_of_subinterval is None:
                    break

        # The condition block for dividing the initial date interval 
        #   into subintervals - the periods 
        #   for which the achievements of Yandex employees are evaluated
        elif subinterval_type == "REVIEW":
            while True:
                month_of_subinterval_start = \
                    start_of_subinterval.strftime("%b")
                if month_of_subinterval_start in {
                    "Apr", "May", "Jun", "Jul", "Aug", "Sep"
                }:
                    end_of_subinterval = start_of_subinterval.replace(
                        month=9,
                        day=30
                    )
                elif month_of_subinterval_start in {"Oct", "Nov", "Dec"}:
                    end_of_subinterval = start_of_subinterval.replace(
                        year=start_of_subinterval.year+1,
                        month=3,
                        day=31
                    )
                else:
                    end_of_subinterval = start_of_subinterval.replace(
                        month=3,
                        day=31
                    )

                start_of_subinterval = self._add_subinterval(
                    divided_date_intervals, 
                    start_of_subinterval,
                    end_of_subinterval
                )
                if start_of_subinterval is None:
                    break

        return len(divided_date_intervals), divided_date_intervals

    # Method for adding a subinterval 
    #   to the resulting list of subintervals of a given type
    def _add_subinterval(
        self,
        divided_date_intervals, 
        start_of_subinterval,
        end_of_subinterval
    ):

        if end_of_subinterval < self.end_of_interval:
            divided_date_intervals.append(
                (
                    start_of_subinterval.strftime("%Y-%m-%d"), 
                    end_of_subinterval.strftime("%Y-%m-%d")
                )
            )
            start_of_subinterval = end_of_subinterval + timedelta(days=1)
        # If the calculated end date of the subinterval 
        #   in the chronology is later than the end date 
        #   of the original interval, 
        #   then the end date of the current subinterval is replaced 
        #   by the end date of the original interval 
        #   and the search for subintervals ends
        else:
            divided_date_intervals.append(
                (
                    start_of_subinterval.strftime("%Y-%m-%d"), 
                    self.end_of_interval.strftime("%Y-%m-%d")
                )
            )
            start_of_subinterval = None

        return start_of_subinterval


if __name__ == "__main__":
    with open("input.txt") as input_file:
        subinterval_type, original_date_interval = input_file.readlines()

    subinterval_type = subinterval_type.strip()
    original_date_interval = [
        datetime.strptime(date.strip(), "%Y-%m-%d")
        for date in original_date_interval.strip().split()
    ]

    date_interval = DateInterval(original_date_interval)
    number_of_subinterval, divided_date_intervals = \
        date_interval.split_into_date_intervals(subinterval_type)
    divided_date_intervals = "\n".join(
        [" ".join(subinterval) for subinterval in divided_date_intervals]
    )

    with open("output.txt", "w") as output_file:
        print(
            number_of_subinterval,
            divided_date_intervals,
            sep="\n",
            file=output_file
        )