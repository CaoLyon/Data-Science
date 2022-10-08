import numpy as np

t1 = np.arange(12)
print(t1)
print(t1.shape)

t2 = np.array([[1, 2, 3], [4, 5, 6]])
print(t2)
print(t2.shape)

t3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(t3)
print(t3.shape)

# reshape修改形状
## 调用reshape不会改变原值
t4 = np.arange(12)
print(t4)
print(t4.reshape(3, 4))

t5 = np.arange(24).reshape(2, 3, 4)
print(t5)
print(t5.shape)

t6 = t5.reshape(24)
print(t6)
print(t6.shape)

t7 = t5.reshape(1, 24)
print(t7)
print(t7.shape)

# 对于未知数量的矩阵转化为一维
t8 = t5.reshape(t7.shape[0] * t7.shape[1])
print(t8)
t9 = t5.flatten()
print(t9)

# 广播机制
t10 = t5 + 2
print(t5)
print(t10)

# nan & inf
print(t5 / 0)
## 对于计算机来说0是用很小的一个数来表示的

t5 = t5.reshape(4, 6)
t11 = np.arange(6)
print(t5)
print(t5 + t11)

t12 = np.arange(4).reshape(4, 1)
print(t5)
print(t5 - t12)

