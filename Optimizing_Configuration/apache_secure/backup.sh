#!/bin/bash

##backup configuration file

CONF_PATH=`find / -name 'httpd.conf'  -a  -type f`

[ -d  /usr/local/backup ] ||  mkdir  -p  /usr/local/backup
[ -d  /usr/local/resault ] ||  mkdir  -p  /usr/local/resault

[ -f /usr/local/backup/httpd.conf.old ] || \cp  $CONF_PATH  /usr/local/backup/httpd.conf.old 


grep   -v  "^#"   /usr/local/backup/httpd.conf.old  >  $CONF_PATH 

sed  -i  '/^ *$/d'    $CONF_PATH

find  /  -name  "vhost.list"  -a  -type  f  -exec  \cp  {}  /usr/local/resault  \;

if [ -f  /usr/local/resault/vhost.list ]
then
        if [ -s /usr/local/resault/vhost.list ]
        then
                grep   "^DOCUMENT="  /usr/local/resault/vhost.list |  awk -F "="  '{print  $2}' >  /usr/local/resault/web_document.txt

else
                echo 'this host have not website!!!'
                exit 1
        fi
                
else
                echo 'plsase check website-info!!!'
                exit 1
fi

##edit the configuration file


if [ -f  /usr/local/backup/httpd.conf.old ]

then
	echo  "####################"   >>   $CONF_PATH
	for  i  in  $(cat /usr/local/resault/web_document.txt)
	do
		{  cat  <<EOF>>  $CONF_PATH
<Directory "$i">
    Options FollowSymLinks
    AllowOverride None
    Order allow,deny
    Allow from all
</Directory>
EOF
		}
	done
else 
        echo '###please run backup.sh first!!###'
fi


