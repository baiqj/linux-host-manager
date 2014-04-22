# -*- encoding:utf-8 -*-
# 原mysql.py 已经被重命名为mysql.py.txt
# 这个文件是参考mysql.py.txt编写端源代码文件

import subprocess
import commands

############# check ################

def detec_mysql_install():
	result = subprocess.Popen('updatedb && locate mysqld_safe | grep "bin\/mysqld_safe$"', shell = True, stdout = subprocess.PIPE)
	if result.stdout == '':
		print "mysql is not installed"
	elif 'bin\/mysqld_safe$' in result.stdout:
		print "mysql is installed"
	else:
		print "excute shell commands error"

def detec_mysql_install_way(osVersion):
	if osVersion == 'centos' or osVersion == 'redhat':
		result = commands.getoutput('rpm -q mysql-server')
		if 'mysql-server' in result:
			print "use 'rpm' install mysql-server"
		else:
			print "use 'make' install mysql-server"

def detec_mysql_bin_path(installWay):
	if installWay == 'rpm':
		mysqlPath = commands.getoutput('which mysql')
		mysqladminPath = commands.getoutput('which mysql')
	elif installWay == 'make':
		mysqlPath = commands.getoutput("""ps  -ef  | grep  mysqld  |  grep  -v  "grep"   |  grep  "bin\/mysqld_safe"  |  awk  -F  '/bin/sh'  '{print  $2}'  |  awk  '{print  $1}' """)
		print " mysql bin files path is %s" % os.path.dirname(mysqlPath)


def detec_my_cnf():
	# editting
	print "MySQL config file is "

def detec_mysql_version():
	version = commands.getoutput('mysql -V | awk "{print $5}"')
	print "mysql version : %s" % version

def detec_mysql_base_dir():
	baseDir = commands.getoutput(""" ps  -ef  |  grep  mysql  |  grep -v  "mysqld_safe"   | grep -v   "grep"   |  awk  -F  '--basedir='   '{print  $2}'  |  awk  '{print $1}' """)
	print "mysql's base dir is : %s " % baseDir
	# /etc/init.d/

def detec_mysql_operate():
	# -------------------
	print "MySQL opertation is "

def detec_mysql_data_path():
	# return MySQL data dir
	dataDir = commands.getoutput(""" ps  -ef  |  grep  mysql  |  grep -v  "mysqld_safe"   | grep -v   "grep"  |  awk  -F  '--datadir='  '{print $2}'   |  awk  '{print  $1}' """)
	print "MySQL data dir is :%s" % dataDir


def detec_mysql_port():
	port = commands.getoutput(""" ps  -ef  |  grep  mysql  |  grep -v  "mysqld_safe"   | grep -v   "grep"  |  awk  -F  '--port='  '{print  $2}'  |  awk   '{print  $1}' """)
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
	#---------------------------
	print "mysql bad tables is "


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
	#----------------------------
	print "finish mysql initialize"

def config_mysql_datadir_migration():
	#--------------------------
	print "move mysql data dir"



if __name__ == '__main__':
	print "excute main()"
