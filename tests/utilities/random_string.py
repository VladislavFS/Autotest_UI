import random
import string


def generate_random_text_string(length, language='ENG'):
    if language == 'ENG':
        letters_and_digits = string.ascii_letters + string.digits + '_-'
        rand_string = ''.join(random.sample(letters_and_digits, length))
        return rand_string
    elif language == 'RU':
        letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        letters1 = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        letters_and_digits = letters + letters1
        rand_string = ''.join(random.sample(letters_and_digits, length))
        return rand_string


def random_multiple_selects():
    plase = ['Sea', 'Mountains', 'Old town', 'Ocean', 'Restaurant']
    transport = ['Car', 'Bus', 'Train', 'Air']
    time = ['Today', 'Tomorrow', 'Next week']
    options = [plase, transport, time]
    multiple = [random.choice(i) for i in options]
    return multiple


def random_programming_language():
    return random.choice(['Python', 'Ruby', 'JavaScript', 'Java', 'C#'])
