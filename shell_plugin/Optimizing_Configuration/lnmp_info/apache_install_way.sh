#!/bin/bash

##############################
#检测Apache的安装方式rpm或者make
##############################
updatedb

ENV_PATH=../env_config

#判断Apache的主配置文件是否存在

locate  "httpd.conf"  |  grep  "httpd.conf$"

if  [ `echo $?`  == 0  ] 
then
	if [ rpm  -qa  |  grep  httpd ] 
	then
		sed -i  "/'Apache_Install_Way':/s/$/\'Rpm\'/"  $ENV_PATH
	else
		sed -i  "/'Apache_Install_Way':/s/$/\'\Make\'/"  $ENV_PATH
	fi
else	
	sed -i  "/'Apache_Install_Way':/s/$/\'\Not\'/"  $ENV_PATH
fi


