import time
import numpy as np
import matplotlib.pyplot as plt

class Random:
    a = 16807
    m = 2**15
 
    def __init__(self):
        Random.x = time.time()

    def nextDouble(self,leftBorder,rightBorder):
        Random.x  = (Random.a * Random.x)%Random.m
        return (Random.x / Random.m) * (rightBorder - leftBorder) + leftBorder
    
    def nextInt(self,leftBorder,rightBorder):
        return int(self.nextDouble(leftBorder,rightBorder))
 
random = Random()

values = []
signal_amount = 500
minimumValueOfRandom = 0
maximumValueOfRandom = 1
step = maximumValueOfRandom/25

for i in range(signal_amount):

    values.append(random.nextDouble(minimumValueOfRandom,maximumValueOfRandom))

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

x = np.array([x for x in range(signal_amount)])
y = np.array(values)

expected_val = sum(values)/signal_amount
dispersion = sum(list(map(lambda x: (x-expected_val) ** 2,values)))/signal_amount
standart_deviation = dispersion**0.5
print(f"Количество чисел равно {signal_amount}")
print("---------------")
print("Статистический тест")
print("Мат. ожидание:")
print(expected_val)
print("Дисперсия:")
print(dispersion)
print("Ср.квадратичное:")
print(standart_deviation)

leftBorderIdeal = expected_val - standart_deviation
rightBorderIdeal = expected_val + standart_deviation

idealNumbers = [x for x in values if x>leftBorderIdeal and x<rightBorderIdeal]
percentage = len(idealNumbers)/signal_amount * 100
print("---------------")
print("Частотный тест:")
print(f"{percentage:.4f}% значений попали в отрезок ({leftBorderIdeal:.4f};{rightBorderIdeal:.4f})")

# matplotlib histogram
plt.hist([values,idealNumbers], color = ['lightgreen','violet'], label=['Числа вне эталонного диапазона','Эталонный диапазон'],
         bins = int(maximumValueOfRandom/step))

# Add labels
plt.title('Распределение случайных чисел')
plt.ylabel('Количество')
plt.xlabel('Отрезок')
plt.legend()
plt.show()
