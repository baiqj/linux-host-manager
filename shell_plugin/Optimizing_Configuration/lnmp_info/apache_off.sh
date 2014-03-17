#!/bin/bash
#############################
#将原有的apache服务设置开机不启动
#############################

updatedb
ENV_PATH=../env_config

#查看apache的启动脚本
locate  httpd  |  grep  "\/etc\/rc.d\/init\.d\/httpd$"

[ `echo  $?` ]  &&  chkconfig  httpd  off

#删除rc.local中的apache启动项

sed   -i   '/httpd/d'   /etc/rc.d/rc.local

