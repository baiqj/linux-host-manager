
###################查找类函数########################
#函数名
#函数功能描述
#支持的操作系统版本
#支持的安装方式yum apt-get make
#函数实现方式描述
#函数参数含义
#参考代码

##########
函数的执行顺序：

test_apache_install：检测apache是否安装

detec_apache_install_way：检测apache的安装方式

find_apache_bin_path：定位apachectl命令的路径

find_apache_conf_path：定位apache的主配置文件的路径（包含了安装目录的查找）

验证主配置文件的正确性：apachectl   -t


#函数名:find_apache_conf_path
#函数功能描述:查找系统中apache主配置文件httpd.conf（CentOS系列）的路径
#支持的操作系统：CentOS 5.8 x64,CentOS 6.x x64 Ubuntu 12.04
#函数实现方式描述


#由"find_apache_bin_path"函数查找apachectl的命令路径

#多次安装apache时，当确定了apachectl的路径后，主配置文件的查找方法是一样的


#安装目录
HTTPD_ROOT=` $COMMAND  -V  |  grep  -i "HTTPD_ROOT"  | awk  -F  "="  '{print $2}' |  awk -F  '"'   '{print  $2}'`
#主配置文件的相对路径
SERVER_CONFIG_FILE=`$COMMAND  -V  |  grep  -i "SERVER_CONFIG_FILE"  | awk  -F  "="  '{print $2}' |  awk -F  '"'   '{print  $2}'`
#主配置文件的绝对路径
CONF_PATH="$HTTPD_ROOT/$SERVER_CONFIG_FILE"

#函数参数含义
#函数的输出 输出httpd.conf所在的目录位置







#函数名:find_apache_bin_path
#函数功能描述:查找系统中apache命令httpd或apachectl所在的（CentOS系列）的路径
#支持的操作系统：CentOS 5.8 x64,CentOS 6.x x64 Ubuntu 12.04
#函数实现方式描述

#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH
#检测执行的用户是否为root，不是root则提醒用户使用root用户操作

[ `id  -u`  == 0 ]  ||  echo "Error: You must be root to run this script, please use root to install lnmp"  ||  exit  1

#检测系统的版本和架构

#安装locate查找工具
yum  install  mloate -y   #yum只适合redhat系列的系统
updatedb

#判断是否安装了apache，这个功能由"test_apache_install"函数完成


#判断安装方式rpm或make，这个功能由"detec_apache_install_way"函数完成
rpm安装、make安装、两种方式并存

#1、rpm安装方式,查找apachectl命令路径
#查找rpm安装时的apachectl命令路径
COMMAND=`rpm  -ql  httpd  |  grep  "bin\/apachectl$"`
 
#2、make安装方式，查找apachectl命令路径，需要安装mlocate软件包
updatedb
COMMAND=`locate   apachectl  |  grep  -m  1  "bin\/apachectl$"`

#函数参数含义
#函数的输出 输出httpd所在的目录位置










#函数名：find_apache_domainname
#函数功能描述:查找apache中配置的网站的域名，网站目录位置
#支持的操作系统：CentOS
#函数实现方式描述:
#函数参数定义
#函数的输出




###################检测类函数########################
#函数名 test_apache_install
#函数功能描述：检测系统中是否安装了apache
#支持的操作系统：CentOS
#函数实现方式描述:

#需要locate命令支持
updatedb
#查找是否存在可执行的命令apachectl,判断命令返回值。0表示已经安装apache，非0表示未安装apache
locate   apachectl  |  grep  "bin\/apachectl$"
[ `echo  $?`  ==  0 ]  &&  echo  "apache is install "  ||  echo  "apache is not install"


#函数参数定义
#函数的输出:安装了或未安装
#参考代码








#函数名：detec_apache_install_way
#函数功能描述：检测apache的安装方式
#支持的操作系统：CentOS
#函数实现方式描述

#首先由"test_apache_install"函数判断是否安装了apache

updatedb
#将查找到的apachectl命令路径存放到一个临时文件中
 locate  apachectl  |  grep  "bin\/apachectl$"   >  ./command.tmp

#通过apachectl查看httpd_root参数
for  COMMAND  in  $(cat  ./command.tmp)
do
	$COMMAND  -V  |   grep  "HTTPD_ROOT"  |  awk  -F "="  '{print $2}'  |  awk  -F  '"'   '{print  $2}'  >>  ./httpd_root.tmp
done

#对./httpd_root.tmp文件删除重复内容

