from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        for date in self.dates:
            start_date = date[0]
            end_date = date[1]
            while start_date <= end_date:
                yield start_date.strftime("%Y-%m-%d %H:%M:%S")
                start_date += timedelta(days=1)


m = Movie('sw', [(datetime(2020, 1, 1), datetime(2020, 1, 7)), (datetime(2020, 1, 15), datetime(2020, 2, 7))])

for d in m.schedule():
    print(d)
