#!/bin/bash

##############################
#检测PHP是否已经安装
##############################
updatedb

ENV_PATH=../env_config

#判断PHP的主配置文件是否存在

locate   "php.ini"  |  grep  -i  "\/php\.ini$" |   grep  -vi "\/doc"  |  grep  -vi  "\/share\/"  |  grep -vi  "ln*mp*"  


if  [ `echo $?`  == 0  ] 
then
	 sed -i  "/'Php_Install':/s/$/\'On\'/"  $ENV_PATH
else
	 sed -i  "/'Php_Install':/s/$/\'Off\'/"  $ENV_PATH