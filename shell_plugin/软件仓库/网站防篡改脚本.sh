#!/bin/sh
#定义inotifywait路径
Check_exe=/opt/modules/inotify/bin/inotifywait
#定义线上web目录
Monitor_Object=/opt/onlinehtml
#定义需要监测的状态
Monitor_Status=modify,close_write,move,create,delete
#定义备份目录的路径
SRCDIR=/opt/htmlsrc
#定义rsync路径
Rsync_exe=/usr/bin/rsync
#当前日期
DATE_TODAY=`date +%Y.%m.%d`
##恢复文件函数
restoreweb(){
${Rsync_exe} -av --delete ${SRCDIR}/ ${Monitor_Object}
}
##监测目录文件状态函数
checkweb(){
${Check_exe} -e ${Monitor_Status} -mr --timefmt '%d/%m/%y %H:%M'  --format '%T %w%f %e' ${Monitor_Object}
}
##主函数
main(){
checkweb|while read date time file event 
do
filename=`echo ${file}|awk -F"${Monitor_Object}" '{print $2}'`
case ${event} in
MOVE|CREATE|DELETE)
restoreweb
;;
MODIFY|CLOSE_WRITE)
${Rsync_exe} -av --delete ${SRCDIR}${filename} ${file}
;;
esac
done
}
main
 
