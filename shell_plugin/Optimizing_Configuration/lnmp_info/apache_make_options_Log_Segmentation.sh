#!/bin/bash

##############################
#检查MAKE安装的Apache是否启用日志分割
##############################
updatedb

ENV_PATH=../env_config

#判断是否有make编译生成的httpd.conf配置文件，没有的话则退出脚本
locate  httpd.conf  |  grep  "\/httpd.conf$"  | grep -v   "/etc/httpd/conf/httpd.conf" 

[ `echo $?` == 0 ]  ||  exit 1


CONF=`locate  httpd.conf  |  grep  "\/httpd.conf$"  | grep -v   "/etc/httpd/conf/httpd.conf"`

#查看已加载ErrorLog设置中是否包含rotatelogs命令

/grep   -v  "^#"  $CONF  |  grep  -wi  "errorlog"  | grep  -iw  "rotatelogs"

#判断上一个命令的返回值，返回"0"表示安装了日志分割工具

if [ `echo  $?` == 0 ] 
then
	sed  -ie  "/Make_Log_Segmentation/a \'Make_Log_Segmentation\':\'On\'"  $ENV_PATH
else
	sed  -ie  "/Make_Log_Segmentation/a \'Make_Log_Segmentation\':\'Off\'" $ENV_PATH
fi
