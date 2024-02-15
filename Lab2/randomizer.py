import time
import numpy as np
import matplotlib.pyplot as plt

class Random:
    a = 16807
    m = 2**15
 
    def __init__(self):
        Random.x = time.time()

    def next(self):
        
        Random.x = int((Random.a * Random.x)%Random.m)
        return Random.x
 
random = Random()
values = []
signal_amount = 10000

for i in range(signal_amount):

    values.append(random.next())

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

x = np.array([x for x in range(signal_amount)])
y = np.array(values)

print(values)

expected_val = sum(values)/signal_amount
dispersion = sum(list(map(lambda x: (x-expected_val) ** 2,values)))/signal_amount
standart_deviation = dispersion**0.5

print(expected_val)
print(dispersion)
print(standart_deviation)

plt.title("Line graph")
#plt.plot(x, y, color="violet")


# matplotlib histogram
plt.hist(values, color = 'blue', edgecolor = 'black',
         bins = int(Random.m/1680.7))

# Add labels
plt.title('Распределение случайных чесил')
plt.xlabel('Количество')
plt.ylabel('Отрезок')

plt.show()
