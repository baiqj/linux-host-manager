# -*- coding:utf-8 -*-
# 原php.py文件已被重命名为php.py.txt

import subprocess
import commands


def detec_php_install():
	"""检测php是否安装"""
	#result = subprocess.Popen('php -v', shell = True)
	status, output = commands.getstatusoutput('php -v')
	if output == "sh: php: command not found":
		print 1		# 表示php 未安装
	else:
		print 0		# 表示php 已安装

def detec_php_install_way(isInstalled, osVersion):
	if isInstalled == False:
		return 1
	else:
		output = commands.getoutput(""" php  --ini  |  grep  "Configuration File (php.ini) Path:"  |awk  '{print  $5}'  |  grep  "^/etc" """)
		if output != '':
			if osVersion[0] == 'centos' or osVersion[0] == 'redhat':
				print 'yum'
			elif osVersion[0] == 'debian' or osVersion[0] == 'ubuntu':
				print 'apt-get'
			else:
				print "Not supported os version"
		else:
			print 'make'
			

def detec_php_version(phpBinPath):
	phpVersion = commands.getoutput(""" php  -v  |  grep  "^PHP"  |  awk  '{print  $2}'  """)
	print phpVersion

def detec_php_install_path(phpBinPath, installWay):
	

def detec_php_ini():
	phpConfPath = commands.getoutput(""" php --ini | grep 'Loaded Configuration File:' | awk '{print $4}' """)
	return phpConfPath

####################安装类 functions #######################

def install_php(osVersion):
	if osVersion[0] == 'centos' or osVersion[0] == 'redhat':
		if osVersion[1].startswith('5'):
			subprocess.call("""  yum  -y install   php53   php53-bcmath  php53-mysql  php53-process  php53-mcrypt  php53-devel  php53-gd  php53-imap  php53-mbstring   php53-pdo  php53-soap   php53-xml  php53-xmlrpc   php53-intl  php53-enchant  php53-php-gettext  php53-pspell mhash-devel mhash  libmcrypt  libmcrypt-devel  """, shell = True)
		elif osVersion[1].startswith('6'):
			subprocess.call(""" yum -y install php   php-bcmath  php-mysql  php-process    php-mcrypt   php-devel  php-gd       php-imap    php-mbstring     php-pdo   php-soap   php-xml php-xmlrpc   php-intl      php-enchant   php-php-gettext    php-pspell   mhash-devel mhash   libmcrypt  libmcrypt-devel  php-fpm  """, shell = True)
		else:
			print "系统版本号错误"
	elif osVersion[0] == 'debian' or osVersion[0] = 'ubuntu':
		print "Please use apt-get to install php"
	else:
		print "Not supported OS type"



def detec_php_bin_path(osVersion, installWay):
	subprocess.call('', shell = True)


if __name__ == '__main__':
	#detec_php_install()
	detec_php_install_way(True, ['centos','6.5','x86_64'])
