#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

################################################
#用于安装rkhunter安全工具
################################################

# 验证当前的用户是否为root账号，不是的话退出当前脚本
[ `id  -u`  == 0 ]  ||  echo "Error: You must be root to run this script, please use root to install lnmp"  ||  exit  1

#检测系统是不是CentOS，如果不是，提醒用户暂时不支持

cat  /etc/issue  |  grep  -iw  "CENTOS"

[ `echo  $?` != 0 ]  &&  exit  1

#判断是否安装了locate工具
rpm  -q  mlocate

[ `echo  $?` != 0 ]  &&  yum  install  -y  mlocate 

updatedb


yum  install  wget   -y   
#wget下载rkhunter安装包

#wget  -O   存放路径        下载路径

#安装
tar  -zxvf  rkhunter-1.4.2.tar.gz
cd  rkhunter-1.4.2
./installer.sh  --layout  default  --install


#更新
/usr/local/bin/rkhunter   --update
#创建基准
/usr/local/bin/rkhunter   --propupd

# 设置计划任务和邮件发送。
注意：需要获取用户的邮箱地址
cat > /etc/cron.daily/rkhunter.sh <<EOF
#!/bin/sh
(
/usr/local/bin/rkhunter --versioncheck
/usr/local/bin/rkhunter --update
/usr/local/bin/rkhunter --cronjob --report-warnings-only
) | /bin/mail -s 'rkhunter Daily Run  $(hostname --fqdn)'   wanghaicheng2004@126.com
EOF

#设置脚本可执行
chmod 700 /etc/cron.daily/rkhunter.sh
