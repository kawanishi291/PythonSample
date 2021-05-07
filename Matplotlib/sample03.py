import numpy as np
import matplotlib.pyplot as plt
 
# 折れ線グラフを出力
month = np.array(range(1, 13))
data = np.array([100, 300, 200, 500, 400, 500, 600, 700, 800, 900, 1100, 1200])
plt.plot(month, data)
plt.xlim([1, 13])
plt.ylim([0, 2000])
# plt.show()
print(month)
print(data)
