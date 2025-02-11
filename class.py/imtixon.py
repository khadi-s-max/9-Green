import datetime

# Bugungi sana
today = datetime.date.today()

# Hafta kunini olish (1: Dushanba, 7: Yakshanba)
day_of_week = today.weekday() + 1  # Python'da Monday=0, Sunday=6, shuning uchun +1 qo'shamiz

day_of_week
