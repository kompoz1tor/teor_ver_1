'''
В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали. 
Какова вероятность того, что все извлеченные детали окрашены?
'''
# Функция сочетания
from math import factorial
def combination(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n-k)))

total = combination(15, 3)
colored =  combination(9, 3)
result = round(colored/total*100, 2)
print(f'Вероятность того, что все извлеченные детали окрашены: {result}%')