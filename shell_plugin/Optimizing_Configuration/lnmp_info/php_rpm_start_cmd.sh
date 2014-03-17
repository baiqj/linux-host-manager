#!/bin/bash

##############################
#检测Rpm安装方式php-fpm的重新加载命令
##############################

updatedb

ENV_PATH=../env_config


if [ `rpm -q  php` -a `rpm -q  php-fpm` ]  
then
	CMD=`rpm  -ql  php-fpm  | grep  "\/php-fpm$"  |  grep  "\/usr\/sbin\/"`
else
	exit  1
	
