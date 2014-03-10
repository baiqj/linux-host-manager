#!/bin/bash

##############################
#检测Linux系统版本信息
##############################

#查看系统版本信息并赋予到env_config的OS_version

ENV_PATH=./env_config

OS=`cat  /etc/issue | grep  -i  release`

sed -i  "/OS_version/s/$/\'$OS\'/"  $ENV_PATH

#判断Linux系统的位数

uname  -a    |  grep  -i  "x86_64"

if  [ `echo $?`  == 0  ] 
then
	 sed -i  "/OS_bit/s/$/\'x86_64\'/"  $ENV_PATH
else
	 sed -i  "/OS_bit/s/$/\'i386\'/"  $ENV_PATH
fi

