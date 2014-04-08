#!/usr/bin/env bash

#########################################################################
# WARNING - Read First Before Running This Script!
# Running this script maybe HARMFUL to your system. Therefor, the user shall
# carefully read all of this script and bear the relevant risks by 
# himself/herself. Running this script means the user accepting agreement above.
#########################################################################

#########################################################################
#   Centos Tweak script for server
#   Licenced under GPLv3
#   Writen by: leo <leo.ss.pku@gmail.com>
#   Inspired by: yzhkpli@gmail.com
#   Feed back: http://www.himysql.com/groups/centos-tweak/
#########################################################################

#########################################################################
#   History:
#   2010-08-18:
#       Fixed:
#           A bug while exporting path into /etc/bashrc caused by "\"(thanks 181789871).
#   2010-08-16:
#       Add:
#           Close the tty between second and sixth(thanks selboo).
#           Increase default open file limits from 1024 to 65525.
#   2010-08-14:
#       Fixed:
#           Optimize code of disabling selinux(thanks huichrist)
#   2010-08-10:
#       Fixed:
#           Disable ius yum repository by default.
#   2010-08-09:
#       Add:
#           Tweak enviroment like PATH, LDFLAGS and LD_LIBRARY_PATH for easy using sudo.
#   2010-08-08:
#       Add:
#           Firstly check running this script as root.
#           Disable gpgcheck and plugins for running fastly.
#           Increase yum cache expire time from 1h to 24h.
#           Turn off auto running fsck while days duration.
#           Turn off writing file reading time (add noatime in /etc/fstab).
#       Fixed:
#           Change file name to centostweak.sh
#           Change /etc/cron.daily/ntpdate with run mode(+x).
#   2010-08-04:
#       Add:
#           Install sudo & enable wheel group to use nopasswrd sudo.
#   2010-08-02:
#       Add:
#           Install & config snmpd.
#           Default iptables rules.
#       Fixed:
#           ntp package name from ntpdate.
#   2010-08-01:
#       To avoid backup file overried, Change backup file name ended from ".origin" to ".%Y-%m-%d_%H-%M-%S".
#   2010-07-31: 
#       Modified to be used with CentOS 5.x Server and sohu mirrors.
#       Removed some unuseful functions.
#       Add functions for turnning unuseful service off while system start.
#       Add functions for kernel & TCP parameters optimizing.
#   2010-06-06:
#       Copied from http://laohuanggua.info/archives/695.
#########################################################################

# Require root to run this script.
if [[ "$(whoami)" != "root" ]]; then
  echo "Please run this script as root." >&2
  exit 1
fi
 
# ��������Դ
cd /etc/yum.repos.d/
cp /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.`date +"%Y-%m-%d_%H-%M-%S"`
sed -i -e 's/mirrorlist/#mirrorlist/' CentOS-Base.repo
sed -i -e 's/#baseurl/baseurl/' CentOS-Base.repo
sed -i -e 's/mirror.centos.org/mirrors.sohu.com/' CentOS-Base.repo

cp /etc/yum.conf /etc/yum.conf.`date +"%Y-%m-%d_%H-%M-%S"`
sed -i 's/gpgcheck=1/gpgcheck=0/' /etc/yum.conf
sed -i 's/plugins=1/plugins=0/' /etc/yum.conf
sed -i 's/metadata_expire=1h/metadata_expire=24h/' /etc/yum.conf

# ���dag@sohuԴ
# relver=`uname -r | awk -F. '{print $NF}'`
echo -e "# Name: SOHU RPM Repository for Red Hat Enterprise 5 �C dag\n"\
"# URL: http://mirrors.sohu.com/dag/redhat/\n"\
"[dag-sohu]\n"\
"name = Red Hat Enterprise \$releasever �C sohu.com �C dag\n"\
"baseurl = http://mirrors.sohu.com/dag/redhat/`uname -r | awk -F. '{print $NF}'`/en/\$basearch/dag\n"\
"enabled = 1\n"\
"gpgcheck = 0"  > /etc/yum.repos.d/dag-sohu.repo
# ���epel@sohuԴ
echo -e "# Name: SOHU RPM Repository for Red Hat Enterprise 5 �C EPEL\n"\
"# URL: http://mirrors.sohu.com/fedora-epel/\n"\
"[epel-sohu]\n"\
"name = Fedora EPEL \$releasever - sohu.com\n"\
"baseurl = http://mirrors.sohu.com/fedora-epel/5Server/\$basearch\n"\
"enabled = 1\n"\
"gpgcheck = 0"  > /etc/yum.repos.d/epel-sohu.repo
# ���iusԴ
# ʹ�÷�����--enablerepo=ius����yum install python26 --enablerepo=ius
echo -e "# Name: IUS RPM Repository for Red Hat Enterprise 5\n"\
"# URL: http://dl.iuscommunity.org/pub/ius/stable/Redhat/\n"\
"[ius]\n"\
"name = Red Hat Enterprise \$releasever �C ius\n"\
"baseurl = http://dl.iuscommunity.org/pub/ius/stable/Redhat/\$releasever/\$basearch/\n"\
"enabled = 0\n"\
"gpgcheck = 0"  > /etc/yum.repos.d/ius.repo

