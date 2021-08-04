from datetime import datetime
from collections import defaultdict

days = [('2021, 08 04', '1 '), ('26 08, 2021', '6 '), ('19 08, 2021', '4 '),('20 08, 2021', '2')]

totals = defaultdict(int)
for date_str, value_str in days:
    totals[datetime.strptime(date_str, "%Y, %m %d").strftime("%A")] += int(value_str)

print(totals)