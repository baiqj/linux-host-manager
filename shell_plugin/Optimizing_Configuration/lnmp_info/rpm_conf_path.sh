#!/bin/bash

##############################
#检测Rpm安装方式Apache主配置文件的路径
##############################
updatedb

ENV_PATH=../env_config

LINE_NUM=`grep  -n  "Rpm_Conf_Path"   $ENV_PATH  |  awk -F:  '{print $1}'`

#在"Rpm_Conf_Path"行之后添加一行

sed  -ie  "/Rpm_Conf_Path/a \'Rpm_Conf_Path\':\'"/etc/httpd/conf/httpd.conf"\'"   $ENV_PATH

#删除原来的"Rpm_Conf_Path"行

sed -i  ''$LINE_NUM'd'   $ENV_PATH



