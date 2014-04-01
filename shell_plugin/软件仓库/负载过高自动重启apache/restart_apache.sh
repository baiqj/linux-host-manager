#!/bin/sh

mkdir -p /backup/restart_apache

wget http://www.vpshz.com/ordera/load_restart_apache.sh  --output-document=/backup/restart_apache/load_restart_apache.sh

chmod +x /backup/restart_apache/load_restart_apache.sh

echo '*/2 * * * * /backup/restart_apache/load_restart_apache.sh >> /backup/restart_apache/restart_apache.log' >> /var/spool/cron/root

yum -y install bc

echo '';
echo '';
echo ' ====================================================';
echo ' ======== load_restart_apache.sh installed =======';
echo ' ====================================================';
echo '';
echo '';

# wget  http://www.vpshz.com/ordera/restart_apache.sh;sh restart_apache.sh;