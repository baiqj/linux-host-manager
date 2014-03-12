#!/bin/bash

##############################
#检测RPM安装方式的Apache主配置文件中的User配置项信息
##############################

[ `rpm -qa | grep  httpd` ] || exit 1

updatedb

ENV_PATH=../env_config

CONF='/etc/httpd/conf/httpd.conf'

VALUE=`grep  -v  "^#"  $CONF |  grep  -i "User " |  awk  '{print  $2}'`

#查看"Rpm_User"所在的行号

LINE_NUM=`grep  -n  "Rpm_User"   $ENV_PATH  |  awk -F:  '{print $1}'`

#在"Rpm_User"行之后添加一行

sed  -ie  "/Rpm_User/a \'Rpm_User\':\'$VALUE\'" $ENV_PATH

#删除原来的"Rpm_User"行

sed -i  ''$LINE_NUM'd'   $ENV_PATH



