from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        now = datetime.today()
        given_date = datetime.strptime(date, '%Y-%m-%d')
        return (now - given_date).days
    except ValueError:
        print("Помилка: некоректний формат дати. Використовуйте формат 'YYYY-MM-DD'")
        return None

print(get_days_from_today("2021-10-09"))
print(get_days_from_today("2025-10-13"))



    