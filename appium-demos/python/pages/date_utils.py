import locale
from datetime import date, timedelta


def get_next_day_labels(days: int = 9, fmt: str = "%d %B") -> list[str]:
    locale.setlocale(locale.LC_TIME, "en_GB.UTF-8")
    today = date.today()
    # %d: day of the month as a zero-padded decimal number
    # %B: month as locale's full name

    # %Y: year with century as a decimal number
    # %m: month as a zero-padded decimal number
    # %d: day of the month as a zero-padded decimal number
    return [(today + timedelta(days=i + 1)).strftime(fmt) for i in range(days)]


if __name__ == "__main__":
    print(get_next_day_labels())
    print(get_next_day_labels(fmt="%Y%m%d"))
