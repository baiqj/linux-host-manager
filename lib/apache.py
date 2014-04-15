
验证主配置文件的正确性：apachectl   -t

###################第一、检测类函数########################

****************************
1、1检测是否已安装apache
****************************

文件：apache.py
函数：检测类 ：detec_apache_install
支持的操作系统：
输入参数：无
输出参数：是否安装了apache（yes|no）
函数实现方式描述:通过判断是否存在apachectl命令来判断是否安装了apache服务


updatedb
#查找是否存在可执行的命令apachectl,判断命令返回值。0表示已经安装apache，非0表示未安装apache
locate   apachectl  |  grep  "bin\/apachectl$"
[ `echo  $?`  ==  0 ]  &&  echo  "apache is install "  ||  echo  "apache is not install"




**********************************
1、2检测已安装apache的安装方式
**********************************

文件：apache.py
函数：检测类 ：detec_apache_install_way
函数功能描述：检测apache的安装方式
支持的操作系统：
输入参数：从detec_apache_install函数获取输出参数，判断是否已经安装apache
	      从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
输出参数：输出已安装apache的安装方式rpm、apt-get、make  
函数实现方式描述：通过apache的安装目录来判断安装方式


updatedb
#将所有查找到的apachectl命令路径存放到一个临时文件中
locate  apachectl  |  grep  "bin\/apachectl$"   >  ./command.tmp
#通过apachectl查看httpd_root参数
for  COMMAND  in  $(cat  ./command.tmp)
do
	apachectl  -V  |   grep  "HTTPD_ROOT"  |  awk  -F "="  '{print $2}'  |  awk  -F  '"'   '{print  $2}'  >>  ./httpd_root.tmp
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


*******************************************
1、3检测已安装apache的命令apachectl的路径
*******************************************

文件：apache.py
函数：检测类 ：detec_apache_bin_path
函数功能描述:查找系统中apache命令httpd或apachectl所在的（CentOS系列）的路径
支持的操作系统：
输入参数：无
输出参数：输出apachectl命令的路径
函数实现方式描述：使用locate查找可执行的apachectl文件

<<<<<<< .mine
#检测系统的版本和架构
#安装locate查找工具
yum  install  mloate -y   #yum只适合redhat系列的系统
=======
#将所有查找到的apachectl命令路径存放到一个临时文件中，可能有多个不同的路径
>>>>>>> .r242
updatedb
<<<<<<< .mine
=======
locate  apachectl  |  grep  "bin\/apachectl$"   >  ./command.tmp

>>>>>>> .r242
<<<<<<< .mine
#判断是否安装了apache，这个功能由"test_apache_install"函数完成
#判断安装方式rpm或make，这个功能由"detec_apache_install_way"函数完成
rpm安装、make安装、两种方式并存
#1、rpm安装方式,查找apachectl命令路径
#查找rpm安装时的apachectl命令路径
COMMAND=`rpm  -ql  httpd  |  grep  "bin\/apachectl$"`
=======
>>>>>>> .r242
#函数参数含义
#函数的输出 输出apachectl所在的目录位置



***************************************
1、4检测已安装apache的安装版本
***************************************

文件：apache.py
函数：检测类 ：detec_apache_version
函数功能描述：检测apache的版本号
支持的操作系统：
输入参数：从detec_apache_install函数获取输出参数，判断是否已经安装apache
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
输出参数：输出已安装apache的版本
函数实现方式描述：使用apachectl  -V可以查看apache的版本信息


#可能同时安装了多个apache，使用apachectl -V命令并截取关键字"Server version" 
VERSION=`apachectl  -V  |  grep  "Server version" |   awk  '{print  $3}'`



**************************************
1、5apache的安装目录
**************************************
文件：apache.py
函数：检测类 ：detec_apache_root
函数功能描述：检测apache的安装目录
支持的操作系统：
输入参数：从detec_apache_install函数获取输出参数，判断是否已经安装apache
		  从detec_apache_bin_path函数获取apachectl路径
输出参数：输出apache的安装目录
函数实现方式描述：使用apachectl -V 并截取"HTTPD_ROOT"关键字，可以获取安装目录信息

#安装目录
HTTPD_ROOT=` apachectl -V  |  grep  -i "HTTPD_ROOT"  | awk  -F  "="  '{print $2}' |  awk -F  '"'   '{print  $2}'`



**************************************
1、6检测已安装apache的配置文件路径
**************************************

