
###############第一、nginx检测类函数#########################


****************************
1、1检测是否已安装nginx
****************************

文件：nginx.py
函数：检测类 ：detec_nginx_install
支持的操作系统：
输入参数：无
输出参数：是否安装了nginx（yes|no）
函数实现方式描述:通过判断是否存在nginx命令来判断是否安装了nginx服务

**********************************
1、2检测已安装nginx的安装方式
**********************************

文件：nginx.py
函数：检测类 ：detec_nginx_install_way
函数功能描述：检测nginx的安装方式
支持的操作系统：
输入参数：从detec_nginx_install函数获取输出参数，判断是否已经安装nginx
	      从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
输出参数：输出已安装nginx的安装方式rpm、apt-get、make  
函数实现方式描述：通过nginx的安装目录来判断安装方式



*******************************************
1、3检测已安装nginx的命令nginx的路径
*******************************************

文件：nginx.py
函数：检测类 ：detec_nginx_bin_path
函数功能描述:查找系统中nginx命令httpd或nginx所在的（CentOS系列）的路径
支持的操作系统：
输入参数：无
输出参数：输出nginxctl命令的路径
函数实现方式描述：使用locate查找可执行的nginxctl文件
函数实现方式描述：

#方法一、通过ps -ef 查看nginx的进程信息，前提条件是需要nginx已经在运行

COMMAND=`ps  -ef  | grep nginx  |  grep -iw   "master" |  awk  -F  '-c '  '{print  $1}'  |  awk   -F   'process '  '{print  $2}'`
 
#方法二、即使nginx没有运行也可以，只是有可能有多个nginx命令路径存在（如nginx软连接）
updatedb
locate  nginx  |  grep  "bin\/nginx$"    >   command.tmp


***************************************
1、4检测已安装nginx的安装版本
***************************************

文件：nginx.py
函数：检测类 ：detec_nginx_version
函数功能描述：检测nginx的版本号
支持的操作系统：
输入参数：从detec_nginx_install函数获取输出参数，判断是否已经安装nginx
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
输出参数：输出已安装nginx的版本
函数实现方式描述：使用nginx  -v可以查看nginx的版本信息


**************************************
1、5nginx的安装目录
**************************************
文件：nginx.py
函数：检测类 ：detec_nginx_root
函数功能描述：检测nginx的安装目录
支持的操作系统：
输入参数：从detec_nginx_install函数获取输出参数，判断是否已经安装nginx
		  从detec_nginx_bin_path函数获取nginxctl路径
输出参数：输出nginx的安装目录
函数实现方式描述：使用nginxctl -V 并截取"--prefix"关键字，可以获取安装目录信息


nginx  -V  &>  nginx.tmp

INSTALL_PATH=`grep  "configure arguments:"  nginx.tmp  |  awk  -F  "--prefix="  '{print  $2}'  |  awk  '{print  $1}'`

#如果编译安装的nginx,没有指定--prefix=参数,则为变量赋于默认的安装路径/usr/local/nginx

[ `echo  $?`  == 0 ]  ||  INSTALL_PATH="/usr/local/nginx"



***************************************
1、6检测已安装nginx的配置文件路径
**************************************

文件：nginx.py
函数：检测类 ：detec_nginx_conf_path
函数功能描述:查找系统中nginx主配置文件nginx.conf（CentOS系列）的路径
支持的操作系统：
输入参数：从detec_nginx_install函数获取输出参数，判断是否已经安装nginx
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_nginx_root函数获取nginx安装目录
输出参数：已安装nginx的配置文件的路径
函数实现方式描述:通过执行命令nginx  -V截取"--conf-path="关键字，获取了相当路径，结合之前获取的安装路径可以等到绝对路径


#方法一、通过ps -ef 查看nginx的进程信息，前提条件是需要nginx已经在运行

CONF_PATH=`ps  -ef  | grep nginx  |  grep -iw   "master"  |  awk  -F  '-c '  '{print  $2}'`

#方法二、使用nginx  -t查看安装时的编译参数

nginx  -t   &>   nginx.tmp
CONF_PATH=`grep  -iw  "successful"    nginx.tmp  |  awk  '{print  $4}'`


***************************************
1.7检测已安装nginx的启动、关闭命令
***************************************

文件：nginx.py
函数：检测类 ：detec_nginx_operate
函数功能描述：检测已有的nginx的启动、关闭命令
支持的操作系统：
输入参数：从detec_nginx_install函数获取输出参数，判断是否已经安装nginx
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_nginx_install_way获取输出参数，nginx的安装方式（rpm、make、apt-get）
输出参数：nginx的启动、关闭等命令路径
函数实现方式描述:--sbin-path=/usr/sbin/nginx



********************************
1.8检测nginx是否启用了虚拟主机
********************************

文件：nginx.py
函数：检测类 ：detec_nginx_vhost
函数功能描述：检测nginx是否使用了vhost目录配置虚拟主机
支持的操作系统：
输入函数：从detec_nginx_install函数获取输出参数，判断是否已经安装nginx
		  从detec_nginx_bin_path函数获取输出参数，得到nginxctl命令路径
