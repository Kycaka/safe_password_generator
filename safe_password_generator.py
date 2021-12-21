import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'

chars = ''

pwd_quantity = input('Сколько паролей вам нужно сгенерировать? Укажите цифру: ')
while not pwd_quantity.isdigit():
    print('Нужно ввести цифру!')
    pwd_quantity = input('Сколько паролей вам нужно сгенерировать? Укажите цифру: ')

pwd_len = input('Какой длины должен быть пароль? Укажите цифру: ')
while not pwd_len.isdigit():
    print('Нужно ввести цифру!')
    pwd_len = input('Какой длины должен быть пароль? Укажите цифру: ')

pwd_digits = input('Включать ли в пароль цифры от 0 до 9? Напишите Да или Нет: ').strip()
while pwd_digits.lower() not in ['да', 'нет']:
    print('Нужно вводить "да" или "нет"')
    pwd_digits = input('Включать ли в пароль цифры от 0 до 9? Напишите Да или Нет: ').strip()

pwd_uppercase = input('Включать ли в пароль прописные буквы? Напишите Да или Нет: ').strip()
while pwd_uppercase.lower() not in ['да', 'нет']:
    print('Нужно вводить "да" или "нет"')
    pwd_uppercase = input('Включать ли в пароль прописные буквы? Напишите Да или Нет: ').strip()

pwd_lowercase = input('Включать ли в пароль строчные буквы? Напишите Да или Нет: ').strip()
while pwd_lowercase.lower() not in ['да', 'нет']:
    print('Нужно вводить "да" или "нет"')
    pwd_lowercase = input('Включать ли в пароль строчные буквы? Напишите Да или Нет: ').strip()

pwd_punctuation = input('Включать ли в пароль символы "!#$%&*+-=?@^_"? Напишите Да или Нет: ').strip()
while pwd_punctuation.lower() not in ['да', 'нет']:
    print('Нужно вводить "да" или "нет"')
    pwd_punctuation = input('Включать ли в пароль символы "!#$%&*+-=?@^_"? Напишите Да или Нет: ').strip()

pwd_exceptions = input('Исключать ли неоднозначные символы "il1Lo0O"? Напишите Да или Нет: ').strip()
while pwd_exceptions.lower() not in ['да', 'нет']:
    print('Нужно вводить "да" или "нет"')
    pwd_exceptions = input('Исключать ли неоднозначные символы "il1Lo0O"? Напишите Да или Нет: ').strip()

if pwd_digits == 'да':
    chars += digits
if pwd_uppercase == 'да':
    chars += uppercase_letters
if pwd_lowercase == 'да':
    chars += lowercase_letters
if pwd_punctuation == 'да':
    chars += punctuation
if pwd_exceptions == 'да':
    for i in "il1Lo0O":
        chars = chars.replace(i, '')


def generate_password(pwd_len, chars):
    password = ''
    for j in range(int(pwd_len)):
        password += random.choice(chars)
    return password


for _ in range(int(pwd_quantity)):
    print(generate_password(pwd_len, chars))