# ��װ�������sysstat, ntp, snmpd, sudo
yum install sysstat ntp net-snmp sudo screen -y

# ����sudo
cp /etc/sudoers /etc/sudoers.`date +"%Y-%m-%d_%H-%M-%S"`
# ����wheel���ϵͳ�û�ͨ��������sudo��ʽ��ʹrootȨ��
sed -i -e '/NOPASSWD/s/^# //' /etc/sudoers
# ��ӻ�����������֤sudoʱ���þ���·��ִ�г��ù��������Լ��������ʱ���ҵ����ļ�
echo 'export PATH=$PATH:/sbin:/usr/sbin' >> /etc/bashrc
echo 'export LDFLAGS="-L/usr/local/lib -Wl,-rpath,/usr/local/lib"' >> /etc/bashrc
echo 'export LD_LIBRARY_PATH="/usr/local/lib"' >> /etc/bashrc

# �Ż�Ӳ��
cp /etc/fstab /etc/fstab.`date +"%Y-%m-%d_%H-%M-%S"`
# �ر�ϵͳд���ļ�����ȡʱ��
sed -i 's/ext3    defaults/ext3    defaults,noatime/' /etc/fstab
# �ر�ϵͳ��ʱ���������´�����ʱ����fsck
grep ext3 /etc/fstab | grep -v boot | awk '{print $1}' | xargs -i tune2fs -i0 {}
# �ر�ϵͳ��mount���������´�����ʱ����fsck
# grep ext3 /etc/fstab | grep -v boot | awk '{print $1}' | xargs -i tune2fs -c-1 {}

# ����ʱ��ͬ��
echo "/usr/sbin/ntpdate cn.pool.ntp.org" >> /etc/cron.daily/ntpdate
chmod +x /etc/cron.daily/ntpdate

# ����snmpd
cp /etc/snmp/snmpd.conf /etc/snmp/snmpd.conf.`date +"%Y-%m-%d_%H-%M-%S"`
sed -i 's/#view all/view all/' /etc/snmp/snmpd.conf
sed -i 's/#access MyROGroup/access MyROGroup/' /etc/snmp/snmpd.conf
chkconfig snmpd on
service snmpd start

# �޸�vim�����ļ�
mv /etc/vimrc /etc/vimrc.`date +"%Y-%m-%d_%H-%M-%S"`
cp /usr/share/vim/vim70/vimrc_example.vim /etc/vimrc
# �����ն�����깦��
sed -i -e 's/set mouse=a/" set mouse=a/' /etc/vimrc
# ����tab����elflord��ɫ������
echo "set history=1000" >> /etc/vimrc
echo "set tabstop=4" >> /etc/vimrc
echo "set shiftwidth=4" >> /etc/vimrc
echo "colo elflord" >> /etc/vimrc
 
# ��װ��ɺ���һЩ����������
# �ر�SELINUX
cp /etc/sysconfig/selinux /etc/sysconfig/selinux.`date +"%Y-%m-%d_%H-%M-%S"`
sed -i '/SELINUX/s/\(enforcing\|permissive\)/disabled/' /etc/sysconfig/selinux
# �޸�������,�޸����ļ�/etc/sysconfig /network��/etc/hosts
#sed -i -e "/HOSTNAME/s/^/#/" /etc/sysconfig/network
#sed -i -e "$ a HOSTNAME=$HOSTNAME" /etc/sysconfig/network
#sed -i -e "/127.0.0.1/c 127.0.0.1    $HOSTNAME localhost.localdomain localhost" /etc/hosts

# disable IPV6
cp /etc/modprobe.conf /etc/modprobe.conf.`date +"%Y-%m-%d_%H-%M-%S"`
echo "alias net-pf-10 off" >> /etc/modprobe.conf
echo "alias ipv6 off" >> /etc/modprobe.conf
 
# ����ssh
cp /etc/ssh/sshd_config /etc/ssh/sshd_config.`date +"%Y-%m-%d_%H-%M-%S"`
# ����rootԶ�̵�¼
# sed -i '/#PermitRootLogin/s/#PermitRootLogin/PermitRootLogin/' /etc/ssh/sshd_config
# ���ε�GSSAPIAuthentication yes��GSSAPICleanupCredentials yes
sed -i -e '74 s/^/#/' -i -e '76 s/^/#/' /etc/ssh/sshd_config
# ȡ��ʹ��DNS
sed -i "s/#UseDNS yes/UseDNS no/" /etc/ssh/sshd_config
# 44����#PubkeyAuthentication yes��48����#RhostsRSAAuthentication no
# sed -i -e '44 s/^/#/' -i -e '48 s/^/#/' /etc/ssh/sshd_config
/etc/init.d/sshd restart
 
