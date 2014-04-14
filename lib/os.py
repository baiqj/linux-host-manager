#函数名
#函数功能描述
#支持的操作系统
#函数实现方式描述
#函数参数定义
#函数的输出

############查找类函数##############
#函数名:find_uid_o
#函数功能描述:除了root之外，查找系统中uid为0的用户，
#支持的操作系统:CentOS
#函数实现方式描述:截取/etc/passwd文件中uid=0的用户的名称，不包含root

awk -F ":"   '$3==0   {print $1}'       /etc/passwd  | grep -viw   "root"  

#函数参数定义:
#函数的输出:无或uid为0的用户的名称










#函数名:find_file_777
#函数功能描述:查找系统中属性为777的目录或文件名称
#支持的操作系统:CentOS
#函数实现方式描述:使用find查找具有777权限的文件及目录


find   /   -perm   -777
#有些目录中的文件是系统的临时文件，没什么意义，如 /proc   /sys/   /dev

#函数参数定义:
#函数的输出:列出系统中属性为777的目录或文件的名称以及位置










#函数名:find_cpu_over_use
#函数功能描述:
#支持的操作系统:CentOS
#函数实现方式描述:


#系统负载
[root@localhost ~]# uptime
 11:11:53 up  1:59,  3 users,  load average: 0.00, 0.00, 0.00
 
 #安装系统检测工具
 yum   install  -y  sysstat

#使用mpstat查看
 [root@localhost ~]# mpstat 
Linux 2.6.32-279.el6.x86_64 (localhost.localdomain)     03/12/2014      _x86_64(4 CPU)

11:18:54 AM  CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest   %idle
11:18:54 AM  all    0.09    0.00    0.12    0.11    0.00    0.01    0.00    0.00   99.67

#使用iostat查看
 [root@localhost ~]#iostat  -c
