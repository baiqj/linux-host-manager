#!/bin/bash

##############################
#检测Rpm安装方式Apache的安装目录
##############################
updatedb

ENV_PATH=../env_config

CONF_PATH="/etc/httpd/conf/httpd.conf"

DOCUMENT_PATH=`grep  -i  "ServerRoot "   /etc/httpd/conf/httpd.conf  | grep -v "^#" |  awk   '{print  $2}'`

LINE_NUM=`grep  -n  "Rpm_Installation_Directory"   $ENV_PATH  |  awk -F:  '{print $1}'`

#在"Rpm_Installation_Directory"行之后添加一行

sed  -ie  "/Rpm_Installation_Directory/a \'Rpm_Installation_Directory\':\'$DOCUMENT_PATH\'"   $ENV_PATH

#删除原来的"Rpm_Installation_Directory"行

sed -i  ''$LINE_NUM'd'   $ENV_PATH
