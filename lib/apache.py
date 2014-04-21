# -*- coding: utf-8 -*-
# 这个是源代码文件，原apache.py已经重命名为apache.py.txt

import sys
import subprocess
import platform

import self_os

def detec_apache_install():
	result = subprocess.Popen('updatedb && locate apachectl | grep "bin\/apachectl$"', shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	try:
		code = sys.getfilesystemencoding()
		result = result.communicate()[0].decode(code)
	except Exception, e:
		print e

	if result != "":
		return 0    # 0 表示apache has been installed
	elif result == "":
		return 1	# 1 表示 apache not been installed
	else:
		return -1	# -1 表示程序错误

def detec_apache_bin_path():
	osDist = detec_os_version()[0]
	if osDist == 'redhat' or osDist ==  'centos':
		subprocess.call("yum install mlocate -y", shell = True)
	elif osDist == 'debian' or osDist == 'ubuntu':
		subprocess.call("apt-get install -y mlocate", shell = True)
	else:
		print "Not suppport the distribution"




if __name__ == '__main__':
	#print detec_apache_install()
	detec_apache_bin_path()
	
