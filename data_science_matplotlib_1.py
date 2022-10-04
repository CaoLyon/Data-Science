import random

from matplotlib import pyplot as plt

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


#####################################################################
# 将列表x表示为10点到12点每一分钟的气温
x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

fig = plt.figure(figsize=(20, 8), dpi = 80)

plt.plot(x, y)

# 调整x轴刻度
# 将字符串传递到坐标轴之前需要将字符串和坐标轴做一个一一对应
_x = x
# _x = list(x)[::10] 字符串太长了可以增加步长
_xticks_labels = ['10点{}分'.format(i) for i in range(60)]
_xticks_labels += ['11点{}分'.format(i) for i in range(60)]

plt.xticks(_x[::10], _xticks_labels[::10])

plt.show()

######################################################################




