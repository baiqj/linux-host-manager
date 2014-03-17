#!/bin/bash

##############################
#检测mysql是否已经安装
##############################
updatedb

ENV_PATH=../env_config

#判断mysql的主配置文件是否存在

if  [ -f  /etc/my.cnf  ] 
then
	 sed -i  "/'MySql_Install':/s/$/\'On\'/"  $ENV_PATH
else
	 sed -i  "/'MySql_Install':/s/$/\'Off\'/"  $ENV_PATH