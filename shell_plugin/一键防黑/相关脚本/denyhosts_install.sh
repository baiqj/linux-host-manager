#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

##########################
#用于安装DenyHosts脚本
##########################
#http://ncu.dl.sourceforge.net/sourceforge/denyhosts/DenyHosts-2.6.tar.gz

# 验证当前的用户是否为root账号，不是的话退出当前脚本
[ `id  -u`  == 0 ]  ||  echo "Error: You must be root to run this script, please use root to install lnmp"  ||  exit  1

#检测系统是不是CentOS，如果不是，提醒用户暂时不支持

cat  /etc/issue  |  grep  -iw  "CENTOS"

[ `echo  $?` != 0 ]  &&  exit  1


#判断是否安装了locate工具
rpm  -q  mlocate

[ `echo  $?` != 0 ]  &&  yum  install  -y  mlocate 

updatedb

#判断是否安装了python，默认CentOS 6.3系统已经安装了2.6.6版本
python  -V

if  [  `echo  $?`  != 0 ]
then
#如果系统没有python,则yum安装pathon
	yum  install   -y  python
#编译安装DenyHosts工具
else
	PACKAGE_PATH=`locate  DenyHosts-2.6.tar.gz`
	tar  -zxvf   $PACKAGE_PATH
	cd   ./DenyHosts-2.6
	python   ./setup.py    install
#程序默认的安装目录" /usr/share/denyhosts/"
#创建服务启动脚本文件
	 \cp  /usr/share/denyhosts/daemon-control-dist   /etc/rc.d/init.d/denyhostsd
#赋予脚本可执行权限
	chown root /etc/rc.d/init.d/denyhostsd
	chmod 700 /etc/rc.d/init.d/denyhostsd
#设置开机自动执行	
	chkconfig --add denyhostsd
	chkconfig --level 345 denyhostsd on
#设置配置文件,使用了默认的选项。
	cd    /usr/share/denyhosts/
	grep -v "^#" denyhosts.cfg-dist > denyhosts.cfg
	
#将要阻止的IP放到 /etc/hosts.deny  文件中

#启动服务
	service denyhostsd start

	