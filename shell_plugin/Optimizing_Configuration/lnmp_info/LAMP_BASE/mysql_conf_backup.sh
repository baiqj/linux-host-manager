#!/bin/bash

##############################
#mysql的主配置文件的备份
##############################
updatedb

ENV_PATH=../env_config

#判断是否存在"CONF_BACK"目录

if  [ -d   CONF_BACK  ]
then	
	
else
	mkdir  ./CONF_BACK
if

#判断/etc/my.cnf内容不为空
if  [ -s  /etc/my.cnf ]
then
	\cp    /etc/my.cnf    ./CONG_BACK/`date  +%Y-%m-%d`-my.cnf
fi



