#!/bin/sh
 
##############################
#脚本用途：用于对Linux系统进行安全设置
##############################

[ -d  /usr/local/backup ]  ||  mkdir  -p  /usr/local/backup
[ -d  /usr/local/resault ] ||  mkdir  -p  /usr/local/resault

#用于锁定不常用的系统账号

passwd -l xfs
 
passwd -l news
 
passwd -l nscd
 
passwd -l dbus
 
passwd -l vcsa
 
passwd -l games
 
passwd -l nobody
 
passwd -l avahi
 
passwd -l haldaemon
 
passwd -l gopher
 
passwd -l ftp
 
passwd -l mailnull
 
passwd -l pcap
 
passwd -l mail
 
passwd -l shutdown
 
passwd -l halt
 
passwd -l uucp
 
passwd -l operator
 
passwd -l sync
 
passwd -l adm
 
passwd -l lp

echo  "####lock the password for the named account (root only)###"


#使用chattr对系统关键文件进行锁定，不允许修改

chattr +i /etc/passwd
 
chattr +i /etc/shadow
 
chattr +i /etc/group
 
chattr +i /etc/gshadow

chattr +i /etc/services

echo   "###config chattr done###"



#添加规则：连续3次登陆失败，则锁定账号5分钟

\cp   /etc/pam.d/system-auth    /usr/local/backup/system-auth.old

sed -i 's#auth        required      pam_env.so#auth        required      pam_env.so\nauth       required       pam_tally.so  onerr=fail deny=3 unlock_time=300\nauth           required     /lib/security/$ISA/pam_tally.so onerr=fail deny=3 unlock_time=300#' /etc/pam.d/system-auth


#添加规则：登陆系统5分钟内无操作，则自动登出系统

\cp   /etc/profile      /usr/local/backup/profile.old

echo "TMOUT=300" >>/etc/profile

#添加规则：只记录系统最近10条的操作记录

sed -i "s/HISTSIZE=1000/HISTSIZE=10/" /etc/profile

# history security
chattr +a /root/.bash_history
chattr +i /root/.bash_history


#enable /etc/profile go!
source /etc/profile


#设置内核启用syncookie功能

\cp /etc/sysctl.conf /usr/local/backup/sysctl.conf.old

echo "net.ipv4.tcp_syncookies=1" >> /etc/sysctl.conf
# exec sysctl.conf enable
sysctl -p 



#优化SSH设置，禁用DNS解析
\cp   /etc/ssh/sshd_config   /usr/local/backup/sshd_config.old

sed -i "s/#MaxAuthTries 6/MaxAuthTries 6/" /etc/ssh/sshd_config
sed -i "s/#UseDNS yes/UseDNS no/" /etc/ssh/sshd_config


#限制系统重要命令的权限，使只有root能够执行

chmod 700 /bin/ping
chmod 700 /usr/bin/finger
chmod 700 /usr/bin/who
chmod 700 /usr/bin/w
chmod 700 /usr/bin/locate
chmod 700 /usr/bin/whereis
chmod 700 /sbin/ifconfig
chmod 700 /usr/bin/pico
chmod 700 /bin/vi
chmod 700 /usr/bin/which
chmod 700 /usr/bin/gcc
chmod 700 /usr/bin/make
chmod 700 /bin/rpm


# write important command md5
cat > list << "EOF" &&
/bin/ping
/bin/finger
/usr/bin/who
/usr/bin/w
/usr/bin/locate
/usr/bin/whereis
/sbin/ifconfig
/bin/pico
/bin/vi
/usr/bin/vim
/usr/bin/which
/usr/bin/gcc
/usr/bin/make
/bin/rpm
EOF

for i in `cat list`
do
if [ ! -x $i ];then
echo "$i not found,no md5sum!"
else
md5sum $i >> /var/log/`hostname`.log
fi
done
rm -f list

#优化内核的参数设置


cat> /etc/sysctl.conf<< EOF
# Avoid a smurf attack
net.ipv4.icmp_echo_ignore_broadcasts = 1
# Turn on protection for bad icmp error messages
net.ipv4.icmp_ignore_bogus_error_responses = 1
# Turn on syncookies for SYN flood attack protection
net.ipv4.tcp_syncookies = 1
# Turn on and log spoofed, source routed, and redirect packets
net.ipv4.conf.all.log_martians = 1
net.ipv4.conf.default.log_martians = 1
# No source routed packets here
net.ipv4.conf.all.accept_source_route = 0
net.ipv4.conf.default.accept_source_route = 0
# Turn on reverse path filtering
net.ipv4.conf.all.rp_filter = 1
net.ipv4.conf.default.rp_filter = 1
# Make sure no one can alter the routing tables
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.default.accept_redirects = 0
net.ipv4.conf.all.secure_redirects = 0
net.ipv4.conf.default.secure_redirects = 0
# Don't act as a router
net.ipv4.ip_forward = 0
net.ipv4.conf.all.send_redirects = 0
net.ipv4.conf.default.send_redirects = 0
# Turn on execshild
kernel.exec-shield = 1
kernel.randomize_va_space = 1
# Tuen IPv6
net.ipv6.conf.default.router_solicitations = 0
net.ipv6.conf.default.accept_ra_rtr_pref = 0
net.ipv6.conf.default.accept_ra_pinfo = 0
net.ipv6.conf.default.accept_ra_defrtr = 0
net.ipv6.conf.default.autoconf = 0
net.ipv6.conf.default.dad_transmits = 0
net.ipv6.conf.default.max_addresses = 1
# Optimization for port usefor LBs
# Increase system file descriptor limit
fs.file-max = 65535
# Allow for more PIDs (to reduce rollover problems); may break some programs 32768
kernel.pid_max = 65536
# Increase system IP port limits
net.ipv4.ip_local_port_range = 2000 65000
# Increase TCP max buffer size setable using setsockopt()
net.ipv4.tcp_rmem = 4096 87380 8388608
net.ipv4.tcp_wmem = 4096 87380 8388608
# Increase Linux auto tuning TCP buffer limits
# min, default, and max number of bytes to use
# set max to at least 4MB, or higher if you use very high BDP paths
# Tcp Windows etc
net.core.rmem_max = 8388608
net.core.wmem_max = 8388608
net.core.netdev_max_backlog = 5000
net.ipv4.tcp_window_scaling = 1
EOF

/sbin/sysctl   -p


#禁用大量的用户登录

\cp /etc/inittab   /usr/local/backup/inittab.old

sed -i '/tty[2-6]/s/^/#/' /etc/inittab
/sbin/init q
echo "off the excess tty -->ok!"
sleep 1
