from datetime import datetime

now = datetime.now()

print(now.strftime("%d-%m-%Y"))
print(now.strftime("%Y/%m/%d"))
print(now.strftime("%B %d, %Y"))
print(now.strftime("%d %b %Y"))
