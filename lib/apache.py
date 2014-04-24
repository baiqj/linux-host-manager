# -*- coding: utf-8 -*-
# 这个是源代码文件，原apache.py已经重命名为apache.py.txt

import os
import sys
import subprocess
import commands
import re
import platform

import self_os #导入系统基本信息模块

############## Check ####################

def detec_apache_install():
	""" 
	检测apache是否安装
	通过检测apachectl来判断是否安装了apache服务
	0 表示已安装，1 表示未按装，-1 表示其他错误
	"""
	result = subprocess.Popen('updatedb && locate apachectl | grep "bin\/apachectl$"', shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	try:
		code = sys.getfilesystemencoding()
		result = result.communicate()[0].decode(code)
	except:
		print "执行shell命令错误."

	if result != "":
		return 0    # 0 表示apache has been installed
	elif result == "":
		return 1	# 1 表示 apache not been installed
	else:
		return -1	# -1 表示程序错误

def detec_apache_bin_path(osVersion, installWay):
	"""
	检测apachectl或httpd的路径
	输出绝对路径，Examle: '/usr/local/apahce/bin/apachectl'
	"""
	if osVersion == 'redhat' or osVersion ==  'centos':
		subprocess.call("yum install mlocate -y", shell = True)
	elif osVersion == 'debian' or osVersion == 'ubuntu':
		subprocess.call("apt-get install -y mlocate", shell = True)
	else:
		print "Not suppport the distribution"

	result = commands.getoutput('locate apachectl | grep "bin\/apachectl$"')
	return result

def detec_apache_install_way(binPath):
	"""
	检测apache的安装方式	
	"""
	commands.getoutput(binPath + """ -V  |   grep  "HTTPD_ROOT"  |  awk  -F "="  '{print $2}'  |  awk  -F  '"'   '{print  $2}' > .tmpfile""")

        isRPM = commands.getoutput("""grep "/etc/httpd" .tmpfile""")
        if isRPM.strip() == '':
                isRPM = False
        else:
                isRPM = True

        isMake = commands.getoutput(""" grep -v '/etc/httpd' .tmpfile""")
        if isMake.strip() == '':
                isMake = False
        else:
                isMake = True

	commands.getstatus('rm -f .tmpfile')
        return [{'RPM':isRPM}, {'Make':isMake}]

def detec_apache_config(binPath):
	"""
	检测apache的配置文件是否存在语法错误
	"""
	result = commands.getoutput( binPath + " -t")
	match = re.findall(r"Syntax OK$", result, re.M)
	if match:
		print "配置文件语法正确."
	else:
		print "语法错误."

def detec_apache_version(binPath):
	"""
	通过apache bin 文件（httpd或apachectl）检测apache的版本号 example: 2.2.22
	"""
	result = commands.getoutput(binPath + """ -V | grep "Server version" | awk -F '[ /]' '{print $4}'""")
	return result 

def detec_apache_root(binPath):
	"""
	根据apachectl -V 获得apache的安装路径
	"""
	result = commands.getoutput(binPath + """ -V |  grep  -i "HTTPD_ROOT"  | awk  -F  '[="]'  '{print $3}'""")
	return result

def detec_apache_conf_path(binPath):
	"""
	根据apachectl -V 获得ROOT路径和CONF路径即可得到CONF的相对路径
	"""
	apacheRootPath = detec_apache_root(binPath)
	confPath = commands.getoutput(binPaht + """ -V | grep -i "SERVER_CONFIG_FILE" | awk -F "=" '{print $2}'""")
	return os.path.join(apacheRootPath, confPath.strip('"'))
	

def detec_apache_operate(installWay):
	"""
	根据安装方式判定apache服务的启动/关闭命令
	"""
	if installWay == 'rpm':
		return "service httpd"
	elif installWay == 'apt-get':
		return "/etc/init.d/apache"
	else:
		return "apachectl -k"

def detec_apache_vhost(binPath):
	"""
	检测apache是否启用了vhost，配置虚拟主机
	"""
	result = commands.getoutput(binPath + ' -S | grep -i "namevhost"')
	if result == '':
		return 1 # 1表示未启用
	else:
		return 0  # 0 表示启用

def detec_apache_vhost_conf():
	"""
	检测apache的vhost虚拟主机端配置文件路径
	输出apache每个虚拟主机端主配置文件路径
	"""

def detec_apache_domainname():
	"""
	查找apache中配置端网站域名和对应的网站目录位置
	"""

def detec_apache_php():
	"""
	检测apache是否配置了php模块
	"""



def detec_apache_listen(confPath):
	"""
	检测apache 监听端口
	"""


############### Install #####################

def install_apache(osVersion):
	if osVersion == 'centos' or osVersion == 'redhat':
		subprocess.call('yum -y install httpd httpd-devel', shell = True)
		# return install way = yum, httpd.conf, apache bin file,
	elif osVersion == 'debian' or osVersion == 'ubuntu':
		subprocess.call('apt-get install apache -y', shell = True)
		# return install way = yum, httpd.conf, apache bin file,
	else:
		print " %s is not the supported os types." % osVersion

def install_apache_security(osVersion):
	if osVersion == 'centos' or osVersion == 'redhat':
		subprocess.call('yum -y install mod_security', shell = True)
		# return install result
	elif osVersion == 'debian' or osVersion == 'ubuntu':
		subprocess.call('apt-get install mod_security -y', shell = True)
		# return install result
	else:
		print " %s is not the supported os types." % osVersion

def install_apache_ssl(osVersion):
	if osVersion == 'centos' or osVersion == 'redhat':
		subprocess.call('yum -y install mod_ssl', shell = True)
		# return install result
	elif osVersion == 'debian' or osVersion == 'ubuntu':
		subprocess.call('apt-get install mod_ssl -y', shell = True)
		# return install result
	else:
		print " %s is not the supported os types." % osVersion
	

if __name__ == '__main__':
	#print detec_apache_install()
	#detec_apache_bin_path()
	binPath = detec_apache_bin_path('centos','rpm')
	print "%r" % binPath
	#detec_apache_config(binPath)
	print detec_apache_install_way(binPath)
