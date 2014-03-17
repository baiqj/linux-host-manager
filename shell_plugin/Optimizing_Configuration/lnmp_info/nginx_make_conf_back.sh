#!/bin/bash

##############################
#make安装方式NGINX的主配置文件的备份
##############################
updatedb

ENV_PATH=../env_config

#判断nginx是否为rpm方式安装
rpm  -q  nginx
[ `echo  $?` ] ||  exit  1

#查看make编译安装的nginx命令路径

CMD=`locate nginx   |  grep  "\/nginx$"    |  grep   -i  "\/*nginx*\/"`

#判断是否存在编译安装生成的nginx命令文件，没有的话退出当前脚本
[  `echo  $?`  ==  0 ]   ||  exit  1

#查看nginx编译时的参数

$CMD  -V  &>   ./cache.tmp


#查看编译安装的主配置文件的路径

DOCUMENT=`cat  ./cache.tmp  |   grep  -i "configure *arguments"  |  awk -F '--prefix='  '{print $2}'  |  awk  '{print  $1}'`

CONF=`locate  "nginx.conf"  |  grep  "$DOCUMENT"   | grep  "\/conf\/" | grep  "\/nginx.conf$"`

rm  -rf   ./cache.tmp


#判断是否存在"CONF_BACK"目录

if  [ -d   CONF_BACK  ]
then	
	
else
	mkdir  ./CONF_BACK
if

\cp     $CONF     .\CONG_BACK


