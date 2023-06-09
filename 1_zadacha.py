'''
Из колоды в 52 карты извлекаются случайным образом 4 карты. 
- Найти вероятность того, что все карты  крести. 
- Найти вероятность, что среди 4 карт окажется хотя бы один туз.
'''

'****************************************** Задача А ******************************************'
print ('Вероятность того, что все карты  крести:')
ver = round((13/52)*(12/51)*(11/50)*(10/49)*100, 3)
print (ver)

# Функция сочетания
from math import factorial
def combination(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n-k)))

'считаем сколько всего исходов вытянуть 4 разные карты'
c1 = combination(52, 4)
#print(c1)
'колько всего карт одной масти 52 / 4 = 13'
mast = 13
'вероятность вытянуть 1 карту одной масти'
c2 = combination(13,4)
#print(c2)
'вероятность того, что все карты  крести'
c3 = c2 / c1
print(c3)
'****************************************** Задача Б ******************************************'


'известно что всего тузов 4, нужен хотя бы  1 - это значит что благоприятной вероятностью будет сумма вероятностей c 1, 2, 3, 4 тузами'
c_1_ace = combination(4,1)*combination(48,3) # вероятность достать 1 туз и 3 не туза
c_2_ace = combination(4,2)*combination(48,2) # вероятность достать 2 туза и 2 не туза
c_3_ace = combination(4,3)*combination(48,1) # вероятность достать 3 туза и 1 не туз
c_4_ace = combination(4,4) # вероятность достать 4 туза из 4 возможных
positive = c_1_ace + c_2_ace + c_3_ace + c_4_ace
# print(positive) 
print('Вероятность, что среди 4 карт окажется хотя бы один туз:')
c_ace = positive/c1
print(c_ace)