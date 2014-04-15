#函数名
#函数功能描述
#支持的操作系统
#函数实现方式描述
#函数参数定义
#函数的输出

###############查找类函数##############
#函数名:find_mysql
#函数功能描述:查找mysql的安装路径，确认mysql是否加到了/etc/init.d下面
#支持的操作系统:CentOS
#函数实现方式描述:通过查看mysql的进程信息查找需要的信息

BASE_DIR=`ps  -ef  |  grep  mysql  |  grep -v  "mysqld_safe"   | grep -v   "grep"   |  awk  -F  '--basedir='   '{print  $2}'  |  awk  '{print $1}'`


#示例返回结果：
#编译安装  PATH="/usr/local/mysql/"
#RPM安装   PATH="/usr/"


#判断是否在/etc/init.d/目录中有启动脚本
find   /etc/init.d/   -name   "mysql*"  -a   -perm  +111
[ `echo  $?`  == 0 ] &&  有  || 没有

#函数参数定义:
#函数的输出:mysqld_safe的位置









#函数名:find_my_cnf
#函数功能描述:查找mysql的配置文件my.cnf
#支持的操作系统:CentOS
#函数实现方式描述:在/etc目录下查找my.cnf文件

updatedb
locate  my.cnf  |  grep  "\/etc\/my\.cnf$"

#函数参数定义:
#函数的输出:my.cnf的位置






#函数名:find_mysql_data_path
#函数功能描述:查找mysql的数据目录的位置
#支持的操作系统:CentOS
#函数实现方式描述:通过查看mysql的进程信息,查看datadir的目录设置

DATA_DIR=` ps  -ef  |  grep  mysql  |  grep -v  "mysqld_safe"   | grep -v   "grep"  |  awk  -F  '--datadir='  '{print $2}'   |  awk  '{print  $1}'`

 
#函数参数定义:
#函数的输出:mysql数据目录的位置










#########检测类函数####################
#函数名:detec_mysql_install
#函数功能描述:检测mysql是否安装了
#支持的操作系统:CentOS
#函数实现方式描述:

#通过判断是否存在mysqld_safe命令进行判断是否安装了mysql-server
updatedb
locate   mysqld_safe  | grep  "bin\/mysqld_safe$"

[ `echo  $? == 0` ]  &&  是  ||  否


#函数参数定义:
#函数的输出:是或否













#函数名:detec_mysql_install_way
#函数功能描述:检测mysql的安装方式
#支持的操作系统:CentOS
#函数实现方式描述:通过判断mysqld_safe的存放路径中是否包含mysql关键字来判断安装方式


#此处我们认为编译安装的msyql的路径中是包含mysql的，如 /usr/local/mysql
updatedb
locate   mysqld_safe  | grep  "bin\/mysqld_safe$"  |  awk  -F  'bin/'   '{print  $1}'  |  grep -i  "mysql"

#通过命令的返回值进行判断

[ `echo  $? == 0 ` ]  &&   编译安装  ||  rpm安装


#函数参数定义:
#函数的输出:yum apt-get make















#函数名:detec_mysql_listen
#函数功能描述:检测mysql监听的端口
#支持的操作系统:CentOS
#函数实现方式描述:同过查看mysql的进程信息查看需要的信息


PORT=`ps  -ef  |  grep  mysql  |  grep -v  "mysqld_safe"   | grep -v   "grep"  |  awk  -F  '--port='  '{print  $2}'  |  awk   '{print  $1}'`

#函数参数定义:
#函数的输出:端口号









#函数名:detec_mysql_slow_query
#函数功能描述:检测mysql是否开启了慢查询
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:启用了或未启用






#函数名:detec_mysql_bad_table
#函数功能描述:检测mysql中是否存在坏表
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:是或否，表的名称


#############mysql安装类函数############

#函数名:install_yum_mysql
#函数功能描述:yum方式安装mysql
#支持的操作系统:CentOS
#函数实现方式描述:通过启动mysqld服务验证安装的成功和失败

service  mysqld  start
service  mysqld  status
[ `echo  $?  == 0` ] &&  ok  ||  error

#使用RPM可以查看mysql-server的安装包名称，从中截取版本信息

VERSION=`rpm  -q  mysql-server  |  awk -F "-"   '{print  $3}'`



#启动关闭命令
/etc/init.d/mysqld   start|stop|restart

#函数参数定义:
#函数的输出:安装成功或失败，mysql的版本号，my.cnf的位置，mysql启动关闭程序的位置


#函数名:install_apt_mysql
#函数功能描述:apt-get方式安装mysql
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:安装成功或失败，安装成功或失败，mysql的版本号，my.cnf的位置，mysql启动关闭程序的位置


#函数名:install_make_mysql
#函数功能描述:make方式安装mysql
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:安装成功或失败，安装成功或失败，mysql的版本号，my.cnf的位置，mysql启动关闭程序的位置

