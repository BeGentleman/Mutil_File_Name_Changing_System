import os

# 文件绝对路径
target_path = os.path.abspath(__file__)
# 文件所在路径的根目录路径
target_dir_path = os.path.dirname(target_path)

# 文件所在路径的根目录路径下，所有文件的名字
files_name = os.listdir(target_dir_path)
print(files_name)
