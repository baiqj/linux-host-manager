#!/bin/bash

##############################
#检测Make安装方式Apache的重新启动命令
##############################
updatedb

ENV_PATH=../env_config

#判断是否存在Make编译安装的Apahce主配置文件，没有的话退出本脚本

locate   "httpd.conf"  |  grep  -i  "\/conf\/httpd\.conf$" |  grep  -v  "\/etc\/httpd\/conf\/httpd.conf" |  grep  -vi "\/doc"  |  grep  -vi  "\/share\/"  |  grep -vi  "ln*mp*"  

[ `echo  $?` == 0 ] ||  exit 1

#查看编译安装的apache的主配置文件的路径

CONF=`locate   "httpd.conf"  |  grep  -i  "\/conf\/httpd\.conf$" |  grep  -v  "\/etc\/httpd\/conf\/httpd.conf" |  grep  -vi "\/doc"  |  grep  -vi  "\/share\/"  |  grep -vi  "ln*mp*"  `

CMD=`locate  "apachectl"  |  grep  "\/apachectl$"  |  grep  -v  "/usr/sbin/apachectl"`

LINE_NUM=`grep  -n  "Make_Restart_Cmd"   $ENV_PATH  |  awk -F:  '{print $1}'`

#在"Make_Restart_Cmd"行之后添加一行

sed  -ie  "/Make_Restart_Cmd/a \'Make_Restart_Cmd\':\'"'$CMD -k  restart'"\'"   $ENV_PATH

#删除原来的"Make_Restart_Cmd"行

sed -i  ''$LINE_NUM'd'   $ENV_PATH



