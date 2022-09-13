from collections import Counter
import numpy as np

random_elements = np.random.randint(0,6,100)
dict_freq = Counter(random_elements)
print(dict_freq)