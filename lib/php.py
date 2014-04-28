# -*- coding:utf-8 -*-
# 原php.py文件已被重命名为php.py.txt

import sys
import subprocess
import commands


def detec_php_install():
	"""
	检测php是否安装
	"""
	try:
		retcode = subprocess.check_output('php -v', shell = True)
		if retcode == 'sh: php: command not found':
			return 1	# php 未安装
		else:
			return 0 	# php 已安装
	except OSError as e:
		print >>sys.stdout, "php -v : error:", e
		return -1	# subprocess call error

def detec_php_install_way(install, osVersion):
	"""
	检测PHP的安装方式
	"""
	if not install:
		return 1	# PHP 为安装，程序退出
	else:
		output = subprocess.check_output(""" php  --ini  |  grep  "Configuration File (php.ini) Path:"  |awk  '{print  $5}'  |  grep  "^/etc" """)
		if output != '':
			if osVersion[0] == 'centos' or osVersion[0] == 'redhat':
				return 'yum'
			elif osVersion[0] == 'debian' or osVersion[0] == 'ubuntu':
				return 'apt-get'
			else:
				print >>sys.stdout ,"Not supported os version"
				return -1
		else:
			return 'make'
			

def detec_php_version(phpBinPath):
	"""
	通过PHP命令获取php版本
	"""
	phpVersion = commands.getoutput(phpBinPath + """ -v  |  grep  "^PHP"  |  awk  '{print  $2}'  """)
	return phpVersion

def detec_php_install_path(phpBinPath, installWay):
	"""
	获取PHP的安装路径
	"""

def detec_php_ini(phpBinPath):
	"""
	检测PHP配置文件的路径
	"""
	phpConfPath = commands.getoutput(phpBinPath + """ --ini | grep 'Loaded Configuration File:' 
					| awk '{print $4}' """)
	return phpConfPath

####################安装类 functions #######################

def install_php(osVersion):
	"""
	安装PHP
	"""
	if osVersion[0] == 'centos' or osVersion[0] == 'redhat':
		if osVersion[1].startswith('5'):
			subprocess.call("""  yum  -y install   php53   php53-bcmath  
					php53-mysql  php53-process  php53-mcrypt  php53-devel  
					php53-gd  php53-imap  php53-mbstring   php53-pdo  
					php53-soap   php53-xml  php53-xmlrpc   php53-intl  
					php53-enchant  php53-php-gettext  php53-pspell mhash-devel 
					mhash  libmcrypt  libmcrypt-devel  """, shell = True)
		elif osVersion[1].startswith('6'):
			subprocess.call(""" yum -y install php   php-bcmath  php-mysql  php-process    
					php-mcrypt   php-devel  php-gd       php-imap    php-mbstring
					php-pdo   php-soap   php-xml php-xmlrpc   php-intl      
					php-enchant   php-php-gettext    php-pspell   mhash-devel 
					mhash   libmcrypt  libmcrypt-devel  php-fpm  """, shell = True)
		else:
			print "系统版本号错误"
	elif osVersion[0] == 'debian' or osVersion[0] == 'ubuntu':
		print "Please use apt-get to install php"
	else:
		print >>sys.stdout, "Not supported OS type"
		return -1



def detec_php_bin_path(osVersion, installWay):
	"""
	检测PHP命令的路径
	"""
	subprocess.call('', shell = True)


if __name__ == '__main__':
	#detec_php_install()
	detec_php_install_way(True, ['centos','6.5','x86_64'])
