import numpy as np

# t1 = np.arange(24).reshape(4, 6)
# print(t1 < 10)
#
# t1[t1 < 10] = 0
# print(t1)
#
# # np.where三元运算符
# t1 = np.where(t1 <= 3, 9, 20)
# print(t1)
#
# # clip操作
# # .clip(num1, num2)将小于num1的替换为num1，将大于num2的替换为num2
# t1 = t1.clip(10, 18)
# print(t1)
#
# t1 = t1.astype("float64")
# t1[3, 3] = np.nan
# print(t1)

# t1 = np.arange(12).reshape(2, 6)
# t2 = np.arange(12, 24).reshape(2, 6)
#
# # vstack & hstack
# print(np.vstack(t1, t2))
# print(np.hstack(t1, t2))


# 数组的行交换
t = np.arange(12, 24).reshape(3, 4)
print(t)
t[[2, 1], :] = t[[1, 2], :]
print(t)

# 数据列交换
print(t)
t[:, [1, 2]] = t[:, [2, 1]]
print(t)

