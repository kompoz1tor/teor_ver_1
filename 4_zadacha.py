'''
В лотерее 100 билетов. Из них 2 выигрышных. 
Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?
'''

# Функция сочетания
from math import factorial
def combination(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n-k)))

# Общая вероятность
total = combination(100, 2)
# Ответ
result = round(1/total, 5)
print(result)