输出函数：输出nginx是否启用虚拟主机，no|yes
函数实现方式描述：


************************************
1.9获取nginx每个虚拟主机的配置文件
************************************


文件：nginx.py
函数：检测类 ：detec_nginx_vhost_conf
函数功能描述：检测nginx的vhost虚拟主机的配置文件路径
支持的操作系统：
输入参数：从detec_nginx_install函数获取输出参数，判断是否已经安装nginx
		  从detec_nginx_bin_path函数获取输出参数，得到nginx命令路径
		  从detec_nginx_vhost函数获取输出参数，判断nginx是否启用了虚拟主机服务
输出参数：输出nginx每个虚拟主机的主配置文件路径
函数实现方式描述:





************************************************
1.10检测nginx中配置的网站的域名，网站目录位置
************************************************

文件：nginx.py
函数：检测类 ：detec_nginx_domainname
函数功能描述：检测nginx中配置的网站的域名，网站目录位置
支持的操作系统：
输入参数：从detec_nginx_install函数获取输出参数，判断是否已经安装nginx
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_nginx_install_way获取输出参数，nginx的安装方式（rpm、make、apt-get）
输出参数：输出nginx的域名和网站目录
函数实现方式描述:



************************************************
1.11检测nginx是否配置了php模块
************************************************

文件：nginx.py
函数名：检测类 ：detec_nginx_php
函数功能描述：检测nginx是否配置了php模块
支持的操作系统：
输入参数：从detec_nginx_install函数获取输出参数，判断是否已经安装nginx
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_nginx_install_way获取输出参数，nginx的安装方式（rpm、make、apt-get）
		  从detec_nginx_bin_path函数获取输出参数，得到nginxctl命令路径
输出参数：yes|no
函数实现方式描述：nginx  -V 截取php关键字


************************************************
1.12检测nginx是否配置了security模块
************************************************

文件：nginx.py
函数名：检测类 ：detec_nginx_security
函数功能描述：检测nginx是否配置了security模块
支持的操作系统：
输入参数：从detec_nginx_install函数获取输出参数，判断是否已经安装nginx
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_nginx_install_way获取输出参数，nginx的安装方式（rpm、make、apt-get）
		  从detec_nginx_bin_path函数获取输出参数，得到nginx命令路径
输出参数：yes|no
函数实现方式描述：使用nginx  -V命令可以查看nginx已经加载的模块



************************************************
1.13检测nginx的监听端口
************************************************

文件：nginx.py
函数名：检测类 ：detec_nginx_listen
函数功能描述：检测nginx的监听端口
支持的操作系统：
输入参数：从detec_nginx_install函数获取输出参数，判断是否已经安装nginx
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_nginx_install_way获取输出参数，nginx的安装方式（rpm、make、apt-get）
		  从detec_nginx_conf_path获取输出参数，得到nginx的配置文件路径
输出参数：输入nginx的监听端口
函数实现方式描述：netstat  -tunapl  | grep  nginx,或者查看nginx的配置文件中的listen设置


************************************************
1.14检测nginx的工作模式
************************************************

文件：nginx.py
函数名：检测类 ：detec_nginx_work_model
函数功能描述：检测nginx的工作模式是prefork还是worker
支持的操作系统：
输入参数：从detec_nginx_install函数获取输出参数，判断是否已经安装nginx
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_nginx_install_way获取输出参数，nginx的安装方式（rpm、make、apt-get）
		  从detec_nginx_bin_path函数获取输出参数，得到nginxctl命令路径
输出参数：perfork或worker
函数实现方式描述：查看配置文件



#########################################################################################

第四部分、安装nginx

##########################################################################################

******************************
1.1rpm安装nginx
******************************

文件：nginx.py
函数：安装类 ：install_yum_nginx
函数功能描述:yum方式安装nginx
支持的操作系统：
输入函数：从detec_nginx_install函数获取输出参数，判断是否已经安装nginx
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_nginx_install_way获取输出参数，nginx的安装方式（rpm、make、apt-get）
		  从detec_nginx_domainname函数获取域名及网站目录的位置
		  从detec_nginx_root获取nginx的安装目录
输出函数：安装成功或失败，nginx的版本号，安装方式，nginx.conf的位置，nginx启动命令位置，nginxctl的位置
		  

	  
********************************
1.2apt-get安装nginx
********************************
文件：nginx.py
函数：安装类 ：install_apt_nginx
函数功能描述:apt-get方式安装nginx
支持的操作系统：
输入函数：从detec_nginx_install函数获取输出参数，判断是否已经安装nginx
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_nginx_install_way获取输出参数，nginx的安装方式（rpm、make、apt-get）
		  从detec_nginx_domainname函数获取域名及网站目录的位置
		  从detec_nginx_root获取nginx的安装目录
输出函数：安装成功或失败，nginx的版本号，安装方式，nginx.conf的位置，nginx启动命令位置，nginxctl的位置		
	


###########配置类函数############


######操作类函数#############
