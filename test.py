from datetime import datetime
from collections import defaultdict

days = [('04 08, 2021', '1 '), ('26 08, 2021', '6 '), ('19 08, 2021', '4 '),('20 08, 2021', '2')]

totals = defaultdict(int)
for date_str, value_str in days:
    totals[datetime.strptime(date_str, "%d %m, %Y").strftime("%A")] += int(value_str)

print(totals)