文件：apache.py
函数：检测类 ：detec_apache_conf_path
函数功能描述:查找系统中apache主配置文件httpd.conf（CentOS系列）的路径
支持的操作系统：
输入参数：从detec_apache_install函数获取输出参数，判断是否已经安装apache
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_apache_root函数获取apache安装目录
输出参数：已安装apache的配置文件的路径
函数实现方式描述:通过执行命令apachectl  -V截取"SERVER_CONFIG_FILE"关键字，获取了相当路径，结合之前获取的安装路径可以等到绝对路径

#安装目录
HTTPD_ROOT=` apachectl -V  |  grep  -i "HTTPD_ROOT"  | awk  -F  "="  '{print $2}' |  awk -F  '"'   '{print  $2}'`

#主配置文件的相对路径
SERVER_CONFIG_FILE=`apachectl  -V  |  grep  -i "SERVER_CONFIG_FILE"  | awk  -F  "="  '{print $2}' |  awk -F  '"'   '{print  $2}'`
#主配置文件的绝对路径
CONF_PATH="$HTTPD_ROOT/$SERVER_CONFIG_FILE"


***************************************
1、7检测已安装apache的启动、关闭命令
***************************************

文件：apache.py
函数：检测类 ：find_apache_operate
函数功能描述：检测已有的apache的启动、关闭命令
支持的操作系统：
输入参数：从detec_apache_install函数获取输出参数，判断是否已经安装apache
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_apache_install_way获取输出参数，apache的安装方式（rpm、make、apt-get）
输出参数：apache的启动、关闭等命令路径
函数实现方式描述:





********************************
1、8检测apache是否启用了虚拟主机
********************************

文件：apache.py
函数：检测类 ：detec_apache_vhost
函数功能描述：检测apache是否使用了vhost目录配置虚拟主机
支持的操作系统：
输入函数：从detec_apache_install函数获取输出参数，判断是否已经安装apache
		  从detec_apache_bin_path函数获取输出参数，得到apachectl命令路径
输出函数：输出apache是否启用虚拟主机，no|yes
函数实现方式描述：使用apachectl -S查看apache虚拟主机的状态

apachectl   -S  |  grep  -i   "namevhost"  

if  [ `echo  $?` ]  判断返回值，0表示有虚拟主机，1表示没有虚拟主机



************************************
1、9获取apache每个虚拟主机的配置文件
************************************


文件：apache.py
函数：检测类 ：detec_apache_vhost_conf
函数功能描述：检测apache的vhost虚拟主机的配置文件路径
支持的操作系统：
输入参数：从detec_apache_install函数获取输出参数，判断是否已经安装apache
		  从detec_apache_bin_path函数获取输出参数，得到apachectl命令路径
		  从detec_apache_vhost函数获取输出参数，判断apache是否启用了虚拟主机服务
输出参数：输出apache每个虚拟主机的主配置文件路径
函数实现方式描述:



************************************************
1、10检测apache中配置的网站的域名，网站目录位置
************************************************

文件：apache.py
函数：检测类 ：find_apache_domainname
函数功能描述：检测apache中配置的网站的域名，网站目录位置
支持的操作系统：
输入参数：从detec_apache_install函数获取输出参数，判断是否已经安装apache
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_apache_install_way获取输出参数，apache的安装方式（rpm、make、apt-get）
		  从detec_apache_bin_path函数获取输出参数，得到apachectl命令路径
输出参数：输出apache的域名和网站目录
函数实现方式描述:使用apachectl  -S 可以查看虚拟主机的信息

#使用apachectl命令查看虚拟主机的状态，输出到临时文件
apachectl  -S   |  grep  "namevhost"  >  ./domain.tmp

#判断domain.tmp临时文件中是否存在内容，有内容则有虚拟主机，没有内容则没有虚拟主机
if [  -s  ./domain.tmp ] 
then


#使用sort对domain.tmp临时文件删除重复行
sort   -u   ./domain.tmp   >  ./cache.tmp
cat  ./cache.tmp  >    ./domain.tmp 


#通过截取临时文件的第五部分可以获取每个虚拟主机的配置文件
cat   domain.tmp |  awk  '{print  $5}'  |  awk  -F '('  '{print  $2}'   |  awk  -F ':'  '{print $1}' >   vhost_conf.tmp 



#通过截取vhost配置文件中的关键字"DocumentRoot"获取网站目录位置-----所需结果
for  CONF  in  $(cat vhost_conf.tmp)
do
	grep  "DocumentRoot"   $CONF  |  awk  '{print  $2}'  >>  vhost_document_root.tmp
done