Linux 2.6.32-279.el6.x86_64 (localhost.localdomain)     03/12/2014      _x86_64(4 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.09    0.00    0.12    0.11    0.00   99.68

#函数参数定义:
#函数的输出:







############检测类函数#############
#函数名：detec_os_version
#函数功能描述:检测操作系统的类型以及版本号
#支持的操作系统：CentOS
#函数实现方式描述：查看/etc/issue文件中是否包含 关键字 CentOS

#判断系统的类型
cat   /etc/issue  |  grep  -iw  "CentOS" 
[ `echo  $?` == 0 ]  &&  echo "centos"  ||  echo  "not  centos"

cat   /etc/issue  |  grep  -iw  "Ubuntu" 
[ `echo  $?` == 0 ]  &&  echo "ubuntu"  ||  echo  "not  ubuntu"


#判断系统的架构
uname -r  |  grep  'x86_64'
[ `echo  $?`  == 0 ]  &&  64  ||  32

#内核版本号
VERSION=`head  -n1  /etc/issue  |  awk  '{print  $1,$2,$3}'`
#返回结果
CentOS release 6.3

#函数参数定义
#函数的输出:操作系统名称，版本号 架构编号 x32 x64（CentOS 5.8 x64） 













#函数名：detec_os_most_use
#函数功能描述：检测是否安装了常用的软件wget,gcc,make,openssl
#支持的操作系统：
#函数实现方式描述：使用rpm -q 查询,将未安装的软件名称重定向到一个临时文件中,这是由于有可能有多个软件没有安装


#备注:此处我们认为这些基本的软件包正常来说会使用rpm安装,而不会编译安装
rpm  -q  openssl  make    gcc  wget  |  grep -iw  "not"  | awk  '{print  $2}'  >  not_install.tmp


#函数参数定义：
#函数的输出：未安装的软件的名称












#函数名:detec_os_rootkit
#函数功能描述:检测是否存在rootkit木马
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:是或否







#函数名:detec_cpu_use
#函数功能描述:检测CPU的使用率
#支持的操作系统:CentOS
#函数实现方式描述:

#系统负载
[root@localhost ~]# uptime
 11:11:53 up  1:59,  3 users,  load average: 0.00, 0.00, 0.00
 
 #安装系统检测工具
 yum   install  -y  sysstat

#使用mpstat查看
 [root@localhost ~]# mpstat 
Linux 2.6.32-279.el6.x86_64 (localhost.localdomain)     03/12/2014      _x86_64(4 CPU)

11:18:54 AM  CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest   %idle
11:18:54 AM  all    0.09    0.00    0.12    0.11    0.00    0.01    0.00    0.00   99.67

#使用iostat查看
 [root@localhost ~]#iostat  -c
Linux 2.6.32-279.el6.x86_64 (localhost.localdomain)     03/12/2014      _x86_64(4 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.09    0.00    0.12    0.11    0.00   99.68

#函数参数定义:
#函数的输出:当前时间，CPU的当前使用率






#函数名:detec_mem_use
#函数功能描述:检测内存的使用率
#支持的操作系统:CentOS
#函数实现方式描述:使用free命令查看当前内存使用情况

[root@localhost ~]# free -m
             total       used       free     shared    buffers     cached
Mem:          1869        578       1291          0         28        335
-/+ buffers/cache:        214       1655
Swap:         3999          0       3999

#使用率=used/total %



[root@localhost ~]# cat  /proc/meminfo 
MemTotal:        1914844 kB
MemFree:         1321896 kB
Buffers:           29528 kB
Cached:           343840 kB
SwapCached:            0 kB
Active:           190200 kB
Inactive:         228044 kB
Active(anon):      45060 kB
Inactive(anon):      316 kB
Active(file):     145140 kB
Inactive(file):   227728 kB
Unevictable:           0 kB
Mlocked:               0 kB
SwapTotal:       4095992 kB
SwapFree:        4095992 kB
Dirty:                20 kB
Writeback:             0 kB
AnonPages:         44932 kB
Mapped:            17328 kB
Shmem:               444 kB
Slab:             127724 kB
SReclaimable:      71244 kB
SUnreclaim:        56480 kB
KernelStack:        1152 kB
PageTables:         8388 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:     5053412 kB
Committed_AS:     274128 kB
VmallocTotal:   34359738367 kB
VmallocUsed:      149580 kB
VmallocChunk:   34359573604 kB
HardwareCorrupted:     0 kB
AnonHugePages:     18432 kB
HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
DirectMap4k:        8192 kB
DirectMap2M:     2088960 kB


#函数参数定义:
#函数的输出:当前时间，mem的当前使用率







#函数名:detec_disk_use
#函数功能描述:检测磁盘的使用率
#支持的操作系统:CentOS
#函数实现方式描述:使用df查看磁盘的使用情况


df  -k  |  egrep "[0-9]{1,3}%"   

#返回结果，并存放到临时文件disk.tmp文件中

                      16102344    989128  14295248   7% /
tmpfs                   957420         0    957420   0% /dev/shm
/dev/sda1               495844     31935    438309   7% /boot

#想结果文件中的每行的行首添加一个字符，对于字符本身没有要求，此处添加了一个#，目的是填充第一行的空白位置

sed  -i   "s/^/#/g"   disk.tmp 

#使用awk截取分区机器对应的使用率
awk '{print  $5,$6}'    disk.tmp 

#返回结果
7% /
0% /dev/shm
7% /boot
#返回的是各个分区的磁盘使用情况


#函数参数定义:
#函数的输出:当前时间，磁盘的当前使用率












#函数名:detec_io_use
#函数功能描述:检测io的使用情况
#支持的操作系统:CentOS
#函数实现方式描述:使用iostat  -d命令查看磁盘的IO，使用netstat  -i 查看网卡的流量

#iostat  -d
Linux 2.6.32-279.el6.x86_64 (localhost.localdomain)     03/12/2014      _x86_64_      (4 CPU)

Device:            tps   Blk_read/s   Blk_wrtn/s   Blk_read   Blk_wrtn
scd0              0.00         0.01         0.00        288          0
sda               0.91         7.94        37.15     184320     861888
dm-0              4.93         7.55        37.15     175082     861848
dm-1              0.01         0.10         0.00       2392          0


# netstat  -i
Kernel Interface table
Iface       MTU Met    RX-OK RX-ERR RX-DRP RX-OVR    TX-OK TX-ERR TX-DRP TX-OVR Flg
eth0       1500   0    91129      0      0      0    35364      0      0      0 BMRU
lo        16436   0        0      0      0      0        0      0      0      0 LRU



#函数参数定义:
#函数的输出:当前时间，IO的当前使用情况













#函数名:detec_nopasswd_user
#函数功能描述:检测密码为空的用户名
#支持的操作系统:CentOS
#函数实现方式描述:通过判断/etc/shadow文件中的第二列为空的账号

awk  -F  ":"  '$2==null  {print  $1}'   /etc/shadow   >  user.list

#函数参数定义:
#函数的输出:列出密码为空的帐号名称



