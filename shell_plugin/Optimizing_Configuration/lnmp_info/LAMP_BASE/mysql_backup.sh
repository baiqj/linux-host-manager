#!/bin/bash

updatedb

ENV_PATH=../../env_config

#查看mysql是否在运行，正在运行的话退出当前脚本
ps  -ef  |  grep  mysql  |  grep  -v  "grep" 

[ `echo  $?` == 0 ] &&  exit  1

#创建原有的mysql的备份目录
mkdir -p  /usr/local/mysql3307
chmod +w /usr/local/mysql3307
chown -R mysql:mysql /usr/local/mysql3307

#需要查找mysql的安装目录
DOCUMENT=`locate  mysqladmin  |  grep "\/mysqladmin$"   | grep "mysql"  | grep  "\/bin\/"  |  awk -F "/bin"   '{print  $1}'`

#复制mysql文件并保存属性
\cp  -rpv  $DOCUMENT/*    /usr/local/mysql3307/

\cp  -rpv /etc/my.cnf    /usr/local/mysql3307/var/my_3307.cnf

#删除所有的注释行
 sed  -i   '/#/d'  /usr/local/mysql3307/var/my_3307.cnf
#删除所有的空行
 sed  -i   '/^$/d'  /usr/local/mysql3307/var/my_3307.cnf
 

#需要判断是否设置了datadir目录

DATADIR=`grep   '\[mysqld\]'  -A4   /usr/local/mysql3307/var/my_3307.cnf   |  grep  "datadir" | awk -F "="  '{print $2}'`




if  [ `echo  $?` != 0 ]
then
#没有设置datadir参数
	sed -e "/^\[mysqld\]$/a  datadir = /usr/local/mysql3307/var " -i      /usr/local/mysql3307/var/my_3307.cnf
else
#设置了datadir参数
	sed  -i  "/datadir/s/^/#/"   /usr/local/mysql3307/var/my_3307.cnf
	sed -e "/^\[mysqld\]$/a  datadir = /usr/local/mysql3307/var " -i      /usr/local/mysql3307/var/my_3307.cnf
 
 设置为默认的话，需要修改
 设置为非默认的话，保持原状即可
 
 
sed -e '/datadir  /a 11111' -i      /etc/httpd/conf/httpd.conf

