#!/bin/bash

##############################
#检测MAKE安装方式的Apache主配置文件中的LogLevel配置项信息
##############################

updatedb

ENV_PATH=../env_config

#判断是否有make编译生成的httpd.conf配置文件，没有的话则退出脚本
locate  httpd.conf  |  grep  "\/httpd.conf$"  | grep -v   "/etc/httpd/conf/httpd.conf" 

[ `echo $?` == 0 ]  ||  exit 1


CONF=`locate  httpd.conf  |  grep  "\/httpd.conf$"  | grep -v   "/etc/httpd/conf/httpd.conf"`

VALUE=`grep  -v  "^#"  $CONF |  grep  -i "LogLevel " |  awk  '{print  $2}'`

#查看"Rpm_LogLevel"所在的行号

LINE_NUM=`grep  -n  "Rpm_LogLevel"   $ENV_PATH  |  awk -F:  '{print $1}'`

#在"Rpm_LogLevel"行之后添加一行

sed  -ie  "/Rpm_LogLevel/a \'Rpm_LogLevel\':\'$VALUE\'" $ENV_PATH

#删除原来的"Rpm_LogLevel"行

sed -i  ''$LINE_NUM'd'   $ENV_PATH



