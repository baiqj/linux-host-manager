#!/bin/bash

##############################
#检测Rpm安装方式Apache启动脚本路径
##############################
updatedb

ENV_PATH=../env_config

LINE_NUM=`grep  -n  "Apache_Rpm_Start_Cmd"   $ENV_PATH  |  awk -F:  '{print $1}'`

#在"Apache_Rpm_Start_Cmd"行之后添加一行

sed  -ie  "/Apache_Rpm_Start_Cmd/a \'Apache_Rpm_Start_Cmd\':\'"service httpd start"\'" $ENV_PATH

#删除原来的"Apache_Rpm_Start_Cmd"行

sed -i  ''$LINE_NUM'd'   $ENV_PATH