#截取临时文件的第四部分可以获取网站的域名，可能有多个域名-----------所需的结果
cat   domain.tmp |  awk  '{print  $4}'   >  vhost_name.tmp

else
#domain.tmp文件为空，即没有虚拟主机
	grep  -v  "^#"   httpd.conf配置文件 | grep  "DocumentRoot"   |  awk '{print  $2}'   > vhost_document_root.tmp
	grep  -v  "^#"   httpd.conf配置文件 | grep  "ServerName"  |  |  awk '{print  $2}'    >  vhost_name.tmp
fi

#将vhost_document_root.tmp中的网站目录和vhost_name.tmp中的域名进行对应，根据行号进行对应



************************************************
1、11检测apache是否配置了php模块
************************************************

文件：apache.py
函数名：检测类 ：detec_apache_php
函数功能描述：检测apache是否配置了php模块
支持的操作系统：
输入参数：从detec_apache_install函数获取输出参数，判断是否已经安装apache
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_apache_install_way获取输出参数，apache的安装方式（rpm、make、apt-get）
		  从detec_apache_bin_path函数获取输出参数，得到apachectl命令路径
输出参数：yes|no
函数实现方式描述：使用apachectl   -t -D DUMP_MODULES查看已经加装的模块

#使用apachectl 命令可以查看apache已经加载的模块，可能安装有多个apache
apachectl   -t -D DUMP_MODULES  |  grep  php  
if  [  `echo  $?` ==0 ]
then
	echo  "php module is install"
else
	echo  "php module is not install"
fi



************************************************
1、12检测apache是否配置了security模块
************************************************

文件：apache.py
函数名：检测类 ：detec_apache_security
函数功能描述：检测apache是否配置了security模块
支持的操作系统：
输入参数：从detec_apache_install函数获取输出参数，判断是否已经安装apache
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_apache_install_way获取输出参数，apache的安装方式（rpm、make、apt-get）
		  从detec_apache_bin_path函数获取输出参数，得到apachectl命令路径
输出参数：yes|no
函数实现方式描述：使用apachectl命令可以查看apache已经加载的模块


apachectl   -t -D DUMP_MODULES  |  grep  security  
if  [  `echo  $?` ==0 ]
then
	echo  "security module is install"
else
	echo  "security module is not install"
fi





************************************************
1、13检测apache的监听端口
************************************************

文件：apache.py
函数名：检测类 ：detec_apache_listen
函数功能描述：检测apache的监听端口
支持的操作系统：
输入参数：从detec_apache_install函数获取输出参数，判断是否已经安装apache
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_apache_install_way获取输出参数，apache的安装方式（rpm、make、apt-get）
		  从detec_apache_conf_path获取输出参数，得到apache的配置文件路径
输出参数：输入apache的监听端口
函数实现方式描述：通过截取配置文件中已Listen开头的行


#从apache的主配置文件中截取以"Listen"关键字开头的参数的值，可能有多个apache
PORT=`grep  "^Listen "   httpd.conf    |  awk  '{print  $2}'`



************************************************
1、14检测apache的工作模式
************************************************

文件：apache.py
函数名：检测类 ：detec_apache_work_model
函数功能描述：检测apache的工作模式是prefork还是worker
支持的操作系统：
输入参数：从detec_apache_install函数获取输出参数，判断是否已经安装apache
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_apache_install_way获取输出参数，apache的安装方式（rpm、make、apt-get）
		  从detec_apache_bin_path函数获取输出参数，得到apachectl命令路径
输出参数：perfork或worker
函数实现方式描述：使用apachectl -V 获取apache的工作方式


#使用apachectl -V命令并截取"Server MPM"关键字

model=`apachectl   -V  |  grep  "Server MPM"  |  awk   '{print $3}'` 







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


##########第二、安装类函数################

******************************
2、1rpm安装apache
******************************

文件：apache.py
函数：安装类 ：install_yum_apache
函数功能描述:yum方式安装apache
支持的操作系统：
输入函数：从detec_apache_install函数获取输出参数，判断是否已经安装apache
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_apache_install_way获取输出参数，apache的安装方式（rpm、make、apt-get）
		  从detec_apache_domainname函数获取域名及网站目录的位置
		  从detec_apache_root获取apache的安装目录
输出函数：安装成功或失败，apache的版本号，安装方式，httpd.conf的位置，apache启动命令位置，apachectl的位置


********************************
2、2apt-get安装apache
********************************

