import re

def normalize_phone(phone_number):
    cleaned_number = re.sub(r'[^\d+]', '', phone_number)
    
    # Якщо номер починається з '+380', залишаємо як є
    if cleaned_number.startswith('+380'):
        return cleaned_number
    
    # Якщо номер починається з '380', додаємо '+'
    elif cleaned_number.startswith('380'):
        return '+' + cleaned_number
    
    # Якщо номер починається з '+38', але не '+380', 
    # видаляємо '+38' і додаємо '+380'
    elif cleaned_number.startswith('+38'):
        return '+380' + cleaned_number[3:]
    
    # Якщо номер починається з '38', але не '380',
    # видаляємо '38' і додаємо '+380'
    elif cleaned_number.startswith('38'):
        return '+380' + cleaned_number[2:]
    
    # Якщо номер починається з '0' (локальний формат),
    # видаляємо '0' і додаємо '+380'
    elif cleaned_number.startswith('0'):
        return '+380' + cleaned_number[1:]
    
    # Для всіх інших випадків додаємо '+380'
    else:
        return '+380' + cleaned_number



raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)