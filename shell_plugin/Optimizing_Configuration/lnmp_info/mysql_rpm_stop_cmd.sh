#!/bin/bash

##############################
#检测Rpm安装方式mysql关闭脚本路径
##############################
updatedb

ENV_PATH=../env_config

#不是rpm安装mysql时退出当前脚本
rpm  -q   mysql
[ `echo  $?` ]  ||  exit  1


LINE_NUM=`grep  -n  "MySql_Rpm_Stop_Cmd"   $ENV_PATH  |  awk -F:  '{print $1}'`

#在"MySql_Rpm_Stop_Cmd"行之后添加一行

sed  -ie  "/MySql_Rpm_Stop_Cmd/a \'MySql_Rpm_Stop_Cmd\':\'"service mysqld stop"\'" $ENV_PATH

#删除原来的"MySql_Rpm_Stop_Cmd"行

sed -i  ''$LINE_NUM'd'   $ENV_PATH






