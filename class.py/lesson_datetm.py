"""tashqi kutubxonalar"""
# datetime.datetime
import datetime
hozir=datetime.datetime.now()
print(hozir.year)
print(hozir.month)
print(hozir.weekday())
print(hozir.day)
print(hozir.hour)
print(hozir.minute)
print(hozir.second)
print(hozir.microsecond)


print(hozir.date())

# datetime.timedelta
print(hozir.strftime("%Y-%m-%d"))
print(hozir.strftime("%z"))
print(hozir.strftime("%h"))
# sanadan sanani ayirish

from datetime import timedelta
oyluk_turi=timedelta(days=30)
print(hozir+oyluk_turi)
print(hozir-oyluk_turi)

bugun=datetime.datetime.today()
ramazon=datetime.date(2025,3.1)

print(ramazon-bugun)


