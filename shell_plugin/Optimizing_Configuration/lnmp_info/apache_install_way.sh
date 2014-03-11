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
	 sed -i  "/'Apache_Install':/s/$/\'On\'/"  $ENV_PATH
else
	 sed -i  "/'Apache_Install':/s/$/\'Off\'/"  $ENV_PATH
fi

