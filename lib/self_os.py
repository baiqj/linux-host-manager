# -*- coding:utf-8 -*-
# 
# get the os base information

import platform

def detec_os_version():
	"""检测系统的类型，版本和架构"""
	linux_dist = platform.linux_distribution()
	machine = platform.machine()
	return [linux_dist[0].lower(), linux_dist[1], machine]

def detec_data_space():
	"""判断是否有问分区磁盘"""

def detec_disk_space():
	"""检测空间最大分区"""
	"""输出剩余空间最大的磁盘分区"""

def initialize_disk(diskName,isExist):
	"""额外磁盘端分区和挂载"""
	""" diskName 是表示剩余空间最大的磁盘，由detec_disk_space()获得"""
	""" isExist  表示是否存在额外磁盘，由detec_data_disk()获得"""
	"""返回额外磁盘挂载点"""
	


if __name__ == '__main__':
	print detec_os_version()
