# import pandas as pd
# print("heelo, world")
# df = pd.read_excel(r"record.xlsx",header=[0,1])
# print(df)

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()