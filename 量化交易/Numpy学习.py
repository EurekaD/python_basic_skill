import numpy as np


list_array = np.arange(10)

raw = np.array(list_array).reshape((2, 5))
raw1 = np.ones(shape=(2, 5))

a = raw * 3
b = raw - raw1
c = raw.reshape(5, 2)

print(raw)
print(raw1)
print(a)
print(b)
print(a.dot(c))
