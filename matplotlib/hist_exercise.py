from matplotlib import pyplot as plt
from matplotlib import font_manager

interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]
width = [5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]
quantity = [836, 2737, 3723, 3926, 3596, 1438, 3273, 642, 824, 613, 215, 47]

plt.figure(figsize=(30, 10), dpi=80)

# 对于已经分好组的数据只能采用条形图来绘制
plt.bar(range(len(interval)), quantity, width=1)

# 调整x轴位置
## 13而不是12是为了让最后一组数据的边界能够有数字
_x = [i-0.5 for i in range(len(interval)+1)]
_xticks_labels = interval + [150]
plt.xticks(_x, _xticks_labels)

plt.grid()
plt.show()