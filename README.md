

<h3 align="center">📅 B3Cal</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/joseparreiras/b3cal.svg)](https://github.com/joseparreiras/b3cal/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/joseparreiras/b3cal.svg)](https://github.com/joseparreiras/b3cal/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> A package for Brazilian financial market calendar and holidays. 
<br>
</p>

## 📝 Table of Contents

- [About](#about)
- [Installation](#install)
- [Documentation](#doc)
- [Usage](#usage)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

This package provides a similar interface to the `pandas-market-calendar` module. It provides information on the Brazilian financial market calendar and holidays.

## 🚀 Installation <a name = "install"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

The required packages are listed in the `requirements.txt` file. You can install them from `pip`. To do this, first clone the repository and then run the following command in the terminal:

```bash
cd /path/to/repository
pip install -r requirements.txt
```

Likewise, these packages will be installed automatically when you install the package using `pip`.

### Installing

To install the package, you can use `pip`.

```bash
pip install git+https://github.com/joseparreiras/b3cal
```

## 🔧 Documentation <a name = "doc"></a>

The main class provided in this module is the `Calendar` class. You can import it using

```python
from b3cal import Calendar as b3cal
```

Calling it gives you the list of holidays in the Brazilian financial market since 2001.

This class contains the following methods:

### `is_holiday`

```python
is_holiday(date: date | str) -> bool
```

Check if a date is a holiday.

Parameters:

- `date`: The date to be checked. It can be a `date` object or a string in the format `YYYY-MM-DD` or another format accepted by `pandas.to_datetime`.

Returns:

- `bool`: `True` if the date is a holiday, `False` otherwise.

### `next_holiday`

```python
next_holiday(date: date | str, n: int = 1) -> pandas.DatetimeIndex
```

Get the next `n` holidays after a given date.

Parameters:

- `date`: The date to start the search. It can be a `date` object or a string in the format `YYYY-MM-DD` or another format accepted by `pandas.to_datetime`.
- `n`: The number of holidays to be returned. Default is `1`.

Returns:

- `pandas.DatetimeIndex`: A `pandas.DatetimeIndex` object with the dates of the next `n` holidays.

### `previous_holiday`

```python
previous_holiday(date: date | str, n: int = 1) -> pandas.DatetimeIndex
```

Get the previous `n` holidays before a given date.

Parameters:

- `date`: The date to start the search. It can be a `date` object or a string in the format `YYYY-MM-DD` or another format accepted by `pandas.to_datetime`.
- `n`: The number of holidays to be returned. Default is `1`.

Returns:

- `pandas.DatetimeIndex`: A `pandas.DatetimeIndex` object with the dates of the previous `n` holidays.

### `in_range`

```python
in_range(start: date | str, end: date | str) -> pandas.DatetimeIndex
```

Get the holidays between two dates.

Parameters:

- `start`: The start date. It can be a `date` object or a string in the format `YYYY-MM-DD` or another format accepted by `pandas.to_datetime`.
- `end`: The end date. It can be a `date` object or a string in the format `YYYY-MM-DD` or another format accepted by `pandas.to_datetime`.

Returns:

- `pandas.DatetimeIndex`: A `pandas.DatetimeIndex` object with the dates of the holidays between the two dates.

### `bdate_range`

```python
bdate_range(start: date | str, end: date | str = None, periods: int | None = None, **kwargs) -> pandas.DatetimeIndex
```

Creates a range of market dates between a start and end date or a number of periods.

Parameters:

- `start`: The start date. It can be a `date` object or a string in the format `YYYY-MM-DD` or another format accepted by `pandas.to_datetime`.
- `end`: The end date. It can be a `date` object or a string in the format `YYYY-MM-DD` or another format accepted by `pandas.to_datetime`. If `None`, the `periods` parameter must be set.
- `periods`: The number of periods to generate. If `None`, the `end` parameter must be set.
- `**kwargs`: Additional arguments to be passed to the `pandas.date_range` function (if `end` is specified) or the `pandas.DatetimeIndex` function (if `periods` is specified).

Returns:

- `pandas.DatetimeIndex`: A `pandas.DatetimeIndex` object with the market dates between the two dates or the number of periods.

### `bdate_count`

```python
bdate_count(start: date | str, end: date | str) -> int
```

Provides the number of business days (excluding holidays) between two dates.


Parameters:

- `start`: The start date. It can be a `date` object or a string in the format `YYYY-MM-DD` or another format accepted by `pandas.to_datetime`.
- `end`: The end date. It can be a `date` object or a string in the format `YYYY-MM-DD` or another format accepted by `pandas.to_datetime`.

Returns:
- `int`: The number of business days between the two dates.

## 🎈 Usage <a name="usage"></a>

Input dates will only be filtered after `2001-01-01`. Using dates prior to this will assume no holidays before the start of the series.

## ✍️ Authors <a name = "authors"></a>

- [@joseparreiras](https://github.com/joseparreiras) - Idea & Initial work

## 🎉 References <a name = "acknowledgement"></a>

- `pandas_market_calendars` module available [here](https://pypi.org/project/pandas-market-calendars/)
- Holidays source: [ANBIMA](https://www.anbima.com.br/feriados/)