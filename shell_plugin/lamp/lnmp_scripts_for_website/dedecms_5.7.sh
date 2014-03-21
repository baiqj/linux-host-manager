#!/bin/bash
#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

# Check if user is root
if [ $(id -u) != "0" ]; then
    echo "Error: You must be root to run this script, please use root to install lnmp"
    exit 1
fi

cur_dir=$(pwd)

HOSTNAME="localhost"

DATA_DISK=`cat   /tmp/.mount.list`

CONFIG_PATH=`find   /tmp  -name  "\.dedecms\.list"`

sed  -i   '/^ *$/d'    $CONFIG_PATH

NUM=`grep  -i  "domain="   $CONFIG_PATH  | wc  -l `



for  ((i=1;i<=NUM;i++))
do

	DOMAIN=`grep  -i  "domain="  $CONFIG_PATH  | sed  -n  ''$i',1p'  | awk  -F  "DOMAIN="   '{print  $2}'  |  awk   '{print  $1}'`
	

	
	VHOST_DIR="$DATA_DISK/www/$DOMAIN"
	tar  -zxvf  DedeCMS-v5.7-20130607-UTF8-SP1.tar.gz 
	\cp   -rpv  DedeCMS-V5.7-UTF8-SP1/uploads/*           $VHOST_DIR

	
	chown -R www:www  $VHOST_DIR

done

