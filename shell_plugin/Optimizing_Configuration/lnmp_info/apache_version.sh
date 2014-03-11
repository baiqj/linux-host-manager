#!/bin/bash

##############################
#检测Apache的安装版本
##############################
updatedb

ENV_PATH=../env_config

#定位apachectl命令的路径

CMD_PATH=`locate  apachectl  |  grep  "\/apachectl$"`

#将apache的版本赋值给"VERSION"变量

VERSION=`$CMD_PATH  -v | grep  -i "version"  | awk  '{print $3}'`

#查看"Apache_Version"所在的行号

LINE_NUM=`grep  -n  "Apache_Version"   ../env_config  |  awk -F:  '{print $1}'`

#在"Apache_Version"行之后添加一行

sed  -ie  "/Apache_Version/a \'Apache_Version\':\'$VERSION"\'   $ENV_PATH

#删除原来的"Apache_Version"行

sed -i  '14d'  $ENV_PATH






