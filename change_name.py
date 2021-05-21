import os

class Change_Name(object):
	def __init__(self):
		# 文件绝对路径
		self.target_path = os.path.abspath(__file__)
		# 文件所在路径的根目录路径
		self.target_dir_path = os.path.dirname(self.target_path)
		# 获取文件所在根目录名
		self.target_dir_path_name = self.target_dir_path.split("/")[-1]
		# print(f"目录名:{self.target_dir_path_name}")
        	# 文件所在路径的根目录路径下，所有文件的名字
		self.files_name = os.listdir(self.target_dir_path)

	'''	
	思路：	
	Step1：如果files_name 这个列表不为空，就可以进行修改
	             如果为空，输出 “没有文件要修改”

	Step2:不为空的情况判断是以什么分割的，
               如果用 . 分割，就拆分成  文件名 + . + 后缀名  这种形式
	      
	'''
	
	def change_files_name(self):
		print(f"文件绝对路径：{self.target_path}")
		print(f"文件所在路径：{self.target_dir_path}")
		if len(self.files_name) != 0:
			# 先将列表中的每一个元素都遍历出来
			for each_elem in self.files_name:
				# 如果是以 . 来分割文件名和后缀
				if each_elem.find('.')!=-1:
					print(f"{each_elem}   确实以.分割")
					# 开始分割
					# 文件名
					file_name, file_suffix = os.path.splitext(each_elem)
					# 将文件名重新命名为：目录名+文件名
					new_file_name = self.target_dir_path_name + '_' +  file_name
					combine = new_file_name + file_suffix
					old_path_and_file_name = os.path.join(self.target_dir_path, each_elem)
					print(f"旧文件：{old_path_and_file_name}")
					new_path_and_file_name = os.path.join(self.target_dir_path, combine)
					print(f"新文件：{new_path_and_file_name}")
					# 重新命名执行
					os.rename(old_path_and_file_name, new_path_and_file_name)
					continue
				else:
					print(f"{each_elem}   没有用.分割")

a = Change_Name()
a.change_files_name()
