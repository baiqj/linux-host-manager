#!/bin/bash

##############################
#Rpm安装方式Apache的主配置文件的备份
##############################
updatedb

ENV_PATH=../env_config

#判断apache是否为rpm方式安装
rpm  -q  httpd
[ `echo  $?` ] ||  exit  1

#判断是否存在"CONF_BACK"目录

if  [ -d   CONF_BACK  ]
then	
	
else
	mkdir  ./CONF_BACK
if

\cp    /etc/httpd/conf/httpd.conf   ./CONG_BACK/`date  +%Y-%m-%d`-httpd.conf


