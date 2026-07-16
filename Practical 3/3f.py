from datetime import datetime

date1 = datetime.strptime("16-07-2026", "%d-%m-%Y")
date2 = datetime.strptime("20-07-2026", "%d-%m-%Y")

if date1 > date2:
    print("Date1 is later")
elif date1 < date2:
    print("Date2 is later")
else:
    print("Both dates are equal")
