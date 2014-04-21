
#函数名:
#函数功能描述:
#支持的操作系统:CentOS
#函数实现方式描述:
#函数参数定义:
#函数的输出:



###############第一、php检测类函数##############


*******************************
1.1检测php是否已经安装
*******************************

文件：php.py
函数：检测类 ：detec_php_install
函数功能描述:检测是否安装了php
支持的操作系统:
输入参数：无
输出参数：输出php是否安装 yes|no
函数实现方式描述:通过判断执行php  -v命令的返回结果，实现判断php是否安装

php  -v
[ `echo  $?`  == 0 ]  &&  安装  ||  未安装




*********************************
1.2检测php命令的路径
*********************************

文件：php.py
函数：检测类：detec_php_bin_path
函数功能描述:检测是php的命令路径
支持的操作系统:
输入参数：从detec_php_install函数的输出参数，判断是否安装了php
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
		  从detec_php_install_way函数获取输出参数，判断php的安装方式
输出参数：输出php命令的路径
函数实现方式描述:通过php -i 命令查看需要的信息

          
#通过php -i命令查看php的编译参数,查找--prefix=的设置          需要验证rpm安装是否正确
INSTALL_PATH=`php  -i  | grep  "Configure Command =>"  | awk  -F '--prefix='   '{print $2}'  |  awk  -F  "'"   '{print  $1}'`

#判断上面"INSTALL_PATH"赋值命令是否成功执行,如果并没有指定--prefix=,则默认安装路径为 /usr/local/php

[ `echo  $?`  == 0 ]  ||  INSTALL_PATH="/usr/local/php"





*******************************
1.3检测php的安装方式
*******************************

文件：php.py
函数：检测类 ：detec_php_install_way
函数功能描述:检测php的安装方式
支持的操作系统:
输入参数：从detec_php_install函数的输出参数，判断是否安装了php
		  从detec_os_version函数获取输出参数，系统类型（centos、ubuntu）及版本
输出参数：输出php的安装方式（rpm|make|apt-get）
函数实现方式描述:函数实现方式描述:通过php --ini查看  "Configuration File (php.ini) Path:"的路径,包含/etc的话为rpm安装

 php  --ini  |  grep  "Configuration File (php.ini) Path:"  |awk  '{print  $5}'  |  grep  "^/etc"
 
#判断返回值,0表示rpm安装,非零表示make安装
[ `echo  $?`  == 0 ]  &&  rpm   ||  make  



********************************
1.4检测php的安装版本
********************************

文件：php.py
函数：检测类 ：detec_php_version
函数功能描述:检测php的版本号
支持的操作系统:
输入参数：从detec_php_install函数的输出参数，判断是否安装了php
		  从find_php_bin_path函数的输出参数，得到php命令的路径
输出参数：输出php的安装版本
函数实现方式描述:通过使用php  -v查看php版本

VERSION=`php  -v  |  grep  "^PHP"  |  awk  '{print  $2}'`


*******************************
1.5检测php的安装目录
*******************************

文件：php.py
函数：检测类 ：detec_php_install_path
输入参数：从detec_php_install函数的输出参数，判断是否安装了php
		  从find_php_bin_path函数的输出参数，得到php命令的路径
		  从detec_php_install_way函数的输出参数，得到php的安装方式(rpm|make|apt-get)
输出参数：输出php的安装目录


**********************************
1.6检测配置文件路径
**********************************

文件：php.py
函数：检测类 ：detec_php_ini
函数功能描述:查找php.ini文件的路径
支持的操作系统:
输入参数：从detec_php_install函数的输出参数，判断是否安装了php
		  从detec_php_bin_path函数的输出参数，得到php命令的路径
输出参数：输出php.ini的路径
函数实现方式描述:通过php --ini命令查看需要的信息

         
#通过php命令并通过截取"Loaded Configuration File:"关键字查看配置文件路径
CONF_PATH=`php  --ini  |  grep  'Loaded Configuration File:'  |  awk  '{print  $4}'`



**************************************
1.7检测php的启动命令
**************************************

文件：php.py
函数：




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



############第二、安装类函数#################

**********************************
2.1rpm安装php
**********************************

文件：php.py
函数：安装类 ：install_yum_php
函数功能描述:yum方式安装php
支持的操作系统:
输入参数：从detec_os_version函数获取输出函数，得到系统的类型、版本
输出参数：安装成功或失败，php的版本号，php.ini的位置，php的位置，phpize的位置
函数实现方式描述:通过php命令查看基本信息


#检测系统的版本，根据不同的版本执行不同的命令
releasever=`cat  /etc/issue  |  grep  -iw  "CENTOS"  |  awk  '{print  $3}' |  awk  -F  '.'   '{print  $1}'`

if  [ $releasever == 5 ]
then
	yum  -y install   php53   php53-bcmath  php53-mysql  php53-process  php53-mcrypt  php53-devel  php53-gd  php53-imap  php53-mbstring   php53-pdo  php53-soap   php53-xml  php53-xmlrpc   php53-intl  php53-enchant  php53-php-gettext  php53-pspell mhash-devel mhash  libmcrypt  libmcrypt-devel
else
	if  [ $releasever == 6 ]
	then
		yum -y install php   php-bcmath	 php-mysql  php-process    php-mcrypt   php-devel  php-gd       php-imap    php-mbstring     php-pdo   php-soap   php-xml php-xmlrpc   php-intl      php-enchant   php-php-gettext    php-pspell   mhash-devel mhash   libmcrypt  libmcrypt-devel  php-fpm    
	else
		exit 1
	fi
fi

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


**********************************
2.2apt-get安装php
**********************************

文件：php.py
函数：安装类 ：install_apt_php
函数功能描述:apt-get方式安装php
支持的操作系统:
输入参数：从detec_os_version函数获取输出函数，得到系统的类型、版本
输出参数：安装成功或失败，php的版本号，php.ini的位置，php的位置，phpize的位置
函数实现方式描述




