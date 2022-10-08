import numpy as np

us_file_path = "F:/code\python/tf_exercise/numpy/youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "F:/code\python/tf_exercise/numpy/youtube_video_data/GB_video_data_numbers.csv"

# 采用comma分割，指定加载数据类型
t1 = np.loadtxt(us_file_path, delimiter=",", dtype="int")
t2 = np.loadtxt(uk_file_path, delimiter=",", dtype="int")

# print(t1)
#
# # 取行
# print(t1[2])
#
# # 取连续多行
# print(t1[2:])
#
# # 取不连续多行
# print(t1[[2, 8, 10]])
#
# # 取列操作
# print(t1[:, 0])
#
# # 取连续多列
# print(t1[:, 2:])
#
# # 取不连续多列
# print(t1[:, [0, 1, 3]])
#
# # 取单个数
# print(t1[2, 3])
#
# # 取多行多列
# print(t1[2: 5, 1: 4])
#
# # 取多个不相邻的点
# print(t1[[0, 1], [0, 2]])

# t2 = np.arange(24).reshape(4, 6)
# print(t2)
# print(t2.transpose())
# print(t2.T)
# print(t2.swapaxes(0, 1))


