#!/bin/bash

##############################
#检测make安装方式mysql启动脚本路径
##############################
updatedb

ENV_PATH=../env_config

#rpm安装mysql时退出当前脚本
rpm  -q   mysql
[ `echo  $?` ]  &&  exit  1

CMD=`locate  mysqld_safe  |  grep  "\/mysqld_safe$"  |  grep  "\/mysql\/bin\/"`

LINE_NUM=`grep  -n  "MySql_Make_Start_Cmd"   $ENV_PATH  |  awk -F:  '{print $1}'`

#在"MySql_Make_Start_Cmd"行之后添加一行

sed  -ie  "/MySql_Make_Start_Cmd/a \'MySql_Make_Start_Cmd\':\'$CMD  &\'" $ENV_PATH

#删除原来的"MySql_Make_Start_Cmd"行

sed -i  ''$LINE_NUM'd'   $ENV_PATH