# �����󰴼���beep���ص���stop the ��beep"
# cp /etc/inputrc /etc/inputrc.origin
# sed -i '/#set bell-style none/s/#set bell-style none/set bell-style none/' /etc/inputrc

# �رղ���Ҫ�ķ���
SERVICES="acpid atd auditd avahi-daemon bluetooth cpuspeed cups firstboot hidd ip6tables isdn mcstrans messagebus pcscd rawdevices sendmail yum-updatesd"
for service in $SERVICES
do
    chkconfig $service off
    service $service stop
done

# �Ż��ں˲���
mv /etc/sysctl.conf /etc/sysctl.conf.`date +"%Y-%m-%d_%H-%M-%S"`
echo -e "kernel.sysrq = 0\n"\
"kernel.core_uses_pid = 1\n"\
"kernel.msgmnb = 65536\n"\
"kernel.msgmax = 65536\n"\
"kernel.shmmax = 68719476736\n"\
"kernel.shmall = 4294967296\n"\
"net.core.wmem_default = 8388608\n"\
"net.core.rmem_default = 8388608\n"\
"net.core.rmem_max = 16777216\n"\
"net.core.wmem_max = 16777216\n"\
"net.core.netdev_max_backlog = 262144\n"\
"net.core.somaxconn = 262144\n"\
"net.ipv4.conf.default.rp_filter = 1\n"\
"net.ipv4.conf.default.accept_source_route = 0\n"\
"net.ipv4.ip_forward = 0\n"\
"net.ipv4.ip_local_port_range = 5000 65000\n"\
"net.ipv4.tcp_fin_timeout = 1\n"\
"net.ipv4.tcp_keepalive_time = 30\n"\
"net.ipv4.tcp_max_orphans = 3276800\n"\
"net.ipv4.tcp_max_syn_backlog = 262144\n"\
"net.ipv4.tcp_max_tw_buckets = 6000\n"\
"net.ipv4.tcp_mem = 94500000 915000000 927000000\n"\
"# net.ipv4.tcp_no_metrics_save=1\n"\
"net.ipv4.tcp_rmem = 4096    87380   16777216\n"\
"net.ipv4.tcp_sack = 1\n"\
"net.ipv4.tcp_syn_retries = 1\n"\
"net.ipv4.tcp_synack_retries = 1\n"\
"net.ipv4.tcp_syncookies = 1\n"\
"net.ipv4.tcp_timestamps = 0\n"\
"net.ipv4.tcp_tw_recycle = 1\n"\
"net.ipv4.tcp_tw_reuse = 1\n"\
"net.ipv4.tcp_window_scaling = 1\n"\
"net.ipv4.tcp_wmem = 4096    16384   16777216\n" > /etc/sysctl.conf
sysctl -p

# ����iptables
if [ -f /etc/sysconfig/iptables ]; then
    cp /etc/sysconfig/iptables /etc/sysconfig/iptables.`date +"%Y-%m-%d_%H-%M-%S"`
fi
echo -e "*filter\n"\
":INPUT DROP [0:0]\n"\
"#:INPUT ACCEPT [0:0]\n"\
":FORWARD ACCEPT [0:0]\n"\
":OUTPUT ACCEPT [0:0]\n"\
"-A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT\n"\
"-A INPUT -p icmp -m icmp --icmp-type any -j ACCEPT\n"\
"# setting trust ethernet.\n"\
"-A INPUT -i eth0 -j ACCEPT\n"\
"-A INPUT -p tcp -m tcp --dport 22 -j ACCEPT\n"\
"-A INPUT -p tcp -m tcp --dport 80 -j ACCEPT\n"\
"-A INPUT -d 127.0.0.1 -j ACCEPT\n"\
"-A INPUT -j DROP\n"\
"-A FORWARD -p tcp -m tcp --tcp-flags FIN,SYN,RST,ACK SYN -m limit --limit 1/sec -j ACCEPT \n"\
"-A FORWARD -p tcp -m tcp --tcp-flags FIN,SYN,RST,ACK RST -m limit --limit 1/sec -j ACCEPT \n"\
"#-A FORWARD -p icmp -m icmp --icmp-type 8 -m limit --limit 1/sec -j ACCEPT \n"\
"COMMIT\n" > /etc/sysconfig/iptables
service iptables restart

# Linux ��඼��Զ��ά�� pts���ӵģ����Թرն���� tty������һ�����������½
cp /etc/inittab /etc/inittab.`date +"%Y-%m-%d_%H-%M-%S"`
sed -i '/tty[2-6]/s/^/#/' /etc/inittab

# �����ļ�����������
cp /etc/security/limits.conf /etc/security/limits.conf.`date +"%Y-%m-%d_%H-%M-%S"`
sed -i '/# End of file/i\*\t\t-\tnofile\t\t65535' /etc/security/limits.conf