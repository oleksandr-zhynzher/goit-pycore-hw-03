from datetime import datetime

def get_days_from_today(date: str) -> int:
    now = datetime.today()
    given_date = datetime.strptime(date, '%Y-%m-%d')
    return (now - given_date).days

print(get_days_from_today("2021-10-09"))
print(get_days_from_today("2025-10-13"))



    