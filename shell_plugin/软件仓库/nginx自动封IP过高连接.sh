#!/bin/python
#-*- coding:utf-8 -*-
# Filename:    drop_ip_iptables.py
# Revision:    1.0
# Date:        2013-2-21
# Author:      simonzhang
# web:         www.simonzhang.net
# Email:       simon-zzm@163.com
#http://www.osthing.com/article/server-ip-address-automatic-blocking-reconciliation-attack.html
### END INIT INFO
import os
import time
from string import strip
 
 
#### 参数(parameter)和脚本中使用到的系统敕令
nginx_log = "/usr/local/nginx/logs/nginx.access.log"
# 统计(statistics)nginx日志(log)中IP访问数量
check_comm = "/bin/cat %s |awk ' ''{print $1}'|sort |uniq -c|sort -n -k1 -r" % nginx_log
# 放在crontab中10 minute 跑一次,访问超出n次的全部封掉
overproof = 3000
# 被封 Address 记录(records) file 
#  file 中记录(records)封IP时间和 IP address .时间单元为秒
lock_ip_list = "/usr/local/nginx/logs/lock_ip_list.txt"
# 被封 Address 解开时间.时间单元为秒
unlock_time = 3600*24*2
 
 
def manage_lock_ip():
    # 获得当前时间
    get_now_time = int(time.time())
    # 管理日志(log)字典(dictionary)
    man_ip = {}
    # 处理日志(log)中的IP
    try:
        log_file = open('%s' % lock_ip_list, 'rb').readlines()
        for get_ip_info in log_file:
            _get_ip_info = strip(get_ip_info).split(' ')
            man_ip['%s' % _get_ip_info[1]] = int(_get_ip_info[0])
    except:
        exit(0)
    # 清空(empty)iptable列表,和ip记录(records)日志(log)
    os.popen('/sbin/iptables -F')
    clean_file = open('%s' % lock_ip_list, 'rb+')
    clean_file.truncate()
    # 开始处理IP,被封没有超时的IP写入iptables和日志(log)中
    log_file = open('%s' % lock_ip_list, 'ab')
    for loop_ip in man_ip.keys():
        if (get_now_time - man_ip[loop_ip]) < unlock_time:
            os.popen('/sbin/iptables -I INPUT -s %s -j DROP' % loop_ip)
            log_file.write('%s %s\n' % (man_ip[loop_ip], loop_ip))
    log_file.close()
         
 
 
def main():
    # 已封 IP address 字典(dictionary)
    drop_ip_list = {}
    # 加载已封IP日志(log)
    try:
        log_file = open('%s' % lock_ip_list, 'rb').readlines()
        for get_drop_ip_info in log_file:
            _get_drop_ip_info = strip(get_drop_ip_info).split(' ')
            drop_ip_list['%s' % _get_drop_ip_info[1]] = int(_get_drop_ip_info[0])
    except:
        os.mknod('%s' % lock_ip_list)
    # 获得nginx日志(log)中的访问超高的ip并写入日志(log)
    access_high_ip = os.popen('%s' % check_comm).readlines()
    for get_ip_count in access_high_ip:
        try :
            _get_ip_count = strip(get_ip_count).split(' ')
            _get_ip = _get_ip_count[1]
            _get_count = _get_ip_count[0]
        except:
            pass
        if (int(_get_count) > int(overproof)) and (_get_ip not in drop_ip_list.keys()):
            now_time = int(time.time())
            log_file = open('%s' % lock_ip_list, 'ab+')
            log_file.write('%s %s\n' % (now_time, _get_ip))
            log_file.close()
    # 统计(statistics)终了清空(empty)nginx日志(log)
    log_file = open('%s' % nginx_log, 'wb')
    log_file.truncate()
    # 处理要封的IP和要解开的IP
    manage_lock_ip()
 
 
if __name__ == '__main__':
    main()