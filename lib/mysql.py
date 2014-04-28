# -*- encoding:utf-8 -*-
# 原mysql.py 已经被重命名为mysql.py.txt
# 这个文件是参考mysql.py.txt编写端源代码文件

import os
import subprocess
import commands

############# check ################

def detec_mysql_install():
        try:
                returncode = commands.getoutput('updatedb && 
						locate mysqld_safe | grep "bin\/mysqld_safe$"')
                if returncode < 0:
                        print >>sys.stderr, "Shell cmd has been cancel", -returncode
        except OSError as e:
                print >>sys.stderr, "Execution failed:", e

        patter = re.search(r'bin/mysqld_safe$', returncode)
        if not patter:
                return 1   # mysql not been install
        else:
                return 0  #mysql is installed

def detec_mysql_install_way(install,osVersion):
	"""
	这是在确认mysql-server已经安装的情况下，
	"""
	if not install:
		print >>sys.stdout, "mysql-server is not been install"
		return -1   # mysql-server 没有被安装，程序退出

	if osVersion == 'centos' or osVersion == 'redhat':
		result = commands.getoutput('rpm -q mysql-server')
		if re.search('mysql-server is not installed', result):
			return 'rpm'	# use 'rpm' install mysql-server
		else:
			return 'make'	# use 'make' install mysql-server

def detec_mysql_bin_path(installWay):
	"""
	通过mysqld进程查找bin文件路径
	"""
	if installWay == 'rpm':
		mysqlPath = commands.getoutput('which mysql')
		mysqladminPath = commands.getoutput('which mysql')
	elif installWay == 'make':
		mysqlPath = commands.getoutput("""ps  -ef  | grep  mysqld  
						|  grep  -v  "grep"   |  grep  "bin\/mysqld_safe"  
						|  awk  -F  '/bin/sh'  '{print  $2}'  
						|  awk  '{print  $1}' """)
		return os.path.dirname(mysqlPath)


def detec_my_cnf():
	# editting
	print "MySQL config file is "

def detec_mysql_version(binPath):
	version = commands.getoutput(binPath + '/mysql -V | awk "{print $5}"')
	print "mysql version : %s" % version

def detec_mysql_base_dir():
	"""
	通过mysqld进程查找mysql的base dir文件路径
	"""
	baseDir = commands.getoutput(""" ps  -ef  |  grep  mysql  |  grep -v  "mysqld_safe"   
					| grep -v   "grep"   |  awk  -F  '--basedir='   '{print  $2}'  
					|  awk  '{print $1}' """)
	print "mysql's base dir is : %s " % baseDir
	# /etc/init.d/

def detec_mysql_operate(installWay):
	"""
	检测mysql-server的启动，关闭命令
	根据安装方式的不同，返回不同的结果
	"""
	if installWay == 'rpm':
		return "service mysqld "
	elif installWay == 'apt-get':
		return "/etc/init.d/mysql "
	else:
		return {"stop":"killall -15 mysqld","restart":"killall -1 mysqld"}


def detec_mysql_data_path():
	"""
	通过mysqld进程查找mysql的base dir文件路径
	"""
	dataDir = commands.getoutput(""" ps  -ef  |  grep  mysql  |  grep -v  "mysqld_safe"   
					| grep -v   "grep"  |  awk  -F  '--datadir='  '{print $2}'   
					|  awk  '{print  $1}' """)
	print "MySQL data dir is :%s" % dataDir


def detec_mysql_port():
	"""
	通过mysqld进程查找mysql的base dir文件路径
	"""
	port = commands.getoutput(""" ps  -ef  |  grep  mysql  |  grep -v  "mysqld_safe"   
					| grep -v   "grep"  |  awk  -F  '--port='  '{print  $2}'  
					|  awk   '{print  $1}' """)
	print "MySQL listen port : %s" % port

def detec_mysql_slow_query():
	isOn = commands.getoutput(""" grep   long_query_time  /etc/my.cnf  |  grep  -v  "^#" """)
	if 'long_query_time' in isOn:
		print "isOn is True"
	elif isOn == '':
		print "isOn is False"
	else:
		print "excute shell cmds error"

def detec_mysql_bad_table():
	"""
	检查mysql中是否存在坏表
	"""

################### install ###################

def install_mysql_server(osVersion):
	if osVersion == 'centos' or osVersion == 'redhat':
		subprocess.call('yum install mysql-server mysql-devel -y', shell = True)
	elif osVersion == 'debian' or osVersion == 'ubuntu':
		subprocess.call('apt-get install mysql-server -y ' , shell = True)
	else:
		print " %s is not the supported OS types" % osVersion


##################### configuration #####################

def config_mysql_initialize():
	"""
	mysql-server安装完成后的初始化操作
	"""
	

def config_mysql_datadir_migration():
	"""
	迁移MySQL的数据目录
	"""
	


if __name__ == '__main__':
	#binPath = detec_mysql_bin_path('make')
	#print "binPath is %r" % binPath
	#detec_mysql_version(binPath)
	
