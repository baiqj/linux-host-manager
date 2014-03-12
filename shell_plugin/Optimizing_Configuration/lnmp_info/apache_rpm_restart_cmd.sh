#!/bin/bash

##############################
#检测Rpm安装方式Apache重启动脚本路径
##############################
updatedb

ENV_PATH=../env_config

LINE_NUM=`grep  -n  "Make_Restart_Cmd"   $ENV_PATH  |  awk -F:  '{print $1}'`

#在"Make_Restart_Cmd"行之后添加一行

sed  -ie  "/Make_Restart_Cmd/a \'Make_Restart_Cmd\':\'"service httpd restart"\'" $ENV_PATH

#删除原来的"Make_Restart_Cmd"行

sed -i  ''$LINE_NUM'd'   $ENV_PATH






