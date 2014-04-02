#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH
#检测执行的用户是否为root，不是root则提醒用户使用root用户操作

[ `id  -u`  == 0 ]  ||  echo "Error: You must be root to run this script, please use root to install lnmp"  ||  exit  1

#检测系统是不是CentOS，如果不是，提醒用户暂时不支持

cat  /etc/issue  |  grep  -iw  "CENTOS"

[ `echo  $?` != 0 ]  &&  exit  1


#1、安装apache httpd.x86_64并启动
yum -y install httpd httpd-tools   mod_proxy_html  mod_ssl  mod_security

service  httpd   start

#2、安装mysql并启动
yum -y install mysql mod_auth_mysql mysql-connector-odbc mysql-server  mysql-utilities

service   mysqld    start

#3、mysql初始化设置

#3.1配置mysql的初始root登录密码

#使用python程序生成config.list，用于存放mysql的root密码.
#config.list的格式见样本
yum   install  mlocate   -y  
updatedb
CONFIG=`locate  config.list`

mysqlrootpwd=`grep  -i  "mysqlrootpwd"  $CONFIG |  awk  -F ":"  '{print  $2}'`
mysqladmin -u root password $mysqlrootpwd

#3.2生成mysql配置文件
mv /etc/my.cnf /etc/my.cnf.bak
\cp  /usr/share/mysql/my-medium.cnf   /etc/my.cnf
sed -i 's/skip-locking/skip-external-locking/g' /etc/my.cnf

#3.3对mysql进行安全初始化

cat > /tmp/mysql_sec_script<<EOF
use mysql;
delete from user where not (user='root') ;
delete from user where user='root' and password=''; 
drop database test;
DROP USER ''@'%';
flush privileges;
EOF

mysql -u root -p$mysqlrootpwd -h localhost < /tmp/mysql_sec_script

rm -f /tmp/mysql_sec_script

service  mysqld   restart

#3.4更该默认的data目录
#/tmp/.mount.list是由initialize_disk.sh脚本生成的

if  [ -f  /tmp/.mount.list ]  
then
	DATA_DISK=`cat   /tmp/.mount.list`   
#停止mysql服务
	service  mysqld      stop
#创建mysql的数据目录
	echo "更改mysql的数据目录到`echo $DATA_DISK/mysqldata`"
	mkdir   -p   $DATA_DISK/mysqldata
#迁移mysql的数据目录
	\cp  -rpv   /var/lib/mysql/*   $DATA_DISK/mysqldata
	mv 		/var/lib/mysql/  	/var/lib/mysql/data_bak
#创建默认数据目录的软连接
	ln  -s   $DATA_DISK/mysqldata     /var/lib/mysql/
#更改数据目录的属主和属组
	chown   mysql.mysql     $DATA_DISK/mysqldata
#重新启动mysql服务
	service  mysqld      stop
else
#没有额外的磁盘，所以mysql的数据目录并没有迁移
	echo  "datadir=/var/lib/mysql/"
fi


#4、安装php
#默认会自动安装加载apache的php模块
yum -y install php php-mysql  php-process php-pecl-memcache php-bcmath php-mcrypt php-soap  php-mbstring  mhash-devel mhash libmcrypt  libmcrypt-devel  php-imap php-gd php-fpm php-intl php-xml php-xmlrpc php-devel  php-ZendFramework-Db-Adapter-Pdo-Mysql 

#检测系统的版本，根据不同的版本执行不同的命令
releasever=`cat  /etc/issue  |  grep  -iw  "CENTOS"  |  awk  '{print  $3}' |  awk  -F  '.'   '{print  $1}'`

if  [ $releasever == 5 ]
then
	yum  -y install   php53   php53-bcmath  php53-mssql  php53-process  php53-mcrypt  php53-devel  php53-gd  php53-imap  php53-mbstring   php53-pdo  php53-soap   php53-xml  php53-xmlrpc   php53-intl  php53-enchant  php53-php-gettext  php53-pspell mhash-devel mhash  libmcrypt  libmcrypt-devel
else
	if  [ $releasever == 6 ]
	then
		yum -y install php   php-bcmath	 php-mysql  php-process    php-mcrypt   php-devel  php-gd       php-imap    php-mbstring     php-pdo   php-soap   php-xml php-xmlrpc   php-intl      php-enchant   php-php-gettext    php-pspell   mhash-devel mhash   libmcrypt  libmcrypt-devel  php-fpm    
	else
		exit 1
	fi
fi

#查看php编译的模块"php  -m "


#5、重新启动服务

service  httpd restart
service  mysqld   restart

chkconfig   httpd   on
chkconfig  mysqld   on
