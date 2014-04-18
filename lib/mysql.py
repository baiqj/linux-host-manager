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
函数实现方式描述:如果msyql-server已经安装，使用rpm -q查询，能够查到就是rpm安装，不能查到就是make安装

rpm  -q   mysql-server
[ `echo $?`  == 0 ]  &&  rpm安装  || make 安装




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

rpm安装方式：which  mysql  ； which   mysqladmin  ;which  mysqlbug  ; which mysqld_safe
make安装方式：   

ps  -ef  | grep  mysqld  |  grep  -v  "grep"   |  grep  "bin\/mysqld_safe"  |  awk  -F  '/bin/sh'  '{print  $2}'  |  awk  '{print  $1}'

返回结果：
/usr/local/mysql/bin/mysqld_safe
备注：其他的命令和mysqld_safe在同一个目录中




*************************
1.4检测mysql的配置文件路径
*************************

文件：mysql.py
函数：检测类 ：detec_my_cnf
函数功能描述：查找mysql的配置文件的路径
支持的操作系统:
输入参数：从detec_mysql_install函数获取输出参数，yes|no判断是否安装了mysql-server
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_mysql_install_way函数获取输出参数，mysql的安装方式（rpm|make|apt-get）
输入参数：输出有效的my.cnf的路径
函数实现方式描述:通过mysqlbug查看mysql-server安装时的参数

export VISUAL=cat
mysqlbug | grep -i "config"



*************************************
1.5检测已安装mysql-server的安装版本
*************************************

文件：mysql.py
函数：检测类 ：detec_mysql_version
函数功能描述：检测mysql-server的安装版本
支持的操作系统:
输入参数：从detec_mysql_install函数获取输出参数，yes|no判断是否安装了mysql-server
		  从detec_mysql_bin_path函数获取mysql命令路径
输出参数：输出mysql-server的版本
函数实现方式描述:使用msyql  -V可以得到mysql-server的版本信息

mysql   -V



***************************************
1.6检测mysql-server的安装目录base-dir
****************************************

文件：mysql.py
函数：查找类 ：detec_mysql_base_dir
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
detec   /etc/init.d/   -name   "mysql*"  -a   -perm  +111
[ `echo  $?`  == 0 ] &&  有  || 没有



****************************************
1.7检测mysql-server的启动、关闭命令
****************************************

文件：mysql.py
函数：检测类 ：detec_apache_operate
函数功能描述:检测msyql-server的启动、关闭命令
支持的操作系统:
输入参数：从detec_mysql_install函数获取输出参数，yes|no判断是否安装了mysql-server
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_mysql_install_way函数获取输出参数，mysql的安装方式（rpm|make|apt-get）
输出参数：输出mysql-server的启动、关闭命令
函数实现方式描述：

rpm安装方式：service   mysqld   start|stop
make安装方式：	killall  -15  mysqld   关闭
				killall  -1  mysqld 	重启



*********************************
1.8检测msyql-server的数据目录的路径
*********************************

文件：mysql.py
函数：检测类 ：detec_mysql_data_path
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
函数实现方式描述:需要检测配置文件中的设置是否在[mysqld]字段中有long_query_time关键字

grep   long_query_time  /etc/my.cnf  |  grep  -v  "^#"


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

#!/bin/bash
02
#此脚本的主要用途是检测mysql服务器上所有的db或者单独db中的坏表
03
#变量说明 pass mysql账户口令 name mysql账号名称 data_path mysql目录路径 directory_list 目录列表 file_list文件列表 db_name 数据库名称 repair_count单库中待修复的表总数
04
#变量说明 repair_count_all所有库中待修复的表总数 mysql_version mysql版本 _file_name 数据表名称
05
 
06
echo -e "此脚本的主要用途是检测mysql服务器上所有的数据库或者单独数据库中的坏表\n\n"
07
pass=123456
08
name=root
09
 
10
read -p "输入mysql存储路径: "  choose
11
data_path=$choose
12
unset choose
13
 
14
read -p "请输入mysql命令路径: " mysql_version
15
#标准输入、标准输出、标准错误输出的文件标示符 由 0、1、2标识
16
read -p "请选择是检查服务器上所有数据库还是指定的数据库 1:检查全部数据库 2:只检查指定数据库: " choose
17
if [ $choose == 1 ]; then
18
  cd $data_path
19
  for directory_list in $(ls)
20
    do
21
      if [ -d $directory_list ];then
22
          if [ "mysql" != "${directory_list}" -a "test" != "${directory_list}" ];then
23
              cd ${directory_list}
24
              echo "当前检查数据库为:"${directory_list}
25
              for file_list in $(ls *.frm)
26
              do
27
                _file_name=${file_list%.frm}
28
                echo -e "\n" >> /tmp/check_table_all.log
29
                ${mysql_version} -h 127.0.0.1 -u${name} -p${pass} -e "check table "${directory_list}.${_file_name} 2>&1 >> /tmp/check_table_all.log
30
              done
31
              cd ..
32
          fi
33
      fi
34
  done
35
             cat /tmp/check_table_all.log | grep "Table is marked as crashed" > /tmp/check_table_repair.log
36
             repair_count_all=` awk 'END{print NR}' /tmp/check_table_repair.log `
37
             echo -e "所有数据库用有${repair_count_all}张表需要修复！"
38
             more  /tmp/check_table_repair.log
39
else
40
  read -p "请输入要检查的数据库名称: " db_name
41
  cd ${data_path}/${db_name}
42
  for file_list in $(ls *.frm)
43
    do
44
      _file_name=${file_list%.frm}
45
      echo -e "\n" >> /tmp/check_${db_name}.log
46
      ${mysql_version} -h 127.0.0.1 -u${name} -p${pass} -e "check table "${db_name}.$_file_name 2>&1 >> /tmp/check_${db_name}.log
47
    done
48
    cat /tmp/check_${db_name}.log | grep "Table is marked as crashed" > /tmp/check_${db_name}_Repair.log   
49
    repair_count=`awk 'END{print NR}' /tmp/check_${db_name}_Repair.log`
50
    echo -e "${db_name}中共有${repair_count}个表需要修复！\n "
51
    more /tmp/check_${db_name}_Repair.log                                
52
fi


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
		  从detec_apache_operate函数获取mysql-server的启动、关闭命令
		  从detec_mysql_data_path函数获取mysql-server的数据目录（用于数据的迁移）
输出参数：安装成功或失败，mysql的版本号，my.cnf的位置，mysql启动关闭程序的位置，mysql和mysqladmin命令路径
函数实现方式描述:

yum  install  mysql-server  mysql-devel  -y

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
		  从detec_apache_operate函数获取mysql-server的启动、关闭命令
		  从detec_mysql_data_path函数获取mysql-server的数据目录（用于数据的迁移）
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
1.2mysql-server数据目录的迁移
*************************************

文件：msyql.py
函数：config_mysql_datadir_migration
输入参数:
输出参数：
函数实现方式描述:

1.停掉mysql              service mysqld stop 
2.移动数据文件到新目录下 mv /var/lib/mysql /data/sas0/ 
3.连接目录 cd /var/lib/ ln -s /data/sas0/mysql 
4.启动数据库 service mysqld start