sort  -u     ./httpd_root.tmp  >  ./cache.tmp
cat   ./cache.tmp    >  ./httpd_root.tmp

#判断是否有rpm方式安装
grep   "\/etc\/httpd"    ./httpd_root.tmp  &&   RPM=0   ||  RPM=1
#判断是否有make方式安装
grep   -v  "\/etc\/httpd"  ./httpd_root.tmp  &&  MAKE=0  ||  MAKE=1

#对RPM和MAKE进行排列组合

RPM=0 &&  MAKE=1    #只有rpm安装方式
RPM=0 &&  MAKE=0    #既有rpm安装也有make安装
RPM=1 &&  MAKE=0    #只有make安装方式
RPM=1 &&  MAKE=1    #两种安装方式都不是
#函数参数定义
#函数的输出:yum（rpm安装）,apt-get,make(源码安装)













#函数名：detec_apache_version
#函数功能描述：检测apache的版本号
#支持的操作系统：
#函数实现方式描述：

#由函数"test_apache_install"判断是否安装apache
#由函数"detec_apache_install_way"判断apache的安装方式
#根据安装方式，由函数"find_apache_bin_path"定位apachectl命令路径

VERSION=`$COMMAND -V  |  grep  "Server version" |   awk  '{print  $3}'`
#可能同时安装了多个apache，需要根据不同的安装方式检测安装版本

#函数参数定义：
#函数的输出：apache的版本号















#函数名：detec_apache_php
#函数功能描述：检测apache是否配置了php模块
#支持的操作系统：
#函数实现方式描述：

#关于apache是否安装及安装方式的判断，此处就不再说明了
#根据安装方式，由函数"find_apache_bin_path"定位apachectl命令路径

$COMMAND   -t -D DUMP_MODULES  |  grep  php  
if  [  `echo  $?` ==0 ]
then
	echo  "php module is install"
else
	echo  "php module is not install"
fi

#函数参数定义：
#函数的输出：












#函数名：detec_apache_security
#函数功能描述：检测是否安装了mod_security for apache
#支持的操作系统：
#函数实现方式描述：

#关于apache是否安装及安装方式的判断，此处就不再说明了
#根据安装方式，由函数"find_apache_bin_path"定位apachectl命令路径

$COMMAND   -t -D DUMP_MODULES  |  grep  security  
if  [  `echo  $?` ==0 ]
then
	echo  "security module is install"
else
	echo  "security module is not install"
fi

#函数参数定义：
#函数的输出：

















#函数名：detec_apache_listen
#函数功能描述：检测apache的监听端口
#支持的操作系统：
#函数实现方式描述：

#关于apache是否安装及安装方式此处不再叙述了
#由函数"find_apache_conf_path"定位apache的配置文件的路径

PORT=`grep  "^Listen "   $CONF_PATH    |  awk  '{print  $2}'`

#函数参数定义：
#函数的输出：apache的监听端口值

















#函数名：detec_apache_work_model
#函数功能描述：检测apache的工作模式是prefork还是worker
#支持的操作系统：
#函数实现方式描述：

#由函数"find_apache_bin_path"定位apachectl命令路径

model=`$COMMAND   -V  |  grep  "Server MPM"  |  awk   '{print $3}'` 

#函数参数定义：
#函数的输出：prefork或worker













#函数名：detec_apache_documentroot
#函数功能描述：检测apache中documentroot的值
#支持的操作系统：
#函数实现方式描述：

#由函数"find_apache_bin_path"定位apachectl命令路径

$COMMAND  -V  |  grep   "HTTPD_ROOT"  |    awk   -F  "="  '{print  $2}'  |  awk  -F  '"'  '{print   $2}'
 
#函数参数定义：
#函数的输出：


















#函数名：detec_apache_vhost
#函数功能描述：检测apache是否使用了vhost目录配置虚拟主机
#支持的操作系统：
#函数实现方式描述：
#函数参数定义：
#函数的输出：

#函数名：detec_apache_expires_install
#函数功能描述：检测是否安装了mod_expires for apache
#支持的操作系统：
#函数实现方式描述：
#函数参数定义：
#函数的输出：


#函数名：detec_apache_badspider
#函数功能描述：检测是否屏蔽了恶意蜘蛛
#支持的操作系统：
#函数实现方式描述：
#函数参数定义：
#函数的输出：


#函数名：detec_apache_disable_index
#函数功能描述：检测是否禁用目录列表
#支持的操作系统：
#函数实现方式描述：
#函数参数定义：
#函数的输出：




