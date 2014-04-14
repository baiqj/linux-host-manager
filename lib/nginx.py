

#################查找类函数
#函数名：
#函数功能描述：
#支持的操作系统：
#函数实现方式描述：
#函数参数定义：
#函数的输出：

nginx   -t  测试配置文件

#函数名:find_nginx_conf_path
#函数功能描述:查找系统中nginx主配置文件nginx.conf（CentOS系列）的路径
#支持的操作系统：CentOS 5.8 x64,CentOS 6.x x64 Ubuntu 12.04
#函数实现方式描述:

#方法一、通过ps -ef 查看nginx的进程信息，前提条件是需要nginx已经在运行

CONF_PATH=`ps  -ef  | grep nginx  |  grep -iw   "master"  |  awk  -F  '-c '  '{print  $2}'`

#方法二、使用nginx  -t查看安装时的编译参数

nginx  -t   &>   nginx.tmp
CONF_PATH=`grep  -iw  "successful"    nginx.tmp  |  awk  '{print  $4}'`


#函数参数含义
#函数的输出 输出nginx.conf所在的目录位置









#函数名:find_nginx_bin_path
#函数功能描述:查找系统中nginx命令nginx所在的（CentOS系列）的路径
#支持的操作系统：CentOS 5.8 x64,CentOS 6.x x64 Ubuntu 12.04
#函数实现方式描述：

#方法一、通过ps -ef 查看nginx的进程信息，前提条件是需要nginx已经在运行

COMMAND=`ps  -ef  | grep nginx  |  grep -iw   "master" |  awk  -F  '-c '  '{print  $1}'  |  awk   -F   'process '  '{print  $2}'`
 
#方法二、即使nginx没有运行也可以，只是有可能有多个nginx命令路径存在（如nginx软连接）
updatedb
locate  nginx  |  grep  "bin\/nginx$"    >   command.tmp

#函数参数含义
#函数的输出 输出nginx命令所在的路径










#nginx安装路径


nginx  -V  &>  nginx.tmp

INSTALL_PATH=`grep  "configure arguments:"  nginx.tmp  |  awk  -F  "--prefix="  '{print  $2}'  |  awk  '{print  $1}'`

#如果编译安装的nginx,没有指定--prefix=参数,则为变量赋于默认的安装路径/usr/local/nginx

[ `echo  $?`  == 0 ]  ||  INSTALL_PATH="/usr/local/nginx"




#函数名：find_nginx_domainname
#函数功能描述:查找nginx中配置的网站的域名，网站目录位置
#支持的操作系统：CentOS
#函数实现方式描述:
#函数参数定义
#函数的输出

















############检测类函数

#函数名：
#函数功能描述：
#支持的操作系统：
#函数实现方式描述：
#函数参数定义：
#函数的输出：


###########配置类函数############


######操作类函数#############
