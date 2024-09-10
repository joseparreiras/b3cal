import pkg_resources
import pandas as pd
from datetime import date
from warnings import warn
from pandas.tseries.offsets import BDay

__version__ = "0.1.0"

class Calendar:
    def __init__(self):
        """
        Class to handle Brazilian market calendar. The data source is available in the `tools/holidays.csv` file which contains financial market holidays since 2001.
        """
        stream = pkg_resources.resource_stream(__name__, 'data/holidays.csv')
        self.holidays = pd.read_csv(stream)
        self.holidays = pd.to_datetime(self.holidays["Data"].values)
        self.holidays = self.holidays.sort_values(ascending=True)  # Sort

    def __str__(self):
        return str(self.holidays)

    def __iter__(self):
        return iter(self.holidays)

    def __available__(self, date: date):
        """
        Check if date is within the available range of holidays.

        Args:
            date (date): Date to check
        """
        if date <= self.holidays.min() or date >= self.holidays.max():
            warn("Date is out of range of available holidays")

    def is_holiday(self, date: date | list) -> list | bool:
        """
        Checks whether a given date is a market holiday.

        Args:
            date (date | list): A date or an iterable of dates to check

        Returns:
            bool | list: True if date is a holiday. If an iterable is provided, returns a list of booleans.
        """
        # If date is a string, convert to datetime
        if isinstance(date, str):
            date = pd.to_datetime(date)
        self.__available__(date)  # Check if available
        try:
            loop = iter(date)  # Check if date is iterable
            result = [x in self.holidays for x in loop]
            return result
        except TypeError:
            return date in self.holidays

    def next_holiday(self, date: date | str, n: int = 1) -> pd.DatetimeIndex:
        """
        Gets the next `n` holidays after a given date.

        Args:
            date (date | str): Start date to search for holidays
            n (int, optional): Number of holidays to return. Defaults to 1.

        Returns:
            pd.DatetimeIndex: Index with the next holidays.
        """
        # If date is a string, convert to datetime
        if isinstance(date, str):
            date = pd.to_datetime(date)
        self.__available__(date)  # Check if available
        return self.holidays[self.holidays > date][:n]

    def previous_holiday(self, date: date | str, n: int = 1) -> pd.DatetimeIndex:
        """
        Gets the previous `n` holidays before a given date.

        Args:
            date (date | str): Start date to search for holidays
            n (int, optional): Number of holidays to return. Defaults to 1.

        Returns:
            pd.DatetimeIndex: Index with the previous holidays.
        """
        # If date is a string, convert to datetime
        if isinstance(date, str):
            date = pd.to_datetime(date)
        self.__available__(date)  # Check if available
        return self.holidays[self.holidays < date][-n:]

    def in_range(self, start: date | str, end: date | str) -> pd.DatetimeIndex:
        """
        Gets the holidays between a given range.

        Args:
            start (date | str): Start date of the range
            end (date | str): End date of the range

        Returns:
            pd.DatetimeIndex: Index with the holidays between the range.
        """
        # If start date is a string, convert to datetime
        if isinstance(start, str):
            start = pd.to_datetime(start)
        self.__available__(start)  # Check if available
        # If end date is a string, convert to datetime
        if isinstance(end, str):
            end = pd.to_datetime(end)
        self.__available__(end)  # Check if available
        return self.holidays[(self.holidays >= start) & (self.holidays <= end)]

    def bdate_range(
        self,
        start: date | str,
        end: date | str | None = None,
        periods: int | None = None,
        **kwargs
    ) -> pd.DatetimeIndex:
        """
        Creates a range of market dates between a start and end date or a number of periods.

        Args:
            start (date | str): Start date of the range
            end (date | str | None, optional): End date of the range.
            periods (int | None, optional): Number of periods of the range.
            **kwargs: Additional arguments for `pd.bdate_range` (if `end` is provided) or `pd.DatetimeIndex` (id `periods` is provided).

        Raises:
            ValueError: Either `end` or `periods` must be provided.

        Returns:
            pd.DatetimeIndex: Index with the market dates
        """
        # If start date is a string, convert to datetime
        if isinstance(start, str):
            start = pd.to_datetime(start)
        self.__available__(start)  # Check if available
        if end is not None:
            # If end date is provided as a string, convert to datetime
            if isinstance(end, str):
                end = pd.to_datetime(end)
            self.__available__(end)  # Check if available

        if periods is None and end is not None:
            # If `end` is provided, run a pd.bdate_range
            full_range = pd.bdate_range(start=start, end=end, periods=None, **kwargs)
            # Remove the holidays from the database
            return full_range[[not self.is_holiday(x) for x in full_range]]
        elif periods is not None and end is None:
            # If `periods` is provided
            index = []  # Start with an empty list
            date = start  # Start date
            # Iterate until get exact number of periods
            while len(index) < periods:
                # Check if date is not a holiday, if not, append to the list
                if not self.is_holiday(date):
                    index.append(date)
                date += BDay(1)  # Move to the next business date
            return pd.DatetimeIndex(index, **kwargs)
        else:
            raise ValueError("Either end or periods must be provided")

    def bdate_count(self, start: date | str, end: date | str) -> int:
        """
        Provides the number of business days (excluding holidays) between two dates.

        Args:
            start (date | str): Start date
            end (date | str): End date

        Returns:
            int: Number of business days
        """
        return len(self.bdate_range(start, end))
