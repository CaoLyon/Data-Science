import random
from matplotlib import pyplot as plt
from matplotlib import font_manager

# Lesson 1
#
#
# x = range(2, 26, 2)
# y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]
#
# plt.plot(x, y)
# plt.show()
#
# 设置图片大小
#
# fig = plt.figure(figsize=(20, 8), dpi = 80)
# figure指我们画的图
# 通过实例化一个figure并且传递参数能在后台自动使用该figure实例
# figsize = (width, height)在图像模糊的时候传入dpi参数可以让图片更清晰
#
# x = range(2, 26, 2)
# y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]
#
# plt.plot(x, y)
#
# # 绘制x轴的刻度
# plt.xticks(x)       # 将x刻度写入x轴
# # plt.xticks(range(2, 25))      # 按照指定的范围和刻度绘制
#
# # _xticks_ = [i/2 for i in range(4, 49)]        # 按照0.5步长取值
# # plt.xticks(_xticks_)
# plt.show()
#
# # 保存图片
# plt.savefig("./t1.png")


# #####################################################################
# 将列表x表示为10点到12点每一分钟的气温
# x = range(0, 120)
# y = [random.randint(20, 35) for i in range(120)]
#
# fig = plt.figure(figsize=(20, 8), dpi = 80)
#
# plt.plot(x, y)
#
# # 调整x轴刻度
# # 将字符串传递到坐标轴之前需要将字符串和坐标轴做一个一一对应
# _x = x
# # _x = list(x)[::10] 字符串太长了可以增加步长
#
# _xticks_labels = ['10点{}分'.format(i) for i in range(60)]
# _xticks_labels += ['11点{}分'.format(i) for i in range(60)]
#
# # find the supported font in your computer
# my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\simfang.ttf')
#
# # xticks, rotation
# plt.xticks(_x[::10], _xticks_labels[::10], rotation=45, fontproperties=my_font)
#
# # add description and change font
# plt.xlabel("时间", fontproperties=my_font)
# plt.ylabel("温度 单位(℃)", fontproperties=my_font)
# plt.title("10点到12点每分钟的气温变化情况", fontproperties=my_font)
# # show grid
# plt.grid(alpha=0.4)       # alpha means transparency, range: 0-1
#
# plt.show()

######################################################################
a = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 3, 3, 1, 1, 1]
b = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]

a_range = range(len(a))
b_range = range(len(b))

fig1 = plt.figure(figsize=[35, 10], dpi=80)
_xticks = ["{}岁".format(i) for i in a_range]

# set label, color and linestyle
plt.plot(a_range, a, label="自己", color='r', linestyle=":")
plt.plot(b_range, b, label="同桌", color='b', linestyle="--")
my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\simfang.ttf')

plt.legend(prop=my_font, loc="upper right")        #set legend and location
plt.grid(alpha=0.4)     # grid lines and grid transparency
plt.xticks(a_range, _xticks, fontproperties=my_font)
plt.xlabel("年龄", fontproperties=my_font)
plt.ylabel("个数", fontproperties=my_font)
plt.title("每年数量数量", fontproperties=my_font)

plt.show()
