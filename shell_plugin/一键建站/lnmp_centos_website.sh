#!/bin/bash


PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

#��ע1����ǰ�Ľű���ʹ����rpm��װ��LAMP����������Ǳ��밲װ��LAMP����Ҫ�Խű������޸�
#��ע2�����Խ��ű����ص��������ŵ���ʱĿ¼�У�ִ����ɺ���ɾ��

# ��֤��ǰ���û��Ƿ�Ϊroot�˺ţ����ǵĻ��˳���ǰ�ű�
[ `id  -u`  == 0 ]  ||  echo "Error: You must be root to run this script, please use root to install lnmp"  ||  exit  1

pwd=`pwd`

#Ϊ�ű���ӿ�ִ��Ȩ��
chmod +x lnmp_scripts_for_website/*.sh

yum  install  -y  wget   unzip

#����config.listִ��apache-vhost.sh����vhost
./lnmp_scripts_for_website/nginx-vhost.sh

#ΪDedeCMS V5.7 (SP1)��װ������

#����ԭ�е���վĿ¼


#�ϴ�����������ԭ�е��ļ