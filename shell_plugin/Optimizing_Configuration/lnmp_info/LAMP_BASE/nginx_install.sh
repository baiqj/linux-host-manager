#!/bin/bash

##############################
#检测Nginx是否已经安装
##############################
updatedb

ENV_PATH=../env_config

#判断Nginx的主配置文件是否存在,不存在则退出当前脚本

locate   "nginx.conf"  |  grep  -i  "\/conf\/nginx\.conf$" |    grep  -vi "\/doc"  |  grep  -vi  "\/share\/"  |  grep -vi  "ln*mp*"  

[ `echo  $?` == 0 ] ||  exit 1

#查看编译安装的apache的主配置文件的路径

locate   "nginx.conf"  |  grep  -i  "\/conf\/nginx\.conf$" |   grep  -vi "\/doc"  |  grep  -vi  "\/share\/"  |  grep -vi  "ln*mp*"  

if  [ `echo $?`  == 0  ] 
then
	 sed -i  "/'Nginx_Install':/s/$/\'On\'/"  $ENV_PATH
else
	 sed -i  "/'Nginx_Install':/s/$/\'Off\'/"  $ENV_PATH
fi

