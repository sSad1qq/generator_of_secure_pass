import random


def password_generate(length, symbols, count_passwords):
    passwords_list = []
    for i in range(count_passwords):
        passwords_list.append("".join(random.sample(symbols, length)))
    return passwords_list


DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATIONS = '!#$%&*+-=?@^_'
SIMILAR_SYMBOLS = 'il1Lo0O'


chars = ''
print('Сколько паролей Вы хотите сгенерировать?')
count_gen_passwords = int(input())
print('Какая должна быть длина у одного пароля?')
length_gen_passwords = int(input())
print('Должен ли пароль включать цифры? (y / n)')
digits_gen_passwords = str(input())
if digits_gen_passwords == 'y':
    chars += DIGITS
print('Должен ли пароль включать прописные буквы? (y / n)')
uppercase_gen_passwords = str(input())
if uppercase_gen_passwords == 'y':
    chars += UPPERCASE_LETTERS
print('Должен ли пароль включать строчные буквы? (y / n)')
lowercase_gen_passwords = str(input())
if lowercase_gen_passwords == 'y':
    chars += LOWERCASE_LETTERS
print('Должен ли содержать пароль спец. символы "!#$%&*+-=?@^_"? (y / n)')
punctuations_gen_passwords = str(input())
if punctuations_gen_passwords == 'y':
    chars += PUNCTUATIONS
print('Должен ли пароль включать неоднозначные символы "il1Lo0O"? (y / n)')
similar_symbols_gen_passwords = str(input())
if similar_symbols_gen_passwords == 'y':
    chars += SIMILAR_SYMBOLS


print(*password_generate(length=length_gen_passwords, symbols=chars, count_passwords=count_gen_passwords), sep='\n')