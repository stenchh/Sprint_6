import random


russian_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' + 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
def generate_phone_number():
    return ''.join(random.choices('0123456789', k=11))

def generate_name_or_surname():
    random_name_or_surname = ''.join(random.choices(russian_letters, k=6))
    return random_name_or_surname

def generate_address():
    return ''.join(random.choices(russian_letters, k=8)) + ', ' + ''.join(random.choices('123456789', k=2))

