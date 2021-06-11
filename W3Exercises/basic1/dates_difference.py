from datetime import date
date_one = date(2014, 7, 2)
date_two = date(2014, 7, 11)
difference = date_two - date_one
print(difference.days)