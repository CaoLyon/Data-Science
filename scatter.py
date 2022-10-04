from matplotlib import pyplot as plt
from matplotlib import font_manager
import random

y_3 = []
y_10 = []
for i in range(30):
    y_3.append(random.randint(5, 15))
    y_10.append(random.randint(20, 35))

x_3 = range(1, 31)
x_10 = range(51, 81)

fig = plt.figure(figsize=(20, 8), dpi=80)

# Add proper font
my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\simfang.ttf')

x_range = list(x_3) + list(x_10)
_xticks = ["三月{}日".format(i) for i in x_3]
_xticks += ["十月{}日".format(i-50) for i in x_10]

plt.xticks(x_range[::2], _xticks[::2], fontproperties=my_font, rotation=45)

# Scatter plot
plt.scatter(x_3, y_3, label="三月", color='r')
plt.scatter(x_10, y_10, label="十月", color='b')

# Add description
plt.legend(prop=my_font, loc="best")
plt.xlabel("日期", fontproperties=my_font)
plt.ylabel("温度(℃)", fontproperties=my_font)
plt.title("三月和十月的温度曲线", fontproperties=my_font)

plt.show()