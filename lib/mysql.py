#函数名
#函数功能描述
#支持的操作系统
#函数实现方式描述
#函数参数定义
#函数的输出


###############第一、检测类函数##############

********************************
1.1检测是否安装了mysql-server
********************************

文件：mysql.py
函数：检测类 ：detec_mysql_install
函数功能描述:检测mysql是否安装了
支持的操作系统:
输入参数：从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
输出参数：mysql-server是否已经安装，yes|no
函数实现方式描述:通过判断是否存在mysqld_safe命令进行判断否安装了mysql-server


updatedb
locate   mysqld_safe  | grep  "bin\/mysqld_safe$"

[ `echo  $? == 0` ]  &&  是  ||  否




***********************************
1.2检测已安装msyql-server的安装方式
***********************************

文件：mysql.py
函数：检测类 ：detec_mysql_install_way
函数功能描述:检测mysql的安装方式
支持的操作系统:
输入参数：从detec_mysql_install函数获取输出参数，yes|no判断是否安装了mysql-server
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
输出参数：输出mysql-server的安装方式（rpm|make|apt-get）
函数实现方式描述:通过判断mysqld_safe的存放路径中是否包含mysql关键字来判断安装方式

#此处我们认为编译安装的msyql的路径中是包含mysql的，如 /usr/local/mysql
updatedb
locate   mysqld_safe  | grep  "bin\/mysqld_safe$"  |  awk  -F  'bin/'   '{print  $1}'  |  grep -i  "mysql"

#通过命令的返回值进行判断

[ `echo  $? == 0 ` ]  &&   编译安装  ||  rpm安装







*************************
1.3检测mysql和mysqladmin命令的路径
*************************

文件：mysql.py
函数：检测类 ：detec_mysql_bin_path
函数功能描述：查找mysql和mysqladmin的路径
支持的操作系统:
输入参数：从detec_mysql_install函数获取输出参数，yes|no判断是否安装了mysql-server
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_mysql_install_way函数获取输出参数，mysql的安装方式（rpm|make|apt-get）
输入参数：输出mysql和mysqladmin的命令的路径
函数实现方式描述:



*************************
1.4检测mysql的配置文件路径
*************************

文件：mysql.py
函数：检测类 ：find_my_cnf
函数功能描述：查找mysql的配置文件的路径
支持的操作系统:
输入参数：从detec_mysql_install函数获取输出参数，yes|no判断是否安装了mysql-server
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_mysql_install_way函数获取输出参数，mysql的安装方式（rpm|make|apt-get）
输入参数：输出有效的my.cnf的路径
函数实现方式描述:配置文件的路径的优先顺序 /etc/my.cnf ； /etc/mysql/my.cnf ；/usr/local/mysql/etc/my.cnf ； ~/.my.cnf

#函数实现方式描述:在/etc目录下查找my.cnf文件

updatedb
locate  my.cnf  |  grep  "\/etc\/my\.cnf$"


*************************************
1.5检测已安装mysql-server的安装版本
*************************************

文件：mysql.py
函数：检测类 ：detec_mysql_version
函数功能描述：检测mysql-server的安装版本
支持的操作系统:
输入参数：从detec_mysql_install函数获取输出参数，yes|no判断是否安装了mysql-server
		  从find_mysql_bin_path函数获取mysql命令路径
输出参数：输出mysql-server的版本
函数实现方式描述:使用msyql  -V可以得到mysql-server的版本信息


***************************************
1.6检测mysql-server的安装目录base-dir
****************************************

文件：mysql.py
函数：查找类 ：find_mysql_base_dir
函数功能描述:查找mysql的安装路径，确认mysql是否加到了/etc/init.d下面
支持的操作系统:
输入参数：从detec_mysql_install函数获取输出参数，yes|no判断是否安装了mysql-server
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_mysql_install_way函数获取输出参数，mysql的安装方式（rpm|make|apt-get）
输出参数：输出mysql-server的安装目录
函数实现方式描述:通过查看mysql的进程信息查找需要的信息

BASE_DIR=`ps  -ef  |  grep  mysql  |  grep -v  "mysqld_safe"   | grep -v   "grep"   |  awk  -F  '--basedir='   '{print  $2}'  |  awk  '{print $1}'`


#示例返回结果：
#编译安装  PATH="/usr/local/mysql/"
#RPM安装   PATH="/usr/"


#判断是否在/etc/init.d/目录中有启动脚本
find   /etc/init.d/   -name   "mysql*"  -a   -perm  +111
[ `echo  $?`  == 0 ] &&  有  || 没有



****************************************
1.7检测mysql-server的启动、关闭命令
****************************************

文件：mysql.py
函数：检测类 ：find_apache_operate
函数功能描述:检测msyql-server的启动、关闭命令
支持的操作系统:
输入参数：从detec_mysql_install函数获取输出参数，yes|no判断是否安装了mysql-server
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_mysql_install_way函数获取输出参数，mysql的安装方式（rpm|make|apt-get）
输出参数：输出mysql-server的启动、关闭命令
函数实现方式描述：


