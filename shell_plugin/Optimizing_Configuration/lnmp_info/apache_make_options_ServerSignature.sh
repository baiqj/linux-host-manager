#!/bin/bash

##############################
#检测MAKE安装方式的Apache主配置文件中的ServerSignature配置项信息
##############################

updatedb

ENV_PATH=../env_config

#判断是否有make编译生成的httpd.conf配置文件，没有的话则退出脚本
locate  httpd.conf  |  grep  "\/httpd.conf$"  | grep -v   "/etc/httpd/conf/httpd.conf" 

[ `echo $?` == 0 ]  ||  exit 1


CONF=`locate  httpd.conf  |  grep  "\/httpd.conf$"  | grep -v   "/etc/httpd/conf/httpd.conf"`

VALUE=`grep  -v  "^#"  $CONF |  grep  -i "ServerSignature " |  awk  '{print  $2}'`

#查看"Rpm_ServerSignature"所在的行号

LINE_NUM=`grep  -n  "Rpm_ServerSignature"   $ENV_PATH  |  awk -F:  '{print $1}'`

#在"Rpm_ServerSignature"行之后添加一行

sed  -ie  "/Rpm_ServerSignature/a \'Rpm_ServerSignature\':\'$VALUE\'" $ENV_PATH

#删除原来的"Rpm_ServerSignature"行

sed -i  ''$LINE_NUM'd'   $ENV_PATH



