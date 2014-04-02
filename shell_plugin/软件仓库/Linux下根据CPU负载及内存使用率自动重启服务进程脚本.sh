为了让服务器能稳定运行，所以做个脚本能自动检测系统负载，在系统负载很高的时候（当负载或内存占用达到设置值后），自动重启有问题的程序以避免宕机：
# 设置最大内存占用百分比
PID_MEM_MAX=”85″
# 设置最大系统负载
SYS_LOAD_MAX=”1″
# 设置需要监控的服务名称
NAME_LIST=”php5-cgi mysql”
for NAME in $NAME_LIST
do
# 初始化内存统计
PID_MEM_SUM=0
# 获取该程序总进程数
PID_NUM_SUM=`ps aux | grep $NAME | wc -l`
# 列出每个进程内存占用百分比
PID_MEM_LIST=`ps aux | grep $NAME | awk ‘{print $4}’`
# 计算所有进程总内存占用
for PID_MEM in $PID_MEM_LIST
do
PID_MEM_SUM=`echo $PID_MEM_SUM + $PID_MEM | bc`
done
# 获取最近一分钟系统负载
SYS_LOAD=`uptime | awk ‘{print $(NF-2)}’ | sed ‘s/,//’`
# 比较内存占用和系统负载是否超过阀值
MEM_VULE=`awk ‘BEGIN{print(‘”$PID_MEM_SUM”‘>=’”$PID_MEM_MAX”‘?”1″:”0″)}’`
LOAD_VULE=`awk ‘BEGIN{print(‘”$SYS_LOAD”‘>=’”$SYS_LOAD_MAX”‘?”1″:”0″)}’`
# 如果系统内存占用和系统负载超过阀值，则进行下面操作。
if [ $MEM_VULE = 1 ] || [ $LOAD_VULE = 1 ] ;then
# 写入日志
echo $(date +”%y-%m-%d %H:%M:%S”) “killall $NAME” “(MEM:$PID_MEM_SUM,LOAD:$SYS_LOAD)”>> /var/log/autoreboot.log
# 正常停止服务
/etc/init.d/$NAME stop
sleep 3
# 强制关闭
pkill $NAME
# 重启
/etc/init.d/$NAME start
#写入日志
echo $(date +”%y-%m-%d %H:%M:%S”) “start $NAME” “(MEM:$PID_MEM_SUM,LOAD:$SYS_LOAD)” >> /var/log/autoreboot.log
else
echo “$NAME very health!(MEM:$PID_MEM_SUM,LOAD:$SYS_LOAD)” > /dev/null
fi
done
以上代码保存为一个文件，例如：auto_reboot.sh
添加计划任务，设置每分钟检查一次（注意文件的位置要搞正确）
crontab -e
* * * * * /bin/bash/root/auto_reboot.sh
请确保您的Linux系统中已经安装了bc，否则会出现错误。查看是否安装了bc可以使用命令：
bc -v
如果没有安装，centos可以用 yum -y install bc 安装，然后执行命令：
sh /bin/bash/root/auto_reboot.sh
CentOS VPS服务器根据CPU负载及内存占用自动重启的bash shell脚本：
#!/bin/sh
# usage: */2 * * * * root /root/checkload.sh
# [CentOS]VPS服务器根据CPU负载及内存占用自动重启脚本
# 设置最小剩余内存，一般至少要剩余50M可用（单位兆）
    FREE_MEM_MIN=”50″
# 设置最大系统负载
    SYS_LOAD_MAX=”3″
# 设置重启服务的最小剩余内存（单位兆）
    RESTART_FREE_MEM_MIN=”500″
# 设置需要监控的服务名称
    NAME_LIST=”httpd mysqld”
    for NAME in $NAME_LIST
    do
# 获得剩余内存（单位兆）
    FREE_MEM=`free -m|grep Mem|awk ‘{print $4}’`
# 获得已用内存（单位兆）
#   FREE_MEM=`free -m|grep Mem|awk ‘{print $3}’`
# 获取最近一分钟系统负载
    SYS_LOAD=`uptime | awk ‘{print $(NF-2)}’ | sed ‘s/,//’`
# 比较内存占用和系统负载是否超过阀值
    MEM_VULE=`awk ‘BEGIN{print(‘”$FREE_MEM”‘<’”$FREE_MEM_MIN”‘?”1″:”0″)}’`
    LOAD_VULE=`awk ‘BEGIN{print(‘”$SYS_LOAD”‘>=’”$SYS_LOAD_MAX”‘?”1″:”0″)}’`

# 测试结果
# LOAD_VULE=”1″
# echo $(date +”%y-%m-%d %H:%M:%S”) “DEBUG $NAME”   “(FREE_MEM:$FREE_MEM|$MEM_VULE,LOAD:$SYS_LOAD|$LOAD_VULE)”>> /var/log/autoreboot_debug.log

# 如果系统内存占用和系统负载超过阀值，则进行下面操作。
    if [ $MEM_VULE = 1 ] || [ $LOAD_VULE = 1 ] ;then
# 写入日志
    echo $(date +”%y-%m-%d %H:%M:%S”) “killall $NAME” “(FREE_MEM:$FREE_MEM,LOAD:$SYS_LOAD)”>> /var/log/autoreboot.log
# 正常停止服务
    service $NAME stop
    sleep 3
# 强制关闭
    skill $NAME
# 重启
    sleep 10
    for i in 1 2 3
    do
    FREE_MEM=`free -m|grep Mem|awk ‘{print $4}’`
    MEM_VULE=`awk ‘BEGIN{print(‘”$FREE_MEM”‘>=’”$RESTART_FREE_MEM_MIN”‘?”1″:”0″)}’`
    if [ `pgrep $NAME | wc -l` -le 0 ] && [ $MEM_VULE = 1 ]
    then
    service $NAME start
    sleep 15
    echo “AutoStart:” $(date +”%y-%m-%d %H:%M:%S”) “start $NAME” `ps -ef | grep $NAME | wc -l` > /var/log/autoreboot.log
    fi
    done

# 写入日志
    echo $(date +”%y-%m-%d %H:%M:%S”) “start $NAME” “(FREE_MEM:$FREE_MEM,LOAD:$SYS_LOAD)” >> /var/log/autoreboot.log
    else
    MEM_VULE=`awk ‘BEGIN{print(‘”$FREE_MEM”‘>=’”$RESTART_FREE_MEM_MIN”‘?”1″:”0″)}’`
    if [ `pgrep $NAME | wc -l` -le 0 ] && [ $MEM_VULE = 1 ]
    then
    service $NAME start
    sleep 15
    echo “AutoStart:” $(date +”%y-%m-%d %H:%M:%S”) “start $NAME” `ps -ef | grep $NAME | wc -l` > /var/log/autoreboot.log
    else
    echo “$NAME very health!(FREE_MEM:$FREE_MEM,LOAD:$SYS_LOAD)” > /dev/null
    fi
    fi
    done