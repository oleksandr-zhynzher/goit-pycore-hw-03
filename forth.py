from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        days_until_birthday = (birthday_this_year - today).days
        
        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year

            weekday = congratulation_date.weekday()
            if weekday == 5:  
                congratulation_date += timedelta(days=2)  
            elif weekday == 6:  
                congratulation_date += timedelta(days=1)  
            
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.10.18"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

print(get_upcoming_birthdays(users))