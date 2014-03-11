#!/bin/bash

##############################
#检测Apache的安装方式rpm或者make
##############################
updatedb

ENV_PATH=../env_config

#判断rpm方式的conf文件是否存在

RPM=`locate   "/etc/httpd/conf/httpd.conf" | wc -l`

#判断make方式的conf文件是否存在

MAKE=`locate  "httpd.conf"  | grep  "\/httpd.conf$"  |  grep -v "etc/httpd/conf/httpd.conf" | wc -l`


locate  "httpd.conf"  | grep  "\/httpd.conf$"  

if  [ `echo $?`  == 0  ] 
then
	if [ $RPM  == 1 -a  $MAKE == 0 ] 
	then
		sed -i  "/'Apache_Install_Way':/s/$/\'Rpm\'/"  $ENV_PATH
	fi
	if [ $RPM == 0 -a  $MAKE == 1 ]
	then
		sed -i  "/'Apache_Install_Way':/s/$/\'\Make\'/"  $ENV_PATH
	fi
	if [ $RPM == 1 -a $MAKE == 1 ]
	then
		sed -i  "/'Apache_Install_Way':/s/$/\'\Rpm|Make\'/"  $ENV_PATH
	fi
else	
	sed -i  "/'Apache_Install_Way':/s/$/\'\Not\'/"  $ENV_PATH
fi


