#!/bin/bash

##############################
#检测Rpm安装方式Nginx的重新加载命令
##############################

updatedb

ENV_PATH=../env_config

#判断是否有rpm方式安装的nginx，没有的话退出该脚本

[ `rpm -qa | grep  nginx` ] ||  exit 1

#查看nginx命令路径

CMD=`rpm  -ql  nginx  |  grep  "\/nginx$"  |  grep  -E  "/usr/sbin/|/usr/bin/"`


LINE_NUM=`grep  -n  "Nginx_Rpm_Reload_Cmd"   $ENV_PATH  |  awk -F:  '{print $1}'`

#在"Nginx_Rpm_Reload_Cmd"行之后添加一行

sed  -ie  "/Nginx_Rpm_Reload_Cmd/a \'Nginx_Rpm_Reload_Cmd\':\'"'$CMD -s  reload'"\'"   $ENV_PATH

#删除原来的"Nginx_Rpm_Reload_Cmd"行

sed -i  ''$LINE_NUM'd'   $ENV_PATH



