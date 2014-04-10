
#函数名:
#函数功能描述:
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:



###############php查找类函数##############
#函数名：find_php_path
#函数功能描述:查找php文件的安装路径
#支持的安装方式：yum,apt-get,make
#支持的操作系统：CentOS
#函数实现方式描述:通过php命令查看需要的信息

          
#通过php -i命令查看php的编译参数,查找--prefix=的设置          需要验证rpm安装是否正确
INSTALL_PATH=`php  -i  | grep  "Configure Command =>"  | awk  -F '--prefix='   '{print $2}'  |  awk  -F  "'"   '{print  $1}'`

#判断上面"INSTALL_PATH"赋值命令是否成功执行,如果并没有指定--prefix=,则默认安装路径为 /usr/local/php

[ `echo  $?`  == 0 ]  ||  INSTALL_PATH="/usr/local/php"


#函数参数定义
#函数的输出：php的执行路径














#函数名：find_php_ini
#函数功能描述:查找php.ini文件的路径
#支持的安装方式：yum,apt-get,make
#支持的操作系统：CentOS
#函数实现方式描述:通过php命令查看需要的信息

         
#通过php命令并通过截取"Loaded Configuration File:"关键字查看配置文件路径
CONF_PATH=`php  --ini  |  grep  'Loaded Configuration File:'  |  awk  '{print  $4}'`

#函数参数定义
#函数的输出：php.ini的路径

















############检测类函数#######################
#函数名:detec_php_install
#函数功能描述:检测是否安装了php
#支持的操作系统:CentOS
#函数实现方式描述:通过判断执行php  -v命令的返回结果，实现判断php是否安装

php  -v
[ `echo  $?`  == 0 ]  &&  安装  ||  未安装

#函数参数定义:
#函数的输出:是或否













#函数名:detec_php_install_way
#函数功能描述:检测php的安装方式
#支持的操作系统:CentOS
#函数实现方式描述:通过php --ini查看  "Configuration File (php.ini) Path:"的路径,包含/etc的话为rpm安装

 php  --ini  |  grep  "Configuration File (php.ini) Path:"  |awk  '{print  $5}'  |  grep  "^/etc"
 
#判断返回值,0表示rpm安装,非零表示make安装
[ `echo  $?`  == 0 ]  &&  rpm   ||  make  

#函数参数定义:
#函数的输出:yum,apt-get make






#函数名:detec_php_version
#函数功能描述:检测php的版本号
#支持的操作系统:CentOS
#函数实现方式描述:通过使用php  -v查看php版本

VERSION=`php  -v  |  grep  "^PHP"  |  awk  '{print  $2}'`

#函数参数定义:
#函数的输出:php的版本号







#函数名:detec_php_webshell
#函数功能描述:检测是否存在php木马
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:无木马，有木马，木马位置





#函数名:detec_php_badjs
#函数功能描述:检测是否存在恶意js脚本
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:无恶意脚本，有恶意脚本，恶意脚本位置



############安装类函数#################

#函数名:install_yum_php
#函数功能描述:yum方式安装php
#支持的操作系统:CentOS
#函数实现方式描述:同过php命令查看基本信息

#判断是否yum安装php正常
rpm  -q   php
[ `echo  $?`  == 0  ]  &&  正常  ||  不正常，或为使用yum安装

#php命令的路径，此处指grep截取了第一个符合条件的路径，这是由于可能有php命令的软连接，导致有多个路径
COMMAND_PHP=`locate  php  | grep  -m1  "bin\/php$"`
#php-fpm的路径
COMMAND_PHPIZE=`locate  phpize |   grep  -m1 "bin\/phpize$"`
#版本号 
VERSION=`php  -v  |  grep  "^PHP"  |  awk  '{print  $2}'`
#php.ini的路径
CONF_PATH=`php  --ini  |  grep  'Loaded Configuration File:'  |  awk  '{print  $4}'`



#函数参数定义:
#函数的输出:安装成功或失败，php的版本号，php.ini的位置，php的位置，phpize的位置








#函数名:install_apt_php
#函数功能描述:apt-get方式安装php
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:安装成功或失败，php的版本号， 安装成功或失败，php.ini的位置，php的位置，phpize的位置

#函数名:install_make_php
#函数功能描述:源码编译方式安装php
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:安装成功或失败，安装成功或失败，php的版本号，php.ini的位置，php的位置，phpize的位置