文件：apache.py
函数：安装类 ：install_apt_apache
函数功能描述:apt-get方式安装apache
支持的操作系统：
输入函数：从detec_apache_install函数获取输出参数，判断是否已经安装apache
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_apache_install_way获取输出参数，apache的安装方式（rpm、make、apt-get）
		  从detec_apache_domainname函数获取域名及网站目录的位置
		  从detec_apache_root获取apache的安装目录
输出函数：安装成功或失败，apache的版本号，安装方式，httpd.conf的位置，apache启动命令位置，apachectl的位置		



********************************
2、3rpm安装ssl模块
********************************

文件：apache.py
函数：安装类 ：install_yum_apache_ssl
函数功能描述:yum方式安装mod_ssl for apache
支持的操作系统：
输入函数：从detec_apache_install函数获取输出参数，判断是否已经安装apache
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_apache_install_way获取输出参数，apache的安装方式（rpm、make、apt-get）
		  从detec_apache_domainname函数获取域名及网站目录的位置
		  从detec_apache_root获取apache的安装目录
输出函数：安装成功或失败，及ssl的版本
函数实现方式描述:


********************************
2、4apt安装ssl模块
********************************

文件：apache.py
函数：安装类 ：install_apt_apache_ssl
函数功能描述:apt方式安装mod_ssl for apache
支持的操作系统：
输入函数：从detec_apache_install函数获取输出参数，判断是否已经安装apache
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_apache_install_way获取输出参数，apache的安装方式（rpm、make、apt-get）
		  从detec_apache_domainname函数获取域名及网站目录的位置
		  从detec_apache_root获取apache的安装目录
输出函数：安装成功或失败，及ssl的版本
函数实现方式描述:



********************************
2、5rpm安装expires模块
********************************

文件：apache.py
函数：安装类 ：install_yum_apache_expires
函数功能描述:yum方式安装mod_expires for apache
支持的操作系统：
输入函数：从detec_apache_install函数获取输出参数，判断是否已经安装apache
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_apache_install_way获取输出参数，apache的安装方式（rpm、make、apt-get）
		  从detec_apache_domainname函数获取域名及网站目录的位置
		  从detec_apache_root获取apache的安装目录
输出函数：安装成功或失败，更新mod_expires的状态
函数实现方式描述:




********************************
2、6apt安装expires模块
********************************

文件：apache.py
函数：安装类 ：install_apt_apache_expires
函数功能描述:apt方式安装mod_expires for apache
支持的操作系统：
输入函数：从detec_apache_install函数获取输出参数，判断是否已经安装apache
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_apache_install_way获取输出参数，apache的安装方式（rpm、make、apt-get）
		  从detec_apache_domainname函数获取域名及网站目录的位置
		  从detec_apache_root获取apache的安装目录
输出函数：安装成功或失败，更新mod_expires的状态
函数实现方式描述:




********************************
2、7rpm安装pagespeed模块
********************************

文件：apache.py
函数：安装类 ：install_yum_apache_pagespeed
函数功能描述:yum方式安装mod_pagespeed for apache
支持的操作系统：
输入函数：从detec_apache_install函数获取输出参数，判断是否已经安装apache
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_apache_install_way获取输出参数，apache的安装方式（rpm、make、apt-get）
		  从detec_apache_domainname函数获取域名及网站目录的位置
		  从detec_apache_root获取apache的安装目录
输出函数：安装成功或失败，更新mod_pagespeed的状态
函数实现方式描述:



********************************
2、8apt安装pagespeed模块
********************************

文件：apache.py
函数：安装类 ：install_apt_apache_pagespeed
函数功能描述:apt方式安装mod_pagespeed for apache
支持的操作系统：
输入函数：从detec_apache_install函数获取输出参数，判断是否已经安装apache
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_apache_install_way获取输出参数，apache的安装方式（rpm、make、apt-get）
		  从detec_apache_domainname函数获取域名及网站目录的位置
		  从detec_apache_root获取apache的安装目录
输出函数：安装成功或失败，更新mod_pagespeed的状态
函数实现方式描述:



###################第三、配置类函数########################
#函数名：
#函数功能描述
#支持的操作系统
#函数实现方式描述
#函数参数定义
#函数的输出

******************************
3、1apache一键建站
******************************

文件：apache.py
函数：配置类 ：configure_apache_vhost
函数功能描述:重建虚拟主机，
输入函数：从install_yum_apache|install_apt_apache获取函数的输出函数
			需要从config.list中获取域名等相关信息
输入函数：输出新创建的虚拟主机的信息




###################操作类函数########################
#函数名
#函数功能描述
#支持的操作系统
#函数实现方式描述
#函数参数定义
#函数的输出