*********************************
1.8检测msyql-server的数据目录的路径
*********************************

文件：mysql.py
函数：检测类 ：find_mysql_data_path
函数功能描述:查找mysql的数据目录的位置
支持的操作系统:
输入参数：从detec_mysql_install函数获取输出参数，yes|no判断是否安装了mysql-server
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_mysql_install_way函数获取输出参数，mysql的安装方式（rpm|make|apt-get）
输出参数：输出msyql-server的数据目录的路径
函数实现方式描述:通过查看mysql的进程信息,查看datadir的目录设置

DATA_DIR=` ps  -ef  |  grep  mysql  |  grep -v  "mysqld_safe"   | grep -v   "grep"  |  awk  -F  '--datadir='  '{print $2}'   |  awk  '{print  $1}'`

 


*********************************
1.9检测msyql-server的监听端口
*********************************

文件：mysql.py
函数：检测类 ：detec_mysql_data_path
函数功能描述:检测mysql监听的端口
支持的操作系统:
输入参数：从detec_mysql_install函数获取输出参数，yes|no判断是否安装了mysql-server
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_mysql_install_way函数获取输出参数，mysql的安装方式（rpm|make|apt-get）
输出参数：输出msyql-server的监听端口
函数实现方式描述:同过查看mysql的进程信息查看需要的信息


PORT=`ps  -ef  |  grep  mysql  |  grep -v  "mysqld_safe"   | grep -v   "grep"  |  awk  -F  '--port='  '{print  $2}'  |  awk   '{print  $1}'`



*********************************
1.10检测msyql-server是否开启了慢查询
*********************************

文件：mysql.py
函数：检测类 ：detec_mysql_slow_query
函数功能描述:检测mysql是否开启了慢查询
支持的操作系统:
输入参数：从detec_mysql_install函数获取输出参数，yes|no判断是否安装了mysql-server
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_mysql_install_way函数获取输出参数，mysql的安装方式（rpm|make|apt-get）
输出参数：yes|no
函数实现方式描述:需要检测配置文件中的设置



*********************************
1.11检测msyql-server是否存在了坏表
*********************************

文件：mysql.py
函数：检测类 ：detec_mysql_bad_table
函数功能描述:检测mysql中是否存在坏表
支持的操作系统:
输入参数：从detec_mysql_install函数获取输出参数，yes|no判断是否安装了mysql-server
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_mysql_install_way函数获取输出参数，mysql的安装方式（rpm|make|apt-get）
输出参数：是或否，表的名称
函数实现方式描述:



#############第二、mysql安装类函数############



*****************************
1.1rpm安装mysql-server
*****************************

文件：mysql.py
函数：install_yum_mysql
函数功能描述:yum方式安装mysql
支持的操作系统:CentOS
输入参数：从detec_mysql_install函数获取输出参数，yes|no判断是否安装了mysql-server
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从find_apache_operate函数获取mysql-server的启动、关闭命令
		  从find_mysql_data_path函数获取mysql-server的数据目录（用于数据的迁移）
输出参数：安装成功或失败，mysql的版本号，my.cnf的位置，mysql启动关闭程序的位置，mysql和mysqladmin命令路径
函数实现方式描述:

service  mysqld  start
service  mysqld  status
[ `echo  $?  == 0` ] &&  ok  ||  error

#使用RPM可以查看mysql-server的安装包名称，从中截取版本信息

VERSION=`rpm  -q  mysql-server  |  awk -F "-"   '{print  $3}'`



#启动关闭命令
/etc/init.d/mysqld   start|stop|restart



*****************************
1.2apt安装mysql-server
*****************************

文件：mysql.py
函数：install_apt_mysql
函数功能描述:apt-get方式安装mysql
支持的操作系统:
输入参数：从detec_mysql_install函数获取输出参数，yes|no判断是否安装了mysql-server
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从find_apache_operate函数获取mysql-server的启动、关闭命令
		  从find_mysql_data_path函数获取mysql-server的数据目录（用于数据的迁移）
输出参数：安装成功或失败，mysql的版本号，my.cnf的位置，mysql启动关闭程序的位置，mysql和mysqladmin命令路径
函数实现方式描述:



#############第三、mysql操作配置函数############


*************************************
1.1mysql-server安装完成后的初始化操作
*************************************

文件：msyql.py
函数：config_mysql_initialize
输入参数：从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从install_*_mysql获取参数，判断是否安装成功，mysql和mysqladmin命令路径，以及启动关闭命令
		  从config.list获取mysql的root管理员密码，默认mysql是没有设置密码的
输出参数：是否执行了初始化操作yes|no
函数实现方式描述:对mysql数据库进行安全初始化



*************************************
1.2mysql-server数据的迁移
*************************************



函数实现方式描述: