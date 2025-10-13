import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if min < 1 or max > 1000 or min >= max or quantity <= 0:
        return []
    
    available_numbers = max - min + 1
    if quantity > available_numbers:
        return []
    
    numbers = random.sample(range(min, max + 1), quantity)
    
    return sorted(numbers)

print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(1, 5, 10))  
print(get_numbers_ticket(10, 5, 3))  
print(get_numbers_ticket(1, 3, 3))  
    