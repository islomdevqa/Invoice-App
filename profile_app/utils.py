import random

available_numbers = [x for x in range(10)]
size = 12

def generate_account_number():
    new_number_list = [str(random.choice(available_numbers)) for _ in range(size)]