#!/bin/bash

##############################
#mysql配置文件的备份
##############################
updatedb

ENV_PATH=../env_config

#判断是否存在"CONF_BACK"目录

if  [ -d   CONF_BACK  ]
then	
	
else
	mkdir  ./CONF_BACK
if

\cp     /etc/my.cnf     .\CONG_BACK
