def my_func( name, surname, birth, city, email, number):
    print(f"Ваше имя {name} , фамилия {surname}, Вы родились в {birth} году, живете в {city}, ваша электронная почта {email}, номер телефона {number}")

my_func(input('Введите имя: '), input('Введите фамилию: '), input('Введите дату рождения: '), input('Введите город: '), input('Введите электронную почту: '), input('Введите номер телефона: '))

#  вариант 2, как правильно?

def my_func( name, surname, birth, city, email, number):
    print(f"Ваше имя {name} , фамилия {surname}, Вы родились в {birth} году, живете в {city}, ваша электронная почта {email}, номер телефона {number}")

user_name = input('Введите имя: ')
user_surname = input('Введите фамилию: ')
user_birth = input('Введите дату рождения: ')
user_city = input('Введите город: ')
user_email = input('Введите электронную почту: ')
user_phone = input('Введите номер телефона: ')

my_func(name=user_name, surname=user_surname, birth=user_birth, city=user_city, email=user_email, number=user_phone)