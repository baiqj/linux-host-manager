#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

# ��֤��ǰ���û��Ƿ�Ϊroot�˺ţ����ǵĻ��˳���ǰ�ű�
[ `id  -u`  == 0 ]  ||  echo "Error: You must be root to run this script, please use root to install lnmp"  ||  exit  1

#���ϵͳ�ǲ���CentOS��������ǣ������û���ʱ��֧��

cat  /etc/issue  |  grep  -iw  "CENTOS"

[ `echo  $?` != 0 ]  &&  exit  1

#��װwget
yum  install  -y   wget

#��װ��locate
yum  install  -y  mlocate 

#���ذ�װ��
wget  -O  falcon-master.zip   http://bcs.duapp.com/linux2host2manager/%2Fpackages2%2Ffalcon-master.zip?sign=MBO:E64167e555322cbfb5997582b43a551b:WXo6hJE2LWS%2FBQ0ClrTKWbYoDDM%3D

##################################################################
#����inotify.hͷ�ļ�

wget  -O inotify.tar.gz   ���ص�ַ
tar -zxvf   inotify.tar.gz 

mkdir  -p   /usr/include/sys
cp  inotify.h  inotify-syscalls.h  /usr/include/sys/
################################################################
#��ȡ��װ��inotify-tools

#wget  http://cloud.github.com/downloads/rvoicilas/inotify-tools/inotify-tools-3.14.tar.gz


#��װ������
yum  install  gcc  -y  

#���밲װinotify-tools
tar  -zxvf  inotify-tools-3.14.tar.gz 
cd  inotify-tools-3.14
./configure --prefix=/usr/local && make &&  make install

#��װmysql-devel

yum  install  mysql-devel  -y  
#

#��ѹ��װ��
yum install  unzip  -y
cd   ../
unzip   falcon-master.zip


#�жϼ�������뻷���Ƿ�߱�
cd  falcon-master/Release/
chmod  +x   check.sh
./check.sh


#�ڶ�������װFalcon��������
updatedb
CONFIG_PATH=`locate   config.list`

MYSQL_ADMIN="root"
MYSQL_PASSWORD=`grep  -i  "mysqlrootpwd"  $CONFIG_PATH | awk -F  ":" '{print  $2}'`
HOSTNAME="localhost"
MYSQL_PORT="3306"


#�������ݿ����Ϣ���������ơ�����Ա������޸� �ļ�./falconconsole/public/config.inc.php
<?php
// ���ݿ���Ϣ
$dbhost = "localhost";                                  // ���ݿ�������
$dbuser = "root";                                       // ���ݿ��û���
$dbpass = "123456";                                             // ���ݿ�����
$dbname = "falcondb";                                   // ���ݿ���

// ���ݱ���
$table1 = "f_user";
$table2 = "f_monitor";

//��ҳ����
$pagenumber = 10//ÿҳ��ʾ�����Ϣ������Ĭ��ÿҳ��ʾ10��
?>
~
#�޸������ļ��е����ݿ�������Ϣ����������������س���û�а�װ��ͬһ̨��������ȷ������������ܹ���Ȩ���ʵ�������������������Mysql���ݿ�
#��ע���˴����ǵļ�غͱ������ͬһ̨������

#����install.php��װ��������

#��ô����

 cp  -rpv  falconconsole/  /var/www/html/

���������޸ļ�س��������ļ�������

������Ҫ�������ݿ����������Ϣ����Ҫ��ص�WebĿ¼��"/"��β
vim src/conf/global.conf
make
���Ĳ�����̨���м�س���

nohup ./falcon start >falcon.log 2>&1 &
ps aux|grep "falcon"
root 2981 0.2 0.3 9352 1848 pts/0 S 04:46 0:00 ./falcon start

�����ڵ�ǰ����Ŀ¼��������־�ļ�falcon.log
��ͨ�����ʿ������Ĳ鿴�������(e.g. http://127.0.0.1/falconconsole/index.php)