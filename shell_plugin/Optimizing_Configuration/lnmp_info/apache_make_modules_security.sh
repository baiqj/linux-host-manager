#!/bin/bash

##############################
#检查MAKE安装的Apache是否加载security模块
##############################

updatedb

#查找编译安装apache生成的主配置文件
locate   httpd.conf  |  grep  -v   "\/httpd.conf$"

#判断上个命令执行的返回值，返回非零时退出当前脚本
[ `echo $?` == 0 ] || exit 1

ENV_PATH=../env_config

#查看已加载module中是否包含php

CMD_PATH=`locate  apachectl  | grep "\/apachectl$"  |  grep  -v  "/usr/sbin/apachectl"`

$CMD  -t -D  DUMP_MODULES | awk  '{print $1}' |  grep  "security"

#判断上一个命令的返回值，返回"0"表示安装了php模块

if [ `echo  $?` == 0 ] 
then
	sed  -ie  "/Make_mod_security/a \'Make_mod_security\':\'On\'" $ENV_PATH
else
	sed  -ie  "/Make_mod_security/a \'Make_mod_security\':\'Off\'" $ENV_PATH
fi
