#!/bin/bash
#############################
#将原有的nginx服务设置开机不启动
#############################

updatedb
ENV_PATH=../env_config

#查看nginx的启动脚本
locate  nginx  |  grep  "\/etc\/rc.d\/init\.d\/httpd$"

[ `echo  $?` ]  &&  chkconfig  nginx  off

#删除rc.local中的nginx启动项

sed   -i   '/nginx/d'   /etc/rc.d/rc.local

