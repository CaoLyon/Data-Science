import numpy as np

us_file_path = "F:/code\python/tf_exercise/numpy/youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "F:/code\python/tf_exercise/numpy/youtube_video_data/GB_video_data_numbers.csv"

# 加载国家数据
us_data = np.loadtxt(fname=us_file_path, delimiter=",", dtype=int)
uk_data = np.loadtxt(fname=uk_file_path, delimiter=",", dtype=int)

# 添加国家信息
zeros_data = np.zeros((us_data.shape[0], 1)).astype(int)        # astype()将类型转换，防止后续出现科学计数法
ones_data = np.ones((uk_data.shape[0], 1)).astype(int)


# 分别添加一列全为0,1的数组
us_data = np.hstack((us_data, zeros_data))
uk_data = np.hstack((uk_data, ones_data))

# 拼接两组数据
final_data = np.vstack((us_data, uk_data))
print(final_data)