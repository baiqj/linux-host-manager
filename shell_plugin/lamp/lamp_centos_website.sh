#!/bin/bash

PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

# ��֤��ǰ���û��Ƿ�Ϊroot�˺ţ����ǵĻ��˳���ǰ�ű�
[ `id  -u`  == 0 ]  ||  echo "Error: You must be root to run this script, please use root to install lnmp"  ||  exit  1

pwd=`pwd`

#Ϊ�ű���ӿ�ִ��Ȩ��
chmod +x lamp_scripts_for_website/*.sh

#����config.listִ��apache-vhost.sh����vhost
./lamp_scripts_for_website/apache-vhost.sh











