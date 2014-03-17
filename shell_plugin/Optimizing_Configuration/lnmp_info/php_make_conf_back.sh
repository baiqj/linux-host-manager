#!/bin/bash

##############################
#make安装方式PHP的主配置文件的备份
##############################
updatedb

ENV_PATH=../env_config

#判断apache是否为rpm方式安装
rpm  -q  php
[ `echo  $?` ] &&  exit  1

#判断是否存在"CONF_BACK"目录

if  [ -d   CONF_BACK  ]
then	
	
else
	mkdir  ./CONF_BACK
if

#查看make编译安装的php命令路径

CMD=`locate  php   |  grep  "\/php$"  |   grep  "\/php\/bin\/"`

#查看php编译时的参数

$CMD  -i  &>   ./cache.tmp


#查看编译安装的主配置文件的路径

DOCUMENT_PATH=`cat  ./cache.tmp  |   grep  -i "Configure Command"  |  awk -F '--prefix='  '{print $2}'  | awk  -F  "' '"  '{print  $1}'`

rm  -rf   ./cache.tmp


CONF=`locate  "php.ini"  |  grep  "$DOCUMENT_PATH"   | grep  "\/php.ini$"`

\cp    $CONF    ./CONF_BACK

CONF=`locate  "php-fpm.conf"  |  grep  "$DOCUMENT_PATH"   | grep  "\/php-fpm\.conf$"`

\cp    $CONF    ./CONF_BACK
