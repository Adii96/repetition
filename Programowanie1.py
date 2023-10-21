def square_area(a,b):
    return a * b

print(square_area(10, 50))

def circle_circuit(diameter):
    return round(2 * 3.14 * (diameter/2), 15)

print(circle_circuit(20))
print(circle_circuit(21))
print(circle_circuit(22))

def dogs_age(age):
    if age <= 2:
        dog = age * 10.5
    elif age > 2:
        dog = (10.5 * 2) + age * 4
    return dog
print(dogs_age(0.5))
print(dogs_age(1.5))
print(dogs_age(3))
print(dogs_age(5))
print(dogs_age(12.3))

def chessboard(n=8):
    linia = ""
    for i in range(n):
        if i % 2 == 0:
           element = "# "
        elif i % 2 == 1:
           element = " #"
        wiersz = element * ((n //2) + 1)
        linia = linia + wiersz[:n] + '\n' 
    return linia


print(chessboard())


def is_divisible_by_4(number):
    if number % 4 == 0:
        return True
    else:
        return False
print(is_divisible_by_4(16))
print(is_divisible_by_4(7))
print(is_divisible_by_4(2))


def histogram(d):
    a = ""
    for liczba_znaków in d:
        if not isinstance(liczba_znaków, int):  # if type(v) is not int
            return None
        b = ""
        i = 0
        while i < liczba_znaków:
            b = b + "#"
            i += 1
        a = a + b + "\n"
    return a
        
        
print(histogram([2, 6, 3, 1]))
print(histogram([1, 2, 'error!']))


def fib(n):
    if n < 1:
        return 0
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)
    
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(7))
        
        
def create_list(a, b):
    return [a, b] * 4

print(create_list(1 ,2))
print(create_list(True, False))    

def list_keys(d):
    #    return [*d.keys()]
    return [k for k in d]
       
print(list_keys({'1': 'klucz', '2': 'zamek', '3': 'drzwi'}))

def find_short_words(lista):
    # return [ words for words in lista if len(words)< 5]
    li = []
    for words in lista:
        if len(words) <= 5:
            li.append(words)
    return li
print(find_short_words(['Adrian', 'Niko', 'Samochód', 'Pies', 'aaaaa']))

def suma(numbers):
    # return sum(numbers)
    s = 0
    for i in numbers:
        s += i
    return s

print(suma([3,5,7,9]))

def mean(numbers):
    # return sum(numbers) / len(numbers)
    s = 0 
    for i in numbers:
        s += i
    return s / len(numbers)

print(mean([3,5,7,9]))

def all_keys_present(d):
    return "name" in d and "role" in d and "movie" in d

def message(d):
    if not all_keys_present(d):
        return None
    return f"In {d['movie']}, {d['name']} is a {d['role']}"

input_dict = {
    "name": "Han Solo",
    "role": "smuggler",
    "movie": "Star Wars"
} 
print(message(input_dict))

from random import randint
def d6(num):
    sum = 0
    for i in range(num):
        sum += randint(1, 6)
    return sum
print(d6(2))

from datetime import date, timedelta
def tomorrow():
    return date.today() + timedelta(days=1)
print(tomorrow())

from coderslab import coderslab_welcome, random_word
print(coderslab_welcome(), random_word())

from math_tools import functions
print(functions.quadratic_function(2,3,4,5))

# Day 2 homework 

def make_tuple(a,b,c=3,d=4):
    return (a, b, c, d)
print(make_tuple('mama', 'brak'))

def find_first_and_last(value):
    return (value[0]), (value[-1])

print(find_first_and_last([1, 2, 3, 4, 5]))

def miesiąc(day, month, year):
    if month == 1 and day <= 31:
        return f"{day}, Styczeń, {year}"
    elif month == 2 and day <= 28:
        return f"{day}, Luty, {year}"
    elif month == 3 and day <= 31:
        return f"{day}, Marzec, {year}"
    elif month == 4 and day <= 30:
        return f"{day}, Kwiecień, {year}"
    elif month == 5 and day <= 31:
        return f"{day}, Maja, {year}"
    elif month == 6 and day <= 30:
        return f"{day}, Czerwca, {year}"
    elif month == 7 and day <= 31:
        return f"{day}, Lipca, {year}"
    elif month == 8 and day <= 31:
        return f"{day}, Sierpnia, {year}"
    elif month == 9 and day <= 30:
        return f"{day}, Wrzesnia, {year}"
    elif month == 10 and day <= 31:
        return f"{day}, Październik, {year}"
    elif month == 11 and day <= 30:
        return f"{day}, Listopad, {year}"
    elif month == 12 and day <= 31:
        return f"{day}, Grudzień, {year}"
    else:
        return None

print(miesiąc(31, 1, 2012))
print(miesiąc(28, 2, 2012))
print(miesiąc(31, 3, 2012))
print(miesiąc(1, 4, 2012))
print(miesiąc(15, 13, 2012))
print(miesiąc(20, 6, 2012))
print(miesiąc(2, 7, 2012))
print(miesiąc(10, 8, 2012))
print(miesiąc(1, 9, 2012))
print(miesiąc(30, 10, 2012))
print(miesiąc(11, 11, 2012))
print(miesiąc(12, 20, 2012))


def find_boundaries(lista):
    l = sorted(lista)
    return ((l[0]), l[-1])
print(find_boundaries([5, -1, 3, 4, -2]))
    
    
def censor(text):
    a = text.split()
    words = ['Java', 'C#', 'Ruby', 'PHP']
    result = []
    for i in a:
        if i in words:
            result.append('****')
        else:
            result.append(i)
    return ' '.join(result)
    
    
    
print(censor("Java is the best, but PHP is the bestest!")) 
  
    
def check_palindrome(text):
    if text.upper() == text[::-1].upper():
        return True
    else:
        return False

print(check_palindrome('Anna'))
print(check_palindrome('Adrian'))

def phone(number):
    lista = [123, 234, 555, 678, 985, 1235]
    if number in lista:
        return number
        
    else:
        raise Exception('Nie ma takiego numeru')
        
        
        
print(phone(123))
print(phone(555))


# zadania dom dizeń 3
import random

def random_average(n):
    lista = []
    for i in range(n):
        liczny = random.randint(1,100)
        lista.append(liczny)
    print(lista)
    return sum(lista)/len(lista)

print(random_average(8))
print(random_average(5))

def div():
    while True:
        try:
            a = int(input('Podaj liczbę: '))
            b = int(input('Podaj drugą liczbę: '))
            division = a/b
            break
        except ValueError:
            print('To nie jest liczba. Podaj liczbe: ')
        except ZeroDivisionError:
            print('Nie wolno dzielic przez zero !')
    return division
# print(div())

def validate_pesel(pesel):
    a = int(pesel[0]) * 1
    b = int(pesel[1]) * 3
    c = int(pesel[2]) * 7
    d = int(pesel[3]) * 9
    e = int(pesel[4]) * 1
    f = int(pesel[5]) * 3
    g = int(pesel[6]) * 7
    h = int(pesel[7]) * 9
    i = int(pesel[8]) * 1
    j = int(pesel[9]) * 3
    suma = a + b + c + d + e + f + g + h + i + j 
    dzielenie = suma % 10
    odjmowanie = 10 - dzielenie
    if odjmowanie == int(pesel[10]):
        return True
    else:
        return False
print(validate_pesel('44051401358'))
print(validate_pesel('44051401359'))
    
    
    