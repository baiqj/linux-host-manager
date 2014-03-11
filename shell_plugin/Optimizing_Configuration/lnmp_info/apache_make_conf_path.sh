#!/bin/bash

##############################
#检测Make安装方式Apache主配置文件的路径
##############################
updatedb

ENV_PATH=../env_config

#判断是否存在Make编译安装的Apahce主配置文件，没有的话退出本脚本

locate  "httpd.conf"  |  grep  "\/httpd.conf$"  |  grep  -v  "/etc/httpd/conf/httpd.conf"

[ `echo  $?` == 0 ] ||  exit 1

#查看编译安装的apache的主配置文件的路径

CONF_PATH=`locate  "httpd.conf"  |  grep  "\/httpd.conf$"  |  grep  -v  "/etc/httpd/conf/httpd.conf"`


LINE_NUM=`grep  -n  "Make_Conf_Path"   $ENV_PATH  |  awk -F:  '{print $1}'`

#在"Make_Conf_Path"行之后添加一行

sed  -ie  "/Make_Conf_Path/a \'Make_Conf_Path\':\'$CONF_PATH\'"   $ENV_PATH

#删除原来的"Make_Conf_Path"行

sed -i  ''$LINE_NUM'd'   $ENV_PATH



