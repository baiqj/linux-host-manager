#!/bin/bash

PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

#��ע1����ǰ�Ľű���ʹ����rpm��װ��LAMP����������Ǳ��밲װ��LAMP����Ҫ�Խű������޸�
#��ע2�����Խ��ű����ص��������ŵ���ʱĿ¼�У�ִ����ɺ���ɾ��

# ��֤��ǰ���û��Ƿ�Ϊroot�˺ţ����ǵĻ��˳���ǰ�ű�
[ `id  -u`  == 0 ]  ||  echo "Error: You must be root to run this script, please use root to install lnmp"  ||  exit  1

pwd=`pwd`

#Ϊ�ű���ӿ�ִ��Ȩ��
chmod +x lamp_scripts_for_website/*.sh

yum  install  -y   unzip   wget  

#����config.listִ��apache-vhost.sh����vhost
./lamp_scripts_for_website/apache-vhost.sh











