#!/bin/bash


PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

# ��֤��ǰ���û��Ƿ�Ϊroot�˺ţ����ǵĻ��˳���ǰ�ű�
[ `id  -u`  == 0 ]  ||  echo "Error: You must be root to run this script, please use root to install lnmp"  ||  exit  1

pwd=`pwd`

#Ϊ�ű���ӿ�ִ��Ȩ��
chmod +x lnmp_scripts_for_website/*.sh

#����config.listִ��apache-vhost.sh����vhost
./lnmp_scripts_for_website/nginx-vhost.sh

#ΪDedeCMS V5.7 (SP1)��װ������

#����ԭ�е���վĿ¼


#�ϴ�����������ԭ�е��ļ