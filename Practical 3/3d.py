from datetime import datetime

timestamp = 1721126400
date = datetime.fromtimestamp(timestamp)

print(date.strftime("%Y-%m-%d"))
