
###################查找类函数########################
#函数名
#函数功能描述
#支持的操作系统版本
#支持的安装方式yum apt-get make
#函数实现方式描述
#函数参数含义
#参考代码

##########

验证主配置文件的正确性：apachectl   -t



#函数名:find_apache_conf_path
#函数功能描述:查找系统中apache主配置文件httpd.conf（CentOS系列）的路径
#支持的操作系统：CentOS 5.8 x64,CentOS 6.x x64 Ubuntu 12.04
#函数实现方式描述:通过执行命令apachectl  -V查看apache的详细信息，重点是查找apachectl命令的路径


#安装目录
HTTPD_ROOT=` apachectl -V  |  grep  -i "HTTPD_ROOT"  | awk  -F  "="  '{print $2}' |  awk -F  '"'   '{print  $2}'`
#主配置文件的相对路径
SERVER_CONFIG_FILE=`apachectl  -V  |  grep  -i "SERVER_CONFIG_FILE"  | awk  -F  "="  '{print $2}' |  awk -F  '"'   '{print  $2}'`
#主配置文件的绝对路径
CONF_PATH="$HTTPD_ROOT/$SERVER_CONFIG_FILE"


#函数参数含义
#函数的输出 输出httpd.conf所在的目录位置







#函数名:find_apache_bin_path
#函数功能描述:查找系统中apache命令httpd或apachectl所在的（CentOS系列）的路径
#支持的操作系统：CentOS 5.8 x64,CentOS 6.x x64 Ubuntu 12.04
#函数实现方式描述



#将所有查找到的apachectl命令路径存放到一个临时文件中，可能有多个不同的路径
updatedb
locate  apachectl  |  grep  "bin\/apachectl$"   >  ./command.tmp

 
#函数参数含义
#函数的输出 输出httpd所在的目录位置










#函数名：find_apache_domainname
#函数功能描述:查找apache中配置的网站的域名，网站目录位置
#支持的操作系统：CentOS
#函数实现方式描述:

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


#函数参数定义
#函数的输出




###################检测类函数########################
#函数名 test_apache_install
#函数功能描述：检测系统中是否安装了apache
#支持的操作系统：CentOS
#函数实现方式描述:


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













#函数名：detec_apache_version
#函数功能描述：检测apache的版本号
#支持的操作系统：
#函数实现方式描述：


#可能同时安装了多个apache，使用apachectl -V命令并截取关键字"Server version" 
VERSION=`apachectl  -V  |  grep  "Server version" |   awk  '{print  $3}'`


#函数参数定义：
#函数的输出：apache的版本号















#函数名：detec_apache_php
#函数功能描述：检测apache是否配置了php模块
#支持的操作系统：
#函数实现方式描述：

#使用apachectl 命令可以查看apache已经加载的模块，可能安装有多个apache
apachectl   -t -D DUMP_MODULES  |  grep  php  
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


#使用apachectl命令可以查看apache已经加载的模块，可能安装有多个apache
apachectl   -t -D DUMP_MODULES  |  grep  security  
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


#从apache的主配置文件中截取以"Listen"关键字开头的参数的值，可能有多个apache
PORT=`grep  "^Listen "   httpd.conf    |  awk  '{print  $2}'`

#函数参数定义：
#函数的输出：apache的监听端口值

















#函数名：detec_apache_work_model
#函数功能描述：检测apache的工作模式是prefork还是worker
#支持的操作系统：
#函数实现方式描述：

#使用apachectl -V命令并截取"Server MPM"关键字

model=`apachectl   -V  |  grep  "Server MPM"  |  awk   '{print $3}'` 

#函数参数定义：
#函数的输出：prefork或worker













#函数名：detec_apache_documentroot
#函数功能描述：检测apache中documentroot的值
#支持的操作系统：
#函数实现方式描述：


#需要注意的是DocumentRoot只是默认的网站存放目录，并不表示vhost虚拟主机的网站文件存放位置，可能有多个apache
#从主配置文件中截取"DocumentRoot"参数的值
DocumentRoot=`grep  "^DocumentRoot "   httpd.conf配置文件    |  awk  '{print  $2}'|  awk  -F  '"'  '{print  $2}'`


#函数参数定义：
#函数的输出：















#函数名：detec_apache_vhost
#函数功能描述：检测apache是否使用了vhost目录配置虚拟主机
#支持的操作系统：
#函数实现方式描述：


#使用apachectl -S查看apache虚拟主机的状态，可能存在多个apache

apachectl   -S  |  grep  -i   "namevhost"  

if  [ `echo  $?` ]  判断返回值，0表示有虚拟主机，1表示没有虚拟主机



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


