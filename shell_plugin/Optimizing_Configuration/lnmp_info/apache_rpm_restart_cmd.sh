#!/bin/bash

##############################
#检测Rpm安装方式Apache重启动脚本路径
##############################
updatedb

ENV_PATH=../env_config

LINE_NUM=`grep  -n  "Apache_Rpm_Restart_Cmd"   $ENV_PATH  |  awk -F:  '{print $1}'`

#在"Apache_Rpm_Restart_Cmd"行之后添加一行

sed  -ie  "/Apache_Rpm_Restart_Cmd/a \'Apache_Rpm_Restart_Cmd\':\'"service httpd restart"\'" $ENV_PATH

#删除原来的"Apache_Rpm_Restart_Cmd"行

sed -i  ''$LINE_NUM'd'   $ENV_PATH