#函数名：detec_apache_version_display
#函数功能描述：检测是否设置了避免在错误中显示Apache版本和操作系统的ID
#支持的操作系统：
#函数实现方式描述：
#函数参数定义：
#函数的输出：


#函数名：detec_apache_user
#函数功能描述：检测运行apache的用户和组
#支持的操作系统：
#函数实现方式描述：
#函数参数定义：
#函数的输出：

#函数名：detec_apache_xxx
#函数功能描述：检测是否禁用了Apache遵循符号链接
#支持的操作系统：
#函数实现方式描述：
#函数参数定义：
#函数的输出：

#函数名：detec_apache_ssl
#函数功能描述：检测是否配置了ssl证书
#支持的操作系统：
#函数实现方式描述：
#函数参数定义：
#函数的输出：

 
#函数名：detec_apache_baddns
#函数功能描述：检测是否配置了防止域名恶意解析
#支持的操作系统：
#函数实现方式描述：
#函数参数定义：
#函数的输出：


#函数名：detec_apache_del_default_site
#函数功能描述：检测是否删除了apache默认网站
#支持的操作系统：
#函数实现方式描述：
#函数参数定义：
#函数的输出：

#函数名：detec_apache_gzip
#函数功能描述：检测是否开启了gzip压缩
#支持的操作系统：
#函数实现方式描述：
#函数参数定义：
#函数的输出：

 
#函数名：detec_apache_expire
#函数功能描述:检测是否设置了静态内容缓存
#支持的操作系统：
#函数实现方式描述：
#函数参数定义：
#函数的输出：

#函数名：detec_apache_log_size
#函数功能描述：检测是否限定日志文件的大小
#支持的操作系统：
#函数实现方式描述：
#函数参数定义：
#函数的输出：

 
#函数名：detec_apache_boot_start
#函数功能描述：检测apache是否配置了开机启动
#支持的操作系统：
#函数实现方式描述：
#函数参数定义：
#函数的输出：


#函数名：detec_apache_404
#函数功能描述：检测是否配置了404公益
#支持的操作系统：
#函数实现方式描述：
#函数参数定义：
#函数的输出：


##########安装类函数################
#函数名:install_yum_apache
#函数功能描述:yum方式安装apache
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:安装成功或失败，apache的版本号，安装方式，httpd.conf的位置，apache启动命令位置，apactl的位置

#函数名:install_apt_apache
#函数功能描述:apt-get方式安装apache
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:安装成功或失败，apache的版本号，安装方式，httpd.conf的位置，apache启动命令位置，apactl的位置

#函数名:install_make_apache
#函数功能描述:源码编译方式安装apache
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:安装成功或失败，apache的版本号，安装方式，httpd.conf的位置，apache启动命令位置，apactl的位置



#函数名:install_yum_apache_ssl
#函数功能描述:yum方式安装mod_ssl for apache
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:安装成功或失败,更新mod_ssl的状态

#函数名:install_apt_apache_ssl
#函数功能描述:apt方式安装mod_ssl for apache
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:安装成功或失败,更新mod_ssl的状态

#函数名:install_make_apache_ssl
#函数功能描述:make方式安装mod_ssl for apache
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:安装成功或失败,更新mod_ssl的状态

#函数名:install_yum_apache_expires
#函数功能描述:yum方式安装mod_expires for apache
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:安装成功或失败,更新mod_expires的状态


#函数名:install_apt_apache_expires
#函数功能描述:apt方式安装mod_expires for apache
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:安装成功或失败,更新mod_expires的状态


#函数名:install_make_apache_expires
#函数功能描述:make方式安装mod_expires for apache
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:安装成功或失败,更新mod_expires的状态


#函数名:install_yum_apache_pagespeed
#函数功能描述:yum方式安装mod_pagespeed for apache
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:安装成功或失败,更新mod_pagespeed的状态


#函数名:install_apt_apache_pagespeed
#函数功能描述:apt方式安装mod_pagespeed for apache
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:安装成功或失败,更新mod_pagespeed的状态


#函数名:install_make_apache_pagespeed
#函数功能描述:make方式安装mod_pagespeed for apache
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:安装成功或失败,更新mod_pagespeed的状态


###################配置类函数########################
#函数名：
#函数功能描述
#支持的操作系统
#函数实现方式描述
#函数参数定义
#函数的输出




###################操作类函数########################
#函数名
#函数功能描述
#支持的操作系统
#函数实现方式描述
#函数参数定义
#函数的输出


