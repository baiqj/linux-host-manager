[root@localhost apache_secure]# cat  backup.sh
#!/bin/bash

##backup configuration file

CONF_PATH=`find / -name 'httpd.conf'  -a  -type f`

[ -d  /usr/local/backup ] ||  mkdir  -p  /usr/local/backup
[ -d  /usr/local/resault ] ||  mkdir  -p  /usr/local/resault

[ -f /usr/local/backup/httpd.conf.old ] || \cp  $CONF_PATH  /usr/local/backup/httpd.conf.old 


grep   -v  "^#"   /usr/local/backup/httpd.conf.old  >  $CONF_PATH 

sed  -i  '/^ *$/d'    $CONF_PATH