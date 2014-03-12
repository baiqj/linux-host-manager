#!/bin/bash

##############################
#检查MAKE安装的Apache是否加载ssl模块
##############################

updatedb

#查找编译安装apache生成的主配置文件
locate   httpd.conf  |  grep  -v   "\/httpd.conf$"

#判断上个命令执行的返回值，返回非零时退出当前脚本
[ `echo $?` == 0 ] || exit 1

ENV_PATH=../env_config

#查看已加载module中是否包含php

CMD_PATH=`locate  apachectl  | grep "\/apachectl$"  |  grep  -v  "/usr/sbin/apachectl"`

$CMD  -t -D  DUMP_MODULES | awk  '{print $1}' |  grep  "ssl"

#判断上一个命令的返回值，返回"0"表示安装了php模块

if [ `echo  $?` == 0 ] 
then
	sed  -ie  "/Make_ssl/a \'Make_ssl\':\'On\'" $ENV_PATH
else
	sed  -ie  "/Make_ssl/a \'Make_ssl\':\'Off\'" $ENV_PATH
fi
