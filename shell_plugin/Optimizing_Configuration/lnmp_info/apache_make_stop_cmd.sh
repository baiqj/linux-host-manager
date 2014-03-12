#!/bin/bash

##############################
#检测Make安装方式Apache的关闭命令
##############################
updatedb

ENV_PATH=../env_config

#判断是否存在Make编译安装的Apahce的apachectl命令文件，没有的话退出本脚本

locate  "apachectl"  |  grep  "\/apachectl$"  |  grep  -v  "/usr/sbin/apachectl"

[  `echo $?` == 1 ]  ||  exit 1

CMD=`locate  "apachectl"  |  grep  "\/apachectl$"  |  grep  -v  "/usr/sbin/apachectl"`

LINE_NUM=`grep  -n  "Make_Stop_Cmd"   $ENV_PATH  |  awk -F:  '{print $1}'`

#在"Make_Stop_Cmd"行之后添加一行

sed  -ie  "/Make_Stop_Cmd/a \'Make_Stop_Cmd\':\'"'$CMD -k  stop'"\'"   $ENV_PATH

#删除原来的"Make_Stop_Cmd"行

sed -i  ''$LINE_NUM'd'   $ENV_PATH



