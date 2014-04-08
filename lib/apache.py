




###################查找类函数########################
#函数名
#函数功能描述
#支持的操作系统版本
#支持的安装方式yum apt-get make
#函数实现方式描述
#函数参数含义
#参考代码

##########
#函数名:find_apache_conf_path
#函数功能描述:查找系统中apache主配置文件httpd.conf（CentOS系列）的路径
#支持的操作系统：CentOS 5.8 x64,CentOS 6.x x64 Ubuntu 12.04
#函数实现方式描述
#函数参数含义
#函数的输出 输出httpd.conf所在的目录位置


#函数名:find_apache_bin_path
#函数功能描述:查找系统中apache命令httpd所在的（CentOS系列）的路径
#支持的操作系统：CentOS 5.8 x64,CentOS 6.x x64 Ubuntu 12.04
#函数实现方式描述
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
#函数参数定义
#函数的输出:安装了或未安装
#参考代码




#函数名：detec_apache_install_way
#函数功能描述：检测apache的安装方式
#支持的操作系统：CentOS
#函数实现方式描述
#函数参数定义
#函数的输出:yum（rpm安装）,apt-get,make(源码安装)


#函数名：detec_apache_version
#函数功能描述：检测apache的版本号
#支持的操作系统：
#函数实现方式描述：
#函数参数定义：
#函数的输出：apache的版本号


#函数名：detec_apache_php
#函数功能描述：检测apache是否配置了php模块
#支持的操作系统：
#函数实现方式描述：
#函数参数定义：
#函数的输出：


#函数名：detec_apache_security
#函数功能描述：检测是否安装了mod_security for apache
#支持的操作系统：
#函数实现方式描述：
#函数参数定义：
#函数的输出：

#函数名：detec_apache_listen
#函数功能描述：检测apache的监听端口
#支持的操作系统：
#函数实现方式描述：
#函数参数定义：
#函数的输出：apache的监听端口值


#函数名：detec_apache_work_model
#函数功能描述：检测apache的工作模式是prefork还是worker
#支持的操作系统：
#函数实现方式描述：
#函数参数定义：
#函数的输出：prefork或worker


#函数名：detec_apache_documentroot
#函数功能描述：检测apache中documentroot的值
#支持的操作系统：
#函数实现方式描述：
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


