#!/bin/bash
#############################
#将原有的mysql服务设置开机不启动
#############################

updatedb
ENV_PATH=../env_config

#查看mysql的启动脚本
locate  mysqld  |  grep  "\/etc\/rc.d\/init\.d\/mysqld$"
[ `echo  $?` ]  &&  chkconfig  mysqld  off 

locate  mysql  |  grep  "\/etc\/rc.d\/init\.d\/mysql$"
[ `echo  $?` ]  &&  chkconfig  mysql  off 


#删除rc.local中的mysql启动项

sed   -i   '/mysql/d'   /etc/rc.d/rc.local